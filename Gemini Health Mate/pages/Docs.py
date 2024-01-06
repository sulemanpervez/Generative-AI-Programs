import streamlit as st

# HealthMate Wellness Companion Documentation

# Introduction
st.title("HealthMate Wellness Companion")

st.write("Welcome to the documentation for Gemini HealthMate, your personal wellness companion. This guide covers the various components and functionalities of the HealthMate application.")

# Section 1: Importing Necessary Tools
st.header("1. Importing Necessary Tools")

st.write("In this section, we import the required tools and libraries for the HealthMate Wellness Companion.")
st.code("""
import requests
from PIL import Image
from io import BytesIO
import speech_recognition as sr
import streamlit as st
import google.generativeai as genai
import elevenlabs
import json
""")

# Section 2: Setting up the Look and Feel
st.header("2. Setting up the Look and Feel")

st.write("This section focuses on configuring the appearance of the HealthMate app.")
st.code("""
st.set_page_config(
    page_title="Health Mate",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
""")

# Section 3: Keys to the Kingdom
st.header("3. Keys to the Kingdom")

st.write("Here, we ensure the app has the right access by using API keys.")
st.code("""
genai.configure(api_key="Gemini_API")
elevenlabs.set_api_key("Elevenslab_API")
""")

# Section 4: Talking with Style
st.header("4. Talking with Style")

st.write("This part gives the app a unique voice using Eleven Labs.")
st.code("""
voice = elevenlabs.Voice(
    voice_id="XrExE9yKIg1WjnnlVkGX",
    settings=elevenlabs.VoiceSettings(
        stability=0,
        similarity_boost=0.85
    ),
)
""")

# Section 5: Adding Some AI Magic
st.header("5. Adding Some AI Magic")

st.write("""Here, we're setting up the rules for our Gemini generative AI. It's like telling it how creative or straightforward it should be when responding to users.""")
st.code("""
generation_config = {
   "temperature": 0.9,
   "top_p": 1,
   "top_k": 1,
   "max_output_tokens": 2048,
}
""")

# Section 6: Keeping It Safe
st.header("6. Keeping It Safe")

st.write("Safety first! We're setting guidelines for our Gemini AI to make sure it doesn't say anything inappropriate. It's like having a moderator to keep conversations respectful. Its optional because model is predefined these safety_settings")
st.code("""
safety_settings = [
   {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
   {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
   {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
   {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
""")

# Section 7: Showing Off Images
st.header("7. Showing Off Images")

st.write("We're creating a feature to show images. It's like opening a photo album to share pictures with users.")
st.subheader("1. User-Agent Setup:")
st.code("""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
""")


# Error Handling
st.subheader("2. Error Handling:")
st.code("""
try:
    # code...
except Exception as e:
    st.write(f"**Error:** {e}")
    return None
""")

# Image Processing
st.subheader("3. Image Processing:")
st.code("""
image = Image.open(BytesIO(response.content))
""")

# Return
st.subheader("4. Return:")
st.code("""
return image
""")

# Exception Handling
st.subheader("5. Exception Handling:")
st.code("""
except Exception as e:
    st.write(f"**Error:** {e}")
    return None
""")

# Dependencies
st.subheader("Dependencies:")
st.code("""
pip install requests Pillow
""")


# Section 8: Listening to Your Voice
st.header("8. Listening to Your Voice")

st.write("We're adding a cool function to recognize what you say through the microphone. It's like having a virtual assistant that understands your voice commands.")
# Streamlit Presentation
# Speech Recognition Setup
st.subheader("1. Speech Recognition Setup:")
st.code("""
recognizer = sr.Recognizer()
""")

# Audio Capture
st.subheader("2. Audio Capture:")
st.code("""
with sr.Microphone() as source:
    st.markdown("⁺₊ Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
""")

# Processing Simulation
st.subheader("3. Processing Simulation:")
st.code("""
with st.spinner("Processing..."):
    time.sleep(1)
""")

# Text Recognition
st.subheader("4. Text Recognition:")
st.code("""
try:
    text = recognizer.recognize_google(audio)
    st.code(f"Your Question: {text}")
    return text
""")

# Unknown Value Error Handling
st.subheader("5. Unknown Value Error Handling:")
st.code("""
except sr.UnknownValueError:
    st.warning("Sorry, I could not understand audio.")
    audio = recognizer.listen(source)
    st.markdown("I'm still listening....")
    return ""
""")

# Request Error Handling
st.subheader("6. Request Error Handling:")
st.code("""
except sr.RequestError as e:
    st.error(f"Could not request results from Google Web Speech API; {e}")
    return ""
""")

# Section 9: The Main Show
st.header("9. The Main Show")

