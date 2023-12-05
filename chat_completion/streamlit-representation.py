from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv, find_dotenv
import os

_: bool = load_dotenv(find_dotenv())
client: OpenAI = OpenAI()

import streamlit as st
from openai.types.chat.chat_completion import ChatCompletion

# Function to interact with OpenAI GPT-3
def chat_completion(prompt: str, max_tokens: int = 300) -> str:
    response: ChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo-1106",
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

def main():
    st.title("Interactive Chatbot with OpenAI GPT-3.5-turbo")

    # List of use cases
    use_cases_list = [
        "Code generation",
        "Language Translation",
        "Storytelling",
        "Interview practice",
        "Recipe Ideas"
    ]

    # Display use case choices
    user_choice = st.selectbox("Choose a use case:", use_cases_list)

    # Map the selected use case to an index
    user_choice_index = use_cases_list.index(user_choice) + 1

    # Display prompt customization options
    prompt_choice = st.radio("Would you like to provide additional details for improved chatbot performance?", ("Yes", "No"))

    if prompt_choice == "Yes":
        if user_choice_index == 1:
            target_programming_lan = st.text_input("Enter the target programming language:")
            program_name = st.text_input("Specify the program you want to code:")
            additional_choice = st.radio("Do you want to add more context?", ("Yes", "No"))
            context = f" that {st.text_input('Specify more details:')}" if additional_choice == 'Yes' else ''
            user_input = f"Generate a {target_programming_lan} code snippet for a {program_name}{context}"
        elif user_choice_index == 2:
            target_language = st.text_input("Enter your target language:")
            sentence_choice = st.radio("Do you have a sentence to translate?", ("Yes", "No"))
            sentence = st.text_input("Enter the sentence in English:") if sentence_choice == 'Yes' else ''
            user_input = f"Translate the following sentence into {target_language}: {sentence}"
        elif user_choice_index == 3:
            target_story = st.text_input("Enter the name of the story:")
            plot_choice = st.radio("Do you want to provide additional plot details?", ("Yes", "No"))
            plot_details = f" where {st.text_input('Enter plot details:')}" if plot_choice == 'Yes' else ''
            user_input = f"Create a captivating story involving {target_story}{plot_details}."
        elif user_choice_index == 4:
            target_interview = st.text_input("Enter the target interview position:")
            topics_choice = st.radio("Do you have specific interview topics?", ("Yes", "No"))
            interview_topics = f" related to {st.text_input('Enter interview topics:')}" if topics_choice == 'Yes' else ''
            user_input = f"Conduct a simulated interview for a {target_interview} position {interview_topics}."
        elif user_choice_index == 5:
            target_dish = st.text_input("Enter the target dish:")
            ingredients_choice = st.radio("Do you have a list of ingredients?", ("Yes", "No"))
            ingredients_list = f" that includes {st.text_input('Enter ingredients:')}" if ingredients_choice == 'Yes' else ''
            user_input = f"Suggest a unique and flavorful recipe for {target_dish}{ingredients_list}."
    else:
        user_input = f"Help me with a {use_cases_list[user_choice_index - 1].lower()}."

    # Display user input
    st.write("User Input:", user_input)

    # Get chatbot response
    response = chat_completion(user_input)
    st.write("Chatbot Response:", response)

if __name__ == "__main__":
    main()
