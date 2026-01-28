import torch
import re
from konlpy.tag import Okt
import joblib   # vectorizer 저장했을 경우

# =====================
# 설정
# =====================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

LABEL_NAMES = [
    "건축허가", "경제", "공통", "교통", "농업축산", "문화체육관광",
    "보건소", "복지", "산림", "상하수도", "세무", "안전건설",
    "위생", "자동차", "정보통신", "토지", "행정", "환경미화"
]

# =====================
# 모델 클래스 (train.py랑 완전히 동일해야 함)
# =====================
import torch.nn as nn

class TextClassifier(nn.Module):
    def __init__(self, input_dim, num_classes=18):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, 256)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(256, num_classes)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

# =====================
# 벡터라이저 로드
# (train 때 저장한 것)
# =====================
vectorizer = joblib.load("vectorizer.pkl")
INPUT_DIM = vectorizer.transform(["임시"]).shape[1]

# =====================
# 모델 로드
# =====================
model = TextClassifier(INPUT_DIM).to(DEVICE)
model.load_state_dict(
    torch.load("best_text_model.pth", map_location=DEVICE)
)
model.eval()

# =====================
# 전처리 (train과 동일)
# =====================
okt = Okt()
stopwords = ['합니다', '바랍니다', '부탁', '요청', '제발', '주세요']

def preprocess(text):
    text = re.sub('[^가-힣 ]', ' ', text)
    nouns = okt.nouns(text)
    nouns = [w for w in nouns if w not in stopwords and len(w) > 1]
    return " ".join(nouns)

# =====================
# ⭐ Gradio에서 쓰는 함수
# =====================
def predict_text_task(text: str) -> str:
    if not text or text.strip() == "":
        return "입력 없음"

    clean = preprocess(text)
    vec = vectorizer.transform([clean]).toarray()
    x = torch.tensor(vec, dtype=torch.float32).to(DEVICE)

    with torch.no_grad():
        logits = model(x)
        pred = torch.argmax(logits, dim=1).item()

    return LABEL_NAMES[pred]
