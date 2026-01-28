import gradio as gr
import numpy as np
import torch
import torch.nn as nn
import re
from konlpy.tag import Okt
import util_func as uf

# =====================================================
# ⚙️ 환경 설정
# =====================================================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MAX_LEN = 50

LABEL_NAMES = [
    "건축허가", "경제", "공통", "교통", "농업축산", "문화체육관광",
    "보건소", "복지", "산림", "상하수도", "세무", "안전건설",
    "위생", "자동차", "정보통신", "토지", "행정", "환경미화"
]

# =====================================================
# 🧠 모델 정의 (train 때랑 동일해야 함)
# =====================================================
class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        x = self.embedding(x.long())
        _, (h_n, _) = self.lstm(x)
        return self.fc(h_n[-1])

# =====================================================
# 🔹 모델 로드 (🔥 핵심 수정 부분)
# =====================================================
VOCAB_SIZE = len(uf.word2idx)
NUM_CLASSES = len(LABEL_NAMES)

model = TextClassifier(
    vocab_size=VOCAB_SIZE,
    embed_dim=128,
    hidden_dim=128,
    num_classes=NUM_CLASSES
).to(DEVICE)

model.load_state_dict(
    torch.load("best_text_model.pth", map_location=DEVICE)
)
model.eval()

# =====================================================
# ✂️ 전처리 (train 때와 동일)
# =====================================================
okt = Okt()
stopwords = ['합니다', '바랍니다', '부탁', '요청', '제발', '주세요', '하십시오']

def preprocess_text(text):
    text = re.sub('[^가-힣 ]', ' ', text)
    nouns = okt.nouns(text)
    nouns = [w for w in nouns if w not in stopwords and len(w) > 1]
    return ' '.join(nouns)

# =====================================================
# 🔮 텍스트 Task 분류 모델
# =====================================================
def text_task_model(text):
    if text is None or text.strip() == "":
        return "입력 없음"

    clean = preprocess_text(text)
    seq = uf.text_to_sequence(clean)
    seq_pad = uf.pad_sequence([seq], max_len=MAX_LEN)

    x = torch.tensor(seq_pad).to(DEVICE)

    with torch.no_grad():
        logits = model(x)
        pred_idx = torch.argmax(logits, dim=1).item()

    return LABEL_NAMES[pred_idx]

# =====================================================
# 🎙️ STT / TTS (더미)
# =====================================================
def stt_func(audio):
    return "음성 인식 결과 텍스트입니다."

def tts_func(text):
    return f"🔊 {text}"

# =====================================================
# 📥 민원 처리 파이프라인
# =====================================================
def submit_complaint(image, title, name, phone, content):
    task = text_task_model(content)

    return (
        title,
        name,
        phone,
        content,
        task
    )

# =====================================================
# 🧠 Gradio UI
# =====================================================
with gr.Blocks() as demo:

    gr.Markdown("## 🏛️ AI 기반 민원 처리 시스템")

    with gr.Tabs():

        # =========================
        # 민원인 탭
        # =========================
        with gr.Tab("민원인"):
            with gr.Row():
                with gr.Column(scale=2):
                    image_input = gr.Image(label="📷 사진 업로드", height=420)

                with gr.Column(scale=3):
                    title_input = gr.Textbox(label="제목")
                    name_input = gr.Textbox(label="성함")
                    phone_input = gr.Textbox(label="전화번호")
                    content_input = gr.Textbox(label="민원 내용", lines=6)
                    audio_input = gr.Audio(source="microphone")
                    stt_btn = gr.Button("🎙️ 음성 → 텍스트")
                    submit_btn = gr.Button("📨 민원 전송")

        # =========================
        # 상담인 탭
        # =========================
        with gr.Tab("상담인"):
            out_title = gr.Textbox(label="제목", interactive=False)
            out_name = gr.Textbox(label="성함", interactive=False)
            out_phone = gr.Textbox(label="전화번호", interactive=False)
            out_content = gr.Textbox(label="민원 내용", interactive=False)
            out_task = gr.Textbox(label="분류 결과", interactive=False)
            tts_btn = gr.Button("🔊 읽어주기")
            tts_out = gr.Textbox(label="TTS 출력")

    # 이벤트 연결
    stt_btn.click(stt_func, audio_input, content_input)
    submit_btn.click(
        submit_complaint,
        [image_input, title_input, name_input, phone_input, content_input],
        [out_title, out_name, out_phone, out_content, out_task]
    )
    tts_btn.click(tts_func, out_content, tts_out)

demo.launch()
