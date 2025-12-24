import gradio as gr
import numpy as np
import cv2
import joblib

FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# =========================
# 1) 모델 로드
# =========================
MODEL_FILE = "./skincolor_model.pkl"
model = joblib.load(MODEL_FILE)

# 라벨 매핑 (모델 예측값 -> 한글)
LABEL_MAP = {
    "white": "백인",
    "yellow": "황인",
    "black": "흑인",
}

# =========================
# 2) 전처리 (학습 때 방식 최대한 맞추기)
#    - Gradio numpy 이미지는 보통 RGB
#    - OpenCV 학습은 보통 BGR(cv2.imread)였을 확률 높음 → RGB->BGR 변환 권장
#    - (70,70)으로 resize 후 1차원 벡터
# =========================
def preprocess_for_model(img_rgb: np.ndarray) -> np.ndarray:
    if img_rgb is None:
        return None

    # uint8 보장
    if img_rgb.dtype != np.uint8:
        img_rgb = img_rgb.astype(np.uint8)

    # RGB -> BGR (cv2.imread와 일치시키려고)
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    # 학습 코드가 fx=0.5 후 (70,70) 했던 경우가 많지만,
    # 예측에서는 핵심이 최종 (70,70) 형태 맞추는 것이라 여기서는 바로 (70,70)로 통일
    img_bgr = cv2.resize(img_bgr, (70, 70), interpolation=cv2.INTER_AREA)

    # flatten -> (1, 70*70*3)
    x = img_bgr.reshape(1, -1)
    return x

def detect_face_and_draw(img_rgb: np.ndarray):
    if img_rgb is None:
        return None, None

    # RGB → BGR
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60, 60)
    )

    if len(faces) == 0:
        return img_rgb, None

    # 가장 큰 얼굴 하나 선택
    x, y, w, h = max(faces, key=lambda f: f[2]*f[3])

    # 네모 박스 그리기
    cv2.rectangle(
        img_bgr,
        (x, y), (x+w, y+h),
        (0, 255, 0), 2
    )

    # 얼굴 crop
    face_crop = img_bgr[y:y+h, x:x+w]

    # 다시 RGB로
    img_boxed = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    return img_boxed, face_crop


# =========================
# 3) 예측 함수
# =========================
def detect_face_and_draw(img_rgb: np.ndarray):
    if img_rgb is None:
        return None, None

    # RGB → BGR
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60, 60)
    )

    if len(faces) == 0:
        return img_rgb, None

    # 가장 큰 얼굴 하나 선택
    x, y, w, h = max(faces, key=lambda f: f[2]*f[3])

    # 네모 박스 그리기
    cv2.rectangle(
        img_bgr,
        (x, y), (x+w, y+h),
        (0, 255, 0), 2
    )

    # 얼굴 crop
    face_crop = img_bgr[y:y+h, x:x+w]

    # 다시 RGB로
    img_boxed = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    return img_boxed, face_crop


# =========================
# 4) Gradio UI
# =========================
with gr.Blocks(title="인종(피부톤) 분류") as demo:
    gr.Markdown("## 얼굴 인종(피부톤) 분류 – 얼굴 검출 기반")

    with gr.Row():
        with gr.Column(scale=1):
            img_in = gr.Image(
                label="이미지 업로드 / 웹캠",
                type="numpy",
                sources=["upload", "webcam"]
            )
            btn = gr.Button("분석 실행")

        with gr.Column(scale=1):
            img_out = gr.Image(label="얼굴 검출 결과")
            out_pred = gr.Textbox(label="예측 결과", interactive=False)
            out_proba = gr.Textbox(label="클래스별 확률", interactive=False)
            out_classes = gr.Textbox(label="model.classes_", interactive=False)

    btn.click(
        fn=predict_ethnicity_with_face,
        inputs=img_in,
        outputs=[img_out, out_pred, out_proba, out_classes]
    )

demo.launch()
