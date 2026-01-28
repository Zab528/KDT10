import gradio as gr

with gr.Blocks(
    title="AI 민원 처리 시스템",
    css="""
    /* 이미지 박스 전체 높이 고정 */
    #image_box {
        height: 520px;
    }

    /* 내부 이미지 꽉 채우기 */
    #image_box img {
        height: 100%;
        width: 100%;
        object-fit: contain;
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

                # 왼쪽: 이미지
                with gr.Column(scale=1):
                    image_input = gr.Image(
                        label="📷 사진 업로드",
                        type="numpy",
                        elem_id="image_box"
                    )

                # 오른쪽: 입력
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

        # =========================
        # 상담인 탭 (복구됨)
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

demo.launch()