st.write("This is where the magic happens! Our main function sets up the chat history, creates the user interface, and handles user input, especially when there's an image involved.")
# Main Function - Health Mate Application
# Initializing Chat History
st.write("The application initializes the chat history in the Streamlit session state.")
st.code("if 'chat_history' not in st.session_state:\n    st.session_state.chat_history = []")

# Streamlit UI Components
st.write("The main user interface components are set up.")
st.code("st.title('Health Mate')\nst.subheader('Your Personal Wellness Companion.')")

# Image Upload Section
st.write("Users can upload an image for analysis.")
st.code("# Image upload section\nwith st.expander('Upload Image'):\n    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])\n    if uploaded_file is not None:\n        # Display the uploaded image\n        image = Image.open(uploaded_file)\n        st.image(image, caption='Uploaded Image', use_column_width=True)")

# Enable Speech Input Button
st.write("A button is provided to enable speech input.")
st.code("if st.button('Enable Speech Input', key='speech_input_button'):\n    user_question = st.chat_input('Ask your question:')\n    user_question = recognize_speech()\n    if user_question is not None:\n        st.write('Your Question:', user_question)\nelse:\n    user_question = st.chat_input('Ask your question:')\n    if user_question is not None:\n        st.write('Your Question:', user_question)")

# Processing User Input
st.write("User input is processed based on the presence of an uploaded image.")
st.code("if image is None and user_question:\n    # Process text-based queries without an image\n    # ...")
st.code("elif image is not None and user_question:\n    # Process queries with both image and text input\n    # ...")

# Speech Recognition Function
st.write("Function for recognizing speech input is defined.")
st.code("# Speech recognition function\ndef recognize_speech():\n    # ...")

# Processing User Input with Image Analysis

# Case: No Image, User Question Present
st.header("Case: No Image, User Question Present")
st.write("When you ask a question without uploading an image, Health Mate uses the **Gemini-pro** generative model to provide a response. The answer is shown on the screen, and the conversation is saved in the chat history. Additionally, responds both in audio and text, and all interactions are stored in a file named 'chat_history.json'.")

st.code("""
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)
chat = model.start_chat(history=[])
response = chat.send_message(f\"\"\"Act as my fitness expert and diet nutritionist, responding with short, friendly, and easily understandable answers. Kindly answer me this {user_question}\"\"\", stream=True)
response.resolve()
st.markdown(response.text)

# Save interaction in chat history
file_path = "chat_history.json"
try:
    with open(file_path, "r") as file:
        chat_history = json.load(file)
except FileNotFoundError:
    chat_history = []

audio = elevenlabs.generate(text=response.text, voice="Matilda")
elevenlabs.play(audio)

st.session_state.chat_history.append({"user": user_question, "response": chat.history[1].parts[0]})
with open(file_path, "w") as file:
    json.dump(chat_history, file, indent=2)
""")

# Case: Image and User Question Present
st.header("Case: Image and User Question Present")
st.write("When the user provides both an image and a question, the application uses a specialized **Gemini-pro-vision** generative model for image analysis. The model interprets the image content, generates a response, and displays it. The interaction is recorded in the chat history.Additionally, responds both in audio and text, and all interactions are stored in a file named 'chat_history.json'")

st.code("""
model = genai.GenerativeModel("gemini-pro-vision")
chat = model.start_chat(history=[])
response = chat.send_message([f\"\"\"Act as my Expert nutritionist Doctor and fitness expert. {user_question}\"\"\", image], stream=True)
response.resolve()
st.markdown(response.text)

# Save interaction in chat history
file_path = "chat_history.json"
try:
    with open(file_path, "r") as file:
        chat_history = json.load(file)
except FileNotFoundError:
    chat_history = []

audio = elevenlabs.generate(text=response.text, voice="Matilda")
elevenlabs.play(audio)

st.session_state.chat_history.append({"user": user_question, "response": chat.history[1].parts[0]})
with open(file_path, "w") as file:
    json.dump(chat_history, file, indent=2)
""")

# Section 10: Let's Roll!
st.header("10. Let's Roll!")
st.write("Finally, this line makes sure that our main function runs when we start the app. It's like saying, 'Let the show begin!'")
st.code("""
if __name__ == "__main__":
   main()
""")


st.write("This documentation covered key aspects of the HealthMate Wellness Companion. Feel free to explore and customize the app according to your needs.")


# 9. Employ sidebar for additional information or navigation
st.sidebar.header("About HealthMate")
st.sidebar.markdown("HealthMate is a AI-powered wellness companion designed to support your health journey.")
st.sidebar.markdown("**Key Features:**")
st.sidebar.markdown("* Engaging conversations")
st.sidebar.markdown("* Personalized health insights")
st.sidebar.markdown("* Image and voice recognition")
