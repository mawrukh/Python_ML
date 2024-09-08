import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer
import torch

# Load the pretrained BART model and tokenizer
@st.cache_resource
def load_model():
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    return model, tokenizer

model, tokenizer = load_model()

st.title("BART Model Text Summarizer")

# Text input for summarization
text = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if text:
        # Encode the input text
        inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
        
        # Generate the summary
        summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # Display the summary
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
