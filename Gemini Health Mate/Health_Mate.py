import time
import requests
from PIL import Image
from io import BytesIO
import speech_recognition as sr
import streamlit as st
import google.generativeai as genai
import elevenlabs
import json
# Set up Streamlit page configuration
st.set_page_config(
    page_title="Heath Mate",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure API keys for generative AI and Eleven Labs
genai.configure(api_key="Gemini_API_Key")
elevenlabs.set_api_key("Elevenslab_API")
# Set up Eleven Labs voice configuration
voice = elevenlabs.Voice(
    voice_id="XrExE9yKIg1WjnnlVkGX",
    settings=elevenlabs.VoiceSettings(
        stability=0,
        similarity_boost=0.85
    ),
)

# Set up generative model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Define safety settings for generative model
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Function to display an image from a given URL
def display_image(img):
    try:
        # Set a custom User-Agent in the request headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Fetch the image from the URL with custom headers
        response = requests.get(img, headers=headers)
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
        st.markdown("⁺₊ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    with st.spinner("Processing..."):
        time.sleep(1)
    try:
        text = recognizer.recognize_google(audio)
        print("Your Question:", text)
        return text
    except sr.UnknownValueError:
        st.warning("Sorry, I could not understand audio.")
        audio = recognizer.listen(source)
        st.markdown("I'm still listening....")
        return ""
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Web Speech API; {e}")
        return ""
# Main function to run the Streamlit application
def main():
    # Initialize chat history in Streamlit session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Streamlit UI components
    st.title("Health Mate")
    st.subheader("Your Personal Wellness Companion.")
    image = None
    # Image upload section
    with st.expander("Upload Image"):
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # Display the uploaded image
           image = Image.open(uploaded_file)
           st.image(image, caption="Uploaded Image",use_column_width=True)

    # Enable Speech Input button
    if st.button("Enable Speech Input", key="speech_input_button"):
        user_question = st.chat_input("Ask your question:")
        user_question = recognize_speech()
        if user_question is not None:
            st.write("Your Question:", user_question)
    else:
        user_question = st.chat_input("Ask your question:")
        if user_question is not None:
            st.write("Your Question:", user_question)

    # Process user input based on the presence of an image
    if image is None and user_question:
        model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)
        chat = model.start_chat(history=[])
        response = chat.send_message(f"""Act as my fitness expert and diet nutritionist, responding with short, friendly, and easily understandable answers. Kindly answer me this {user_question}""", stream=True)
        response.resolve() 
        st.markdown(response.text)
        file_path = "chat_history.json"
        try:
            with open(file_path, "r") as file:
                chat_history = json.load(file)
        except FileNotFoundError:
            chat_history = []
        audio = elevenlabs.generate(
                text=response.text, 
                voice="Matilda")
        elevenlabs.play(audio)

        st.session_state.chat_history.append({"user": user_question, "response": chat.history[1].parts[0]})
        with open(file_path, "w") as file:
            json.dump(chat_history, file, indent=2)

    elif image is not None and user_question:
        model = genai.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat(history=[])
        response = chat.send_message([f"""Act as my Expert nutritionist Doctor and fitness expert. {user_question}""", image], stream=True)
        response.resolve() 
        st.markdown(response.text)
        file_path = "chat_history.json"
        try:
            with open(file_path, "r") as file:
                chat_history = json.load(file)
        except FileNotFoundError:
            chat_history = []
            
        audio = elevenlabs.generate(
                text=response.text, 
                voice="Matilda")
        elevenlabs.play(audio)

        st.session_state.chat_history.append({"user": user_question, "response": chat.history[1].parts[0]})
        with open(file_path, "w") as file:
            json.dump(chat_history, file, indent=2)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
