def preprocess_text(text):
    # 네가 만든 전처리 함수로 교체
    return text

def text_task_model(text):
    # torch.load("task_model.pth") 이런 식으로 나중에 교체
    return "건축허가"

def priority_model(text):
    return "2순위"

def emotion_model(text):
    return "불만"

def image_task_model(image):
    return "건축허가 (이미지)"



def submit_complaint(image, title, name, phone, content):
    clean_text = preprocess_text(content)

    img_task = image_task_model(image)
    txt_task = text_task_model(clean_text)
    priority = priority_model(clean_text)
    emotion = emotion_model(clean_text)

    return (
        title,
        name,
        phone,
        content,
        img_task,
        txt_task,
        priority,
        emotion
    )


import gradio as gr

with gr.Blocks() as demo:

    gr.Markdown("## 🏛️ AI 민원 처리 시스템")

    with gr.Tabs():

        # =====================
        # 민원인 탭
        # =====================
        with gr.Tab("민원인"):
            gr.Markdown("### 민원 접수")

            with gr.Row():

                # 🔹 왼쪽: 이미지 (크게!)
                with gr.Column(scale=2):
                    image_input = gr.Image(
                        label="📷 사진 업로드",
                        type="numpy",
                        height=420   # ⭐ 핵심
                    )

                # 🔹 오른쪽: 입력폼
                with gr.Column(scale=3):
                    title_input = gr.Textbox(label="제목")
                    name_input = gr.Textbox(label="성함")
                    phone_input = gr.Textbox(label="전화번호")

                    content_input = gr.Textbox(
                        label="민원 내용",
                        lines=6,
                        placeholder="민원 내용을 입력해주세요"
                    )

                    submit_btn = gr.Button("📨 민원 전송")

        # =====================
        # 상담인 탭 (복구 완료)
        # =====================
        with gr.Tab("상담인"):
            gr.Markdown("### 민원 분석 결과")

            out_title = gr.Textbox(label="제목")
            out_name = gr.Textbox(label="성함")
            out_phone = gr.Textbox(label="전화번호")
            out_content = gr.Textbox(label="민원 내용", lines=5)

            out_img_task = gr.Textbox(label="이미지 기반 Task")
            out_txt_task = gr.Textbox(label="텍스트 기반 Task")
            out_priority = gr.Textbox(label="우선순위")
            out_emotion = gr.Textbox(label="감정 상태")

    # 🔗 이벤트 연결
    submit_btn.click(
        fn=submit_complaint,
        inputs=[image_input, title_input, name_input, phone_input, content_input],
        outputs=[
            out_title,
            out_name,
            out_phone,
            out_content,
            out_img_task,
            out_txt_task,
            out_priority,
            out_emotion
        ]
    )

demo.launch()
