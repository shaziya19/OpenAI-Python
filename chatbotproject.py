from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()
initial_message = [
        {"role": "system", "content": "You are a trip planner in Dubai. You should be expert to help user to plan the trip effectively. You will provide a seamless travel experience with personalized itineraries, real-time flight and accommodation bookings, and AI-curated recommendations for local attractions and dining. It will include multilingual chat for easy communication, travel tips and safety alerts, smart packing lists, and an expense tracker for budget management and making it the ultimate all-in-one travel companion. You should be more interactive and ask questions professionally and help user to plan their trip easy. Don't exceed more than 200 words."},
        {
            "role": "assistant",
            "content": "Hello, I am Travello, Your trip planner. How can i help you?"
        }
]

def get_response_from_llm(messages):
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=messages
    )
    return completion.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = initial_message
st.title("Travello: Explore the World with AI")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
user_message = st.chat_input("Enter Your Message")
if user_message:
    new_message = {
            "role": "user",
            "content": user_message
        }
    st.session_state.messages.append (new_message)
    with st.chat_message(new_message["role"]):
            st.markdown(new_message["content"])
    response = get_response_from_llm (st.session_state.messages)
    if response:
         response_message = {
            "role": "assistant",
            "content": response
         }
    st.session_state.messages.append (response_message)
    with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])
