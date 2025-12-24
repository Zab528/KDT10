import gradio as gr
import numpy as np
import cv2

# ✅ MediaPipe 설치 필요:
# pip install mediapipe

import mediapipe as mp

mp_face = mp.solutions.face_detection

# -----------------------------
# 얼굴 검출 + 박스 그리기 + crop
# -----------------------------
def detect_and_crop(img_rgb: np.ndarray, conf_th=0.6, margin=0.25):
    """
    img_rgb: gradio에서 들어오는 RGB 이미지 (H,W,3)
    return:
      boxed_rgb: 얼굴 박스 그린 RGB 이미지
      crop_rgb : 얼굴 crop RGB 이미지 (없으면 None)
    """
    if img_rgb is None:
        return None, None

    # mediapipe는 RGB 입력 사용
    h, w, _ = img_rgb.shape

    boxed = img_rgb.copy()
    crop = None

    with mp_face.FaceDetection(model_selection=0, min_detection_confidence=conf_th) as detector:
        results = detector.process(img_rgb)

        if not results.detections:
            return boxed, None

        # 가장 큰 얼굴 1개만 사용(원하면 여러개로 확장 가능)
        best = None
        best_area = -1

        for det in results.detections:
            bbox = det.location_data.relative_bounding_box
            x1 = int(bbox.xmin * w)
            y1 = int(bbox.ymin * h)
            bw = int(bbox.width * w)
            bh = int(bbox.height * h)
            x2 = x1 + bw
            y2 = y1 + bh
            area = bw * bh
            if area > best_area:
                best_area = area
                best = (x1, y1, x2, y2)

        x1, y1, x2, y2 = best

        # margin 적용
        mw = int((x2 - x1) * margin)
        mh = int((y2 - y1) * margin)
        x1 = max(0, x1 - mw)
        y1 = max(0, y1 - mh)
        x2 = min(w, x2 + mw)
        y2 = min(h, y2 + mh)

        # 박스 그리기 (OpenCV는 BGR이지만 여기선 RGB에 직접 rectangle 그려도 됨)
        cv2.rectangle(boxed, (x1, y1), (x2, y2), (0, 255, 0), 2)

        crop = img_rgb[y1:y2, x1:x2].copy() if (x2 > x1 and y2 > y1) else None

    return boxed, crop

# -----------------------------
# Gradio 버튼용: "캡처"를 누르면 crop 결과를 고정 표시
# -----------------------------
def capture_face(img_rgb):
    boxed, crop = detect_and_crop(img_rgb)
    if crop is None:
        return boxed, None, "얼굴을 찾지 못했습니다."
    return boxed, crop, "캡처 완료: 얼굴 crop 생성"

# -----------------------------
# UI
# -----------------------------
with gr.Blocks(title="웹캠 얼굴 검출 + 캡처") as demo:
    gr.Markdown("## 웹캠 얼굴 검출(박스 표시) + 캡처(얼굴 crop)")

    with gr.Row():
        with gr.Column():
            cam = gr.Image(
                label="웹캠 입력",
                type="numpy",
                sources=["webcam"]  # 웹캠만
            )
            btn = gr.Button("캡처(얼굴 crop)")

        with gr.Column():
            out_boxed = gr.Image(label="얼굴 박스 표시 결과", type="numpy")
            out_crop  = gr.Image(label="캡처된 얼굴 crop", type="numpy")
            msg = gr.Textbox(label="상태", interactive=False)

    # 버튼 클릭 시: 박스 이미지 + crop 이미지 반환
    btn.click(fn=capture_face, inputs=cam, outputs=[out_boxed, out_crop, msg])

demo.launch()
