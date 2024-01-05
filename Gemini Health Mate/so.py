import streamlit as st
from audio_recorder_streamlit import audio_recorder
from google.cloud import speech_v1p1beta1 as speech

# Set up Google Cloud credentials (replace 'path/to/your/credentials.json' with your actual path)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

def transcribe_audio(audio_bytes):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_bytes)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    return response.results[0].alternatives[0].transcript

audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav", start_time=0, autoplay=True)
    text_result = transcribe_audio(audio_bytes)
    st.write("Transcription:")
    st.write(text_result)
