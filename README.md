# Traductor de Voz Español → Inglés con IA

Este proyecto es un traductor de voz que funciona de manera sencilla:

1. Le das un **audio en español**.  
2. El sistema **transcribe** el audio a texto usando Whisper.  
3. Luego, **traduce** el texto al inglés.  
4. Finalmente, devuelve el texto en inglés **con una voz generada por IA** usando ElevenLabs.  

---

## Características

- Traducción **automática de voz a voz**.
- Interfaz web sencilla con **Gradio**.
- Audio de salida generado con **voz de IA realista**.
- Basado en el vídeo de **Mouredev en YouTube**.

---

## Requisitos

- Librerías necesarias:
  - `gradio`
  - `whisper`
  - `translate`
  - `python-dotenv`
  - `elevenlabs`
- **FFmpeg** instalado en tu sistema si no whisper da errores
