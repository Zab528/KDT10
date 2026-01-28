import gradio as gr

with gr.Blocks(
    title="AI 민원 처리 시스템",
    css="""
    .image-box {
        height: 520px;
    }
    .image-box img {
        object-fit: contain;
        height: 100%;
    }
    """
) as demo:

    gr.Markdown("## 🏛️ AI 기반 민원 처리 시스템")

    with gr.Tabs():

        # =========================
        # 민원인 탭
        # =========================
        with gr.Tab("민원인"):
            gr.Markdown("### 민원 접수")

            with gr.Row():

                # =========================
                # 왼쪽: 이미지
                # =========================
                with gr.Column(scale=1):
                    image_input = gr.Image(
                        label="📷 사진 업로드",
                        type="numpy",
                        elem_classes=["image-box"]
                    )

                # =========================
                # 오른쪽: 입력 폼
                # =========================
                with gr.Column(scale=1):
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

demo.launch()
