import gradio as gr
import numpy as np
import torch
import re
from konlpy.tag import Okt
import util_func as uf

# =====================================================
# 🔧 환경 설정
# =====================================================

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MAX_LEN = 50

# =====================================================
# 🔖 라벨 매핑
# =====================================================

LABEL_MAP = {
    0: "건축허가",
    1: "경제",
    2: "공통",
    3: "교통",
    4: "농업축산",
    5: "문화체육관광",
    6: "보건소",
    7: "복지",
    8: "산림",
    9: "상하수도",
    10: "세무",
    11: "안전건설",
    12: "위생",
    13: "자동차",
    14: "정보통신",
    15: "토지",
    16: "행정",
    17: "환경미화"
}

# =====================================================
# 🔧 전처리 (train 때와 동일)
# =====================================================

okt = Okt()
stopwords = ['합니다', '바랍니다', '부탁', '요청', '제발', '주세요', '하십시오']

def preprocess_text(text):
    text = re.sub('[^가-힣 ]', ' ', text)
    nouns = okt.nouns(text)
    nouns = [w for w in nouns if w not in stopwords and len(w) > 1]
    return ' '.join(nouns)

# =====================================================
# 🤖 모델 로드
# =====================================================

model = torch.load("best_text_model.pth", map_location=DEVICE)
model.eval()

# =====================================================
# 🧠 텍스트 Task 분류 모델 (핵심!)
# =====================================================

def text_task_model(text):
    if text is None or text.strip() == "":
        return "입력 없음"

    clean = preprocess_text(text)

    # util_func에 있던 방식 그대로 사용
    seq = uf.text_to_sequence(clean)
    seq_pad = uf.pad_sequence([seq], max_len=MAX_LEN)

    x = torch.tensor(seq_pad, dtype=torch.float32).to(DEVICE)

    with torch.no_grad():
        logits = model(x)
        pred_idx = torch.argmax(logits, dim=1).item()

    return LABEL_MAP[pred_idx]

# =====================================================
# 더미 모델들 (나중에 교체)
# =====================================================

def image_task_model(image):
    return "건축허가 (이미지)"

def priority_model(text):
    return "2순위 (중)"

def emotion_model(text):
    return "불만 / 불안"

def profanity_filter(text):
    return "비속어 없음"

def pii_filter(name, phone):
    return f"이름: {name}, 전화번호: {phone}"

def stt_func(audio):
    return "🎤 음성에서 변환된 민원 내용입니다."

def tts_func(text):
    return f"🔊 {text}"

# =====================================================
# 📥 민원 처리
# =====================================================

def submit_complaint(image, title, name, phone, content):
    txt_task = text_task_model(content)

    return (
        title,
        name,
        phone,
        content,
        image_task_model(image),
        txt_task,
        priority_model(content),
        emotion_model(content),
        profanity_filter(content),
        pii_filter(name, phone)
    )
