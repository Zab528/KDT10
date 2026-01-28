import gradio as gr
import numpy as np

# =========================
# 🔧 더미 모델 함수들
# =========================

def image_task_classifier(image):
    return "건축허가 (이미지 기반)"

def text_task_classifier(text):
    return "건축허가"

def priority_classifier(text):
    return "2순위 (중)"

def emotion_classifier(text):
    return "불안 / 불만"

def profanity_filter(text):
    return "비속어 없음"

def pii_filter(name, phone):
    return f"이름: {name}, 전화번호: {phone}"

def stt_func(audio):
    return "음성에서 변환된 민원 내용입니다."

def tts_func(text):
    return "🔊 (TTS 음성 출력)"

# =========================
# 📥 민원 전송 처리
# =========================

def submit_complaint(image, title, name, phone, content):
    img_task = image_task_classifier(image)
    txt_task = text_task_classifier(content)
    priority = priority_classifier(content)
    emotion = emotion_classifier(content)
    profanity = profanity_filter(content)
    pii = pii_filter(name, phone)

    return (
        title,
        content,
        img_task,
        txt_task,
        priority,
        emotion,
        profanity,
        pii
    )

# =========================
# 🧠 Gradio UI
# =========================

with gr.Blocks(title="AI 민원 처리 시스템") as demo:

    gr.Markdown("## 🏛️ AI 기반 민원 처리 시스템")

    with gr.Tabs():

        # =========================
        # 민원인 탭
        # =========================
        with gr.Tab("민원인"):
            gr.Markdown("### 민원 접수")

            with gr.Row():

                # =========================
                # 왼쪽: 이미지 입력
                # =========================
                with gr.Column(scale=1.5):
                    image_input = gr.Image(
                        label="📷 사진 업로드",
                        type="numpy"
                    )

                # =========================
                # 오른쪽: 텍스트 입력
                # =========================
                with gr.Column(scale=1.5):
                    title_input = gr.Textbox(label="제목")
                    name_input = gr.Textbox(label="성함")
                    phone_input = gr.Textbox(label="전화번호")

                    content_input = gr.Textbox(
                        label="민원 내용",
                        lines=6,
                        placeholder="민원 내용을 입력해주세요"
                    )

                    audio_input = gr.Audio(
                        source="microphone",
                        type="numpy",
                        label="🎙️ 음성 입력"
                    )

                    stt_btn = gr.Button("🎙️ 음성 → 텍스트")
                    submit_btn = gr.Button("📨 민원 전송")

        # =========================
        # 상담인 탭
        # =========================
        with gr.Tab("상담인"):
            gr.Markdown("### 민원 분석 결과")

            out_title = gr.Textbox(label="제목", interactive=False)
            out_content = gr.Textbox(label="민원 내용", lines=5, interactive=False)

            out_img_task = gr.Textbox(label="이미지 기반 Task", interactive=False)
            out_txt_task = gr.Textbox(label="텍스트 기반 Task", interactive=False)
            out_priority = gr.Textbox(label="우선순위", interactive=False)
            out_emotion = gr.Textbox(label="감정 상태", interactive=False)
            out_profanity = gr.Textbox(label="비속어 필터링", interactive=False)
            out_pii = gr.Textbox(label="개인정보", interactive=False)

            tts_btn = gr.Button("🔊 요약 읽어주기")
            tts_output = gr.Textbox(label="TTS 출력", interactive=False)

    # =========================
    # 🔗 이벤트 연결
    # =========================

    stt_btn.click(
        fn=stt_func,
        inputs=audio_input,
        outputs=content_input
    )

    submit_btn.click(
        fn=submit_complaint,
        inputs=[image_input, title_input, name_input, phone_input, content_input],
        outputs=[
            out_title,
            out_content,
            out_img_task,
            out_txt_task,
            out_priority,
            out_emotion,
            out_profanity,
            out_pii
        ]
    )

    tts_btn.click(
        fn=tts_func,
        inputs=out_content,
        outputs=tts_output
    )

demo.launch()
