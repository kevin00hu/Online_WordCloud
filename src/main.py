import gradio as gr

from .utils import generate_wordcloud

#=======================================================#

with gr.Blocks() as demo:
    gr.Markdown("# WordCloud Generator")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="input text",
                                    lines=10,
                                    placeholder="Put text here")
            extra_stop_words = gr.Textbox(label="stop words",
                                          placeholder="Exclude words here (Support RE)")
            generate_button = gr.Button("Generate!")
        
        with gr.Column():
            wordcloud = gr.Image(label="Word Cloud", height=500)

    generate_button.click(fn=generate_wordcloud,
                          inputs=input_text,
                          outputs=wordcloud)

demo.launch(server_name="0.0.0.0", server_port=8888)