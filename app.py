import gradio as gr
import whisper

model = whisper.load_model("base")

def transcribe(audio):
    result = model.transcribe(audio)
    return result["text"]

gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(type="filepath", label="Subí un audio"),
    outputs=gr.Textbox(label="Transcripción"),
    title="Transcriptor de Audios",
    description="Subí un archivo de audio (.wav, .mp3, etc.) y obtené el texto"
).launch(server_name="0.0.0.0", server_port=8080)
