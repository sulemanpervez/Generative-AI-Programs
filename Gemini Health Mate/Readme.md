# HealthMate Wellness Companion Documentation

## Introduction
# HealthMate Wellness Companion
Welcome to the documentation for Gemini HealthMate, your personal wellness companion. This guide covers the various components and functionalities of the HealthMate application.

## 1. Importing Necessary Tools
In this section, we import the required tools and libraries for the HealthMate Wellness Companion.

```python
import requests
from PIL import Image
from io import BytesIO
import speech_recognition as sr
import streamlit as st
import google.generativeai as genai
import elevenlabs
import json
```

## 2. Setting up the Look and Feel
This section focuses on configuring the appearance of the HealthMate app.

```python
st.set_page_config(
    page_title="Health Mate",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

## 3. Keys to the Kingdom
Here, we ensure the app has the right access by using API keys.

```python
genai.configure(api_key="Gemini_API")
elevenlabs.set_api_key("Elevenslab_API")
```

## 4. Talking with Style
This part gives the app a unique voice using Eleven Labs.

```python
voice = elevenlabs.Voice(
    voice_id="XrExE9yKIg1WjnnlVkGX",
    settings=elevenlabs.VoiceSettings(
        stability=0,
        similarity_boost=0.85
    ),
)
```

## 5. Adding Some AI Magic
Here, we're setting up the rules for our Gemini generative AI. It's like telling it how creative or straightforward it should be when responding to users.

```python
generation_config = {
   "temperature": 0.9,
   "top_p": 1,
   "top_k": 1,
   "max_output_tokens": 2048,
}
```

## 6. Keeping It Safe
Safety first! We're setting guidelines for our Gemini AI to make sure it doesn't say anything inappropriate. It's like having a moderator to keep conversations respectful. Its optional because the model is predefined these safety_settings.

```python
safety_settings = [
   {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
   {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
   {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
   {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
```

## 7. Showing Off Images
We're creating a feature to show images. It's like opening a photo album to share pictures with users.

### 1. User-Agent Setup:
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
```

### 2. Error Handling:
```python
try:
    # code...
except Exception as e:
    st.write(f"**Error:** {e}")
    return None
```

### 3. Image Processing:
```python
image = Image.open(BytesIO(response.content))
```

### 4. Return:
```python
return image
```

### 5. Exception Handling:
```python
except Exception as e:
    st.write(f"**Error:** {e}")
    return None
```

### Dependencies:
```python
pip install requests Pillow
```

## 8. Listening to Your Voice
We're adding a cool function to recognize what you say through the microphone. It's like having a virtual assistant that understands your voice commands.

### 1. Speech Recognition Setup:
```python
recognizer = sr.Recognizer()
```

### 2. Audio Capture:
```python
with sr.Microphone() as source:
    st.markdown("⁺₊ Listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
```

### 3. Processing Simulation:
```python
with st.spinner("Processing..."):
    time.sleep(1)
```

### 4. Text Recognition:
```python
try:
    text = recognizer.recognize_google(audio)
    st.code(f"Your Question: {text}")
    return text
```

### 5. Unknown Value Error Handling:
```python
except sr.UnknownValueError:
    st.warning("Sorry, I could not understand audio.")
    audio = recognizer.listen(source)
    st.markdown("I'm still listening....")
    return ""
```

### 6. Request Error Handling:
```python
except sr.RequestError as e:
    st.error(f"Could not request results from Google Web Speech API; {e}")
    return ""
```

## 9. The Main Show
This is where the magic happens! Our main function sets up the chat history, creates the user interface, and handles user input, especially when there's an image involved.

```python
# Main Function - Health Mate Application
# Initializing Chat History
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI Components
st.title('Health Mate')
st.subheader('Your Personal Wellness Companion.')

# Image Upload Section
with st.expander('Upload Image'):
    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

# Enable Speech Input Button
if st.button('Enable Speech Input', key='speech_input_button'):
    user_question = st.chat_input('Ask your question:')
    user_question = recognize_speech()
    if user_question is not None:
        st.write('Your Question:', user_question)
else:
    user_question = st.chat_input('Ask your question:')
    if user_question is not None:
        st.write('Your Question:', user_question)

# Processing User Input
if image is None and user_question:
    # Process text-based queries without an image
    # ...

elif image is not None and user_question:
    # Process queries with both image and text input
    # ...

# Speech Recognition Function
def recognize_speech():
    # ...

# Processing User Input with Image Analysis

# Case: No Image, User Question Present
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)
chat = model.start_chat(history=[])
response = chat.send_message(f"""Act as my fitness expert and diet nutritionist, responding with short, friendly, and easily understandable answers. Kindly answer me this {user_question}""", stream=True)
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

# Case: Image and User Question Present
model = genai.GenerativeModel("gemini-pro-vision")
chat = model.start_chat(history=[])
response = chat.send_message([f"""Act as my Expert nutritionist Doctor and fitness expert. If I provide an image of my nutrition, describe its components, benefits, and potential drawbacks, responding with short, friendly, and easily understandable. If I share an exercise routine image map, guide me on the correct way to perform each exercise, along with pros and cons of the routine. {user_question}""", image], stream=True)
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

## 10. Let's Roll!
Finally, this line makes sure that our main function runs when we start the app. It's like saying, 'Let the show begin!'

```
if __name__ == "__main__":
   main()
```

This documentation covered key aspects of the HealthMate Wellness Companion. Feel free to explore and customize the app according to your needs.

## About HealthMate
**HealthMate** is an AI-powered wellness companion designed to support your health journey.

**Key Features:**
- Engaging conversations
- Personalized health insights
- Image and voice recognition