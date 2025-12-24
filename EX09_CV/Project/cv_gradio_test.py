import gradio as gr
import numpy as np
import cv2
import joblib
import face_recognition

# =========================
# 모델 로드
# =========================
skincolor_model = joblib.load("skincolor_model.pkl")

# ⚠️ 민감특성(인종 등) 라벨은 지양. 중립 라벨로 표기 권장
LABEL_MAP = {
    0: "Class A",
    1: "Class B",
    2: "Class C",
}

def extract_features(img, mode="rgb", margin=0.3):
    # face_recognition은 RGB 기준
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_img)

    # 얼굴 못 찾으면 fallback (전체 이미지 사용)
    if len(face_locations) == 0:
        resized = cv2.resize(img, (64, 64))
        resized = resized.astype(np.float32) / 255.0
        if mode == "gray":
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            return gray.reshape(1, -1)
        return resized.reshape(1, -1)

    top, right, bottom, left = face_locations[0]
    h, w, _ = img.shape

    face_h = bottom - top
    face_w = right - left
    m_h = int(face_h * margin)
    m_w = int(face_w * margin)

    top = max(0, top - m_h)
    bottom = min(h, bottom + m_h)
    left = max(0, left - m_w)
    right = min(w, right + m_w)

    face_crop = img[top:bottom, left:right]

    if mode == "gray":
        face_crop = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
        face_crop = cv2.resize(face_crop, (64, 64))
        face_crop = face_crop.astype(np.float32) / 255.0
        return face_crop.reshape(1, -1)

    # rgb
    face_crop = cv2.resize(face_crop, (64, 64))
    face_crop = face_crop.astype(np.float32) / 255.0
    return face_crop.reshape(1, -1)

def predict_skin_model(image):
    if image is None:
        return "이미지를 업로드하세요.", "-", "-", "-"

    X = extract_features(image, mode="rgb")  # 네 학습 방식에 맞춰 'rgb'/'gray' 선택

    pred = skincolor_model.predict(X)[0]
    pred_label = LABEL_MAP.get(int(pred), str(pred))

    # 확률 출력(모델이 predict_proba 지원할 때만)
    proba_text = "-"
    if hasattr(skincolor_model, "predict_proba"):
        proba = skincolor_model.predict_proba(X)[0]
        # 예쁘게 문자열로
        proba_text = ", ".join([f"{LABEL_MAP.get(i, i)}:{p*100:.1f}%" for i, p in enumerate(proba)])

    return pred_label, proba_text, str(X.shape), "face_recognition crop 사용"

with gr.Blocks(title="3-Class Image Model Test") as demo:
    gr.Markdown("### 이미지 업로드 → (중립 라벨) 3클래스 분류 모델 테스트")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="이미지 업로드", type="numpy")
            submit_btn = gr.Button("분석 실행")

        with gr.Column():
            pred_out = gr.Textbox(label="예측 결과", interactive=False)
            proba_out = gr.Textbox(label="확률", interactive=False)
            shape_out = gr.Textbox(label="입력 feature shape", interactive=False)
            note_out = gr.Textbox(label="비고", interactive=False)

    submit_btn.click(
        fn=predict_skin_model,
        inputs=image_input,
        outputs=[pred_out, proba_out, shape_out, note_out],
    )

demo.launch()
