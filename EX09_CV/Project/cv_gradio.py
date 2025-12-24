import gradio as gr
import numpy as np
import cv2
import random
import joblib
import face_recognition

# ======================================================
## 각자 만든 모델 로드
# ======================================================
# gender_model = joblib.load("./svc_rbf_model.pkl")
skincolor_model = joblib.load("skincolor_model.pkl")
# age_model = joblib.load("age_model.pkl")
# emotion_model = joblib.load("emotion_model.pkl")


## 범위 잡는거? face_recognition?
# ======================================================
## 사진 피쳐 추출
# ======================================================
def extract_features(img, mode="gray", margin=0.3):
    """
    mode: 'gray' or 'rgb'
    """

    # face_recognition은 RGB 기준
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_img)

    # 얼굴 못 찾으면 fallback
    if len(face_locations) == 0:
        if mode == "gray":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (64, 64))
            gray = gray.astype(np.float32) / 255.0
            return gray.reshape(1, -1)
        else:
            resized = cv2.resize(img, (64, 64))
            resized = resized.astype(np.float32) / 255.0
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

    # ===== 모드별 처리 =====
    if mode == "gray":
        face_crop = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
        face_crop = cv2.resize(face_crop, (64, 64))
        face_crop = face_crop.astype(np.float32) / 255.0
        return face_crop.reshape(1, -1)  # (1, 4096)

    elif mode == "rgb":
        face_crop = cv2.resize(face_crop, (64, 64))
        face_crop = face_crop.astype(np.float32) / 255.0
        return face_crop.reshape(1, -1)  # (1, 12288)


# ======================================================
# 더미 예측 함수
# ======================================================
def predict_dummy(image):
    if image is None:
        return "이미지를 업로드하세요.", "-", "-", "-", "-"

    # (형식상 feature 추출만 호출)
    features = extract_features(image)

    #GENDER_MAP = {0: "남성", 1: "여성"}

    # 더미 예측값
    ethnicity = random.choice(["Asian", "Caucasian", "African"])
    age = random.choice(["10대", "20대", "30대", "40대", "50대+"])
    emotion = random.choice(["Happy", "Neutral", "Sad", "Angry"])

    ## 이후 불러온 모델로 예측
    gray_features = extract_features(image, mode="gray")
    pred = gender_model.predict(gray_features)[0]
    gender = GENDER_MAP[pred]
    print("raw pred:", pred)
    print("mapped:", GENDER_MAP[pred])

    # ethnicity = ethnicity_model.predict(features)[0]
    # age = age_model.predict(features)[0]
    # emotion = emotion_model.predict(features)[0]

    return gender, ethnicity, age, emotion


# ======================================================
# Gradio UI
# ======================================================
with gr.Blocks(title="Face Analysis ML Dashboard (Dummy)") as demo:
    gr.Markdown(
        """
        <br><br>

        <h3>성별 · 인종 · 연령 · 감정 예측 모델</h3>

        <br>
        """
    )

    with gr.Row():
        # ============ LEFT ============
        with gr.Column(scale=1):
            image_input = gr.Image(label="얼굴 사진 업로드", type="numpy")
            submit_btn = gr.Button("분석 실행")

        # ============ RIGHT ============
        with gr.Column(scale=1):
            gender_out = gr.Textbox(label="성별 (더미)", interactive=False)
            ethnicity_out = gr.Textbox(label="인종 (더미)", interactive=False)
            age_out = gr.Textbox(label="연령 (더미)", interactive=False)
            emotion_out = gr.Textbox(label="감정 (더미)", interactive=False)

    submit_btn.click(
        fn=predict_dummy,
        inputs=image_input,
        outputs=[gender_out, ethnicity_out, age_out, emotion_out],
    )

demo.launch()
