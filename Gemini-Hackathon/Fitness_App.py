import requests
from PIL import Image
from io import BytesIO
import speech_recognition as sr
import streamlit as st
import google.generativeai as genai
import elevenlabs

genai.configure(api_key="AIzaSyA781SBF8gVIb7vrN8Yz7KEbRyuXdE0blo")
elevenlabs.set_api_key("Elevenslab_API")
voice = elevenlabs.Voice(  # elevens lab configurations
            voice_id="XrExE9yKIg1WjnnlVkGX",
             settings=elevenlabs.VoiceSettings(
                 stability=0, 
                 similarity_boost=0.85),
            )

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]


def display_image_from_url(url):
    try:
        # Set a custom User-Agent in the request headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Fetch the image from the URL with custom headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Open the image using Pillow
        image = Image.open(BytesIO(response.content))

        # Return the opened image
        return image

    except Exception as e:
        print(f"Error: {e}")
        return None


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        st.markdown("I'm listening....")
    try:
        text = recognizer.recognize_google(audio)
        print("Your Question:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
        audio = recognizer.listen(source)
        st.markdown("I'm stil listening....")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return ""

def main():
        
    st.title("HealthMate")
    image = None
    st.subheader("Your Personal Wellness Companion.")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display the uploaded image
         image = Image.open(uploaded_file)
         st.image(image, caption="Uploaded Image", use_column_width=True)
    if st.button("Enable Speech Input (Optional)", key="speech_input_button"):
            user_question = recognize_speech()
            st.write("Your Question:", user_question)
    else:
                # Default text input
           user_question = st.chat_input("Ask your question:")
           st.write("Your Question:", user_question)
    if image is None and user_question:
            model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)
            response = model.generate_content(f"""Act as my fitness expert and diet nutritionist{user_question}""")
            st.markdown(response.text)
            # audio = elevenlabs.generate(
            #     text=response.text, 
            #     voice="Matilda")
            # elevenlabs.play(audio)

    elif image is not None and user_question:
        model = genai.GenerativeModel("gevisionmini-pro-")
        response = model.generate_content([f"""Act as my fitness expert and diet nutritionist , At this moment, kindly assist with this {user_question}""", image], stream=True)
        response.resolve() 
        st.markdown(response.text)
        # audio = elevenlabs.generate(
        #         text=response.text, 
        #         voice="Matilda")
        # elevenlabs.play(audio)

if __name__ == "__main__":
    main()