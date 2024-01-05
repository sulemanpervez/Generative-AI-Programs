import streamlit as st
st.title("Chat History")
chat_history = st.session_state.chat_history
for item_data in chat_history:
    st.write(item_data)