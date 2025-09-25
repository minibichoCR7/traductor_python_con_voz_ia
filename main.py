import gradio as gr
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

"""
he usado 

gradio
openai-whisper
translate
python-dotenv
elevenlabs

"""
config = dotenv_values(".env")
api_key = config["ELEVENLABS_API_KEY"]
def translator(audio_file):

    #transcribir texto

    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error transcribiendo el texto: {str(e)}")


    #traducir texto
    try:
        en_transcription = Translator(
            from_lang="es", to_lang="en").translate(transcription)
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error traduciendo el texto: {str(e)}")


    #generar audio traducido
    en_save_file_path = text_to_speach(en_transcription, "en")

    return en_save_file_path

def text_to_speach(text: str, language: str) -> str:

    try:
        client = ElevenLabs(api_key=api_key)

        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  #voz por defecto y todo por defecto lo unico que se ha cambiado es el text para que reciba nuestra traduccion
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=0.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        save_file_path = f"{language}.mp3"

        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error creando el audio: {str(e)}")

    return save_file_path


web = gr.Interface(
    fn=translator,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath",
        label="Español"
    ),
    outputs=[
        gr.Audio(label="Inglés"),
    ],
    title="traductor español a ingles con voz de ia",
    description="Traductor de voz hecho con python"
)

web.launch()
