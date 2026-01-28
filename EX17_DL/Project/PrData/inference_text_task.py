import torch
import re
from konlpy.tag import Okt
import util_func as uf

# =========================
# 설정
# =========================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MAX_LEN = 50

LABEL_NAMES = [
    "건축허가", "경제", "공통", "교통", "농업축산", "문화체육관광",
    "보건소", "복지", "산림", "상하수도", "세무", "안전건설",
    "위생", "자동차", "정보통신", "토지", "행정", "환경미화"
]

# =========================
# 모델 정의 (train 때와 동일)
# =========================
import torch.nn as nn

class TextClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(5000, 128)
        self.lstm = nn.LSTM(128, 128, batch_first=True)
        self.fc = nn.Linear(128, 18)

    def forward(self, x):
        x = self.embedding(x.long())
        _, (h, _) = self.lstm(x)
        return self.fc(h[-1])

# =========================
# 모델 로드 (1번만)
# =========================
model = TextClassifier().to(DEVICE)
model.load_state_dict(
    torch.load("best_text_model.pth", map_location=DEVICE)
)
model.eval()

# =========================
# 전처리 (train과 동일)
# =========================
okt = Okt()
stopwords = ['합니다', '바랍니다', '부탁', '요청', '제발', '주세요', '하십시오']

def _preprocess(text):
    text = re.sub('[^가-힣 ]', ' ', text)
    nouns = okt.nouns(text)
    nouns = [w for w in nouns if w not in stopwords and len(w) > 1]
    return ' '.join(nouns)

# =========================
# ⭐ 외부 공개용 함수 (이거 하나만!)
# =========================
def predict_text_task(text: str) -> str:
    if text is None or text.strip() == "":
        return "입력 없음"

    clean = _preprocess(text)
    seq = uf.text_to_sequence(clean)
    seq_pad = uf.pad_sequence([seq], max_len=MAX_LEN)

    x = torch.tensor(seq_pad).to(DEVICE)

    with torch.no_grad():
        logits = model(x)
        pred = torch.argmax(logits, dim=1).item()

    return LABEL_NAMES[pred]
