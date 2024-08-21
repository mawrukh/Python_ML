import json
import streamlit as st
from fuzzywuzzy import process

# Load the FAQ data from the JSON file
try:
    with open('faqs.json', 'r') as json_file:
        faqs = json.load(json_file)
except FileNotFoundError:
    st.error("Error: The JSON file 'faqs.json' was not found. Please make sure it is in the correct location.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the JSON file: {str(e)}")
    st.stop()

# Function to find the best answer based on the user's query
def find_answer(query):
    best_match, best_match_ratio = process.extractOne(query, faqs.keys())
    if best_match_ratio > 80:  # If match confidence is higher than 80%
        return faqs[best_match]
    else:
        return "Sorry, I couldn't find an answer to your question."


# Streamlit app
st.title("ComsatsGPT")
# Custom CSS to style the Q&A
st.markdown("""
    <style>
    .user-question {
        background-color: #f3e9d0;
        color: #de0a26;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .bot-answer {
        background-color: #de0a26;
        color: #f3e9d0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    .input-field {
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state to store the conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Display the conversation in a chat-like format, in reverse order
with st.container():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for entry in reversed(st.session_state.conversation):
        if "user" in entry:
            st.markdown(f"<div class='user-question'><strong>You asked:</strong> {entry['user']}</div>", unsafe_allow_html=True)
        if "bot" in entry:
            st.markdown(f"<div class='bot-answer'><strong>Response:</strong> {entry['bot']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Get user input (positioned below the conversation history)

user_query = st.text_input("Type your query:", key="user_input", placeholder="Type your question here...")

if st.button("Send"):
    if user_query:
        
        
        try:
            # Get the chatbot's answer
            answer = find_answer(user_query)
            # Store the chatbot's answer in conversation
            st.session_state.conversation.append({"bot": answer})
            # Store user query in conversation
            st.session_state.conversation.append({"user": user_query})
        except Exception as e:
            st.error(f"An error occurred while processing your query: {str(e)}")

# For debugging: Display the contents of the FAQs
# if st.checkbox("Show FAQ contents"):
#     st.write(faqs)
