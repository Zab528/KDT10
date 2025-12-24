import gradio as gr
import cv2
import numpy as np
import joblib

# =====================================
# 1. 모델 로드
# =====================================
MODEL_FILE = "./skincolor_model.pkl"
model = joblib.load(MODEL_FILE)

# =====================================
# 2. 이미지 전처리 함수
#    (학습 때와 반드시 동일해야 함)
# =====================================
def preprocess_image(img):
    """
    img: gr.Image(type="numpy") → BGR numpy array
    return: (1, N) feature vector
    """
    # resize (학습 때 사용한 크기로!)
    img = cv2.resize(img, (70, 70), interpolation=cv2.INTER_AREA)

    # flatten
    img = img.reshape(1, -1)

    return img

# =====================================
# 3. 예측 함수
# =====================================
def predict_skincolor(image):
    if image is None:
        return "이미지를 업로드해주세요."

    x = preprocess_image(image)

    pred_label = model.predict(x)[0]

    # 확률까지 보고 싶으면
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(x)[0]
        classes = model.classes_

        prob_text = " / ".join(
            [f"{cls}: {p*100:.1f}%" for cls, p in zip(classes, proba)]
        )

        return f"예측 인종: {pred_label}\n확률: {prob_text}"

    return f"예측 인종: {pred_label}"

# =====================================
# 4. Gradio UI
# =====================================
with gr.Blocks(title="인종 분류 모델 테스트") as demo:
    gr.Markdown(
        """
        ## 🧑 얼굴 이미지 기반 인종 분류 모델  
        **분류 클래스:** White / Yellow / Black  
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(label="얼굴 이미지 업로드", type="numpy")
            predict_btn = gr.Button("분석 실행")

        with gr.Column(scale=1):
            output_text = gr.Textbox(
                label="예측 결과",
                interactive=False,
                lines=3
            )

    predict_btn.click(
        fn=predict_skincolor,
        inputs=image_input,
        outputs=output_text
    )

demo.launch()
