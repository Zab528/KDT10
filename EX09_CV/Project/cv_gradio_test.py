import gradio as gr
import numpy as np
import cv2
import joblib

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

# =========================
# 3) 예측 함수
# =========================
def predict_ethnicity(image):
    if image is None:
        return "이미지를 업로드하거나 웹캠으로 촬영한 뒤 분석 실행을 눌러주세요.", "-", "-"

    x = preprocess_for_model(image)
    pred = model.predict(x)[0]               # 'white'/'yellow'/'black' 예상
    proba = model.predict_proba(x)[0]        # 클래스 순서는 model.classes_ 기준

    pred_kr = LABEL_MAP.get(str(pred), str(pred))

    # 확률도 같이 보여주기 (원하면 제거 가능)
    classes = [LABEL_MAP.get(c, c) for c in model.classes_]
    proba_text = ", ".join([f"{cls}:{p*100:.1f}%" for cls, p in zip(classes, proba)])

    return pred_kr, proba_text, str(model.classes_)

# =========================
# 4) Gradio UI
# =========================
with gr.Blocks(title="인종(피부톤) 분류: 백인/황인/흑인") as demo:
    gr.Markdown("## 얼굴 이미지 인종(피부톤) 분류 (백인/황인/흑인)\n- 업로드 또는 웹캠 촬영 후 **분석 실행**을 누르세요.")

    with gr.Row():
        with gr.Column(scale=1):
            img_in = gr.Image(
                label="이미지 업로드 / 웹캠",
                type="numpy",
                sources=["upload", "webcam"]  # ✅ 웹캠 포함
            )
            btn = gr.Button("분석 실행")

        with gr.Column(scale=1):
            out_pred = gr.Textbox(label="예측 결과", interactive=False)
            out_proba = gr.Textbox(label="클래스별 확률", interactive=False)
            out_classes = gr.Textbox(label="model.classes_ (참고용)", interactive=False)

    btn.click(
        fn=predict_ethnicity,
        inputs=img_in,
        outputs=[out_pred, out_proba, out_classes]
    )

demo.launch()
