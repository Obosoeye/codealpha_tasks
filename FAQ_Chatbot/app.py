# ================================================================
# CodeAlpha Internship - Task 2: FAQ Chatbot
# Name: Obosoeye Anthony Peters
# Description: NLP-powered chatbot that matches user questions
#              to the most similar FAQ and returns the answer
# ================================================================

import streamlit as st
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from faqs import FAQ_DATA

# --- Download NLTK data silently ---
nltk.download('punkt',     quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

# --- Page Setup ---
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --- Text Preprocessing Function ---
def preprocess(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]
    # Join back to string
    return ' '.join(tokens)

# --- Prepare FAQ Data ---
faq_questions = [item['question'] for item in FAQ_DATA]
faq_answers   = [item['answer']   for item in FAQ_DATA]
processed_faqs = [preprocess(q)   for q in faq_questions]

# --- Find Best Matching FAQ ---
def find_best_match(user_question, threshold=0.1):
    processed_input = preprocess(user_question)

    vectorizer = TfidfVectorizer()
    all_texts  = processed_faqs + [processed_input]
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    user_vector  = tfidf_matrix[-1]
    faq_vectors  = tfidf_matrix[:-1]
    similarities = cosine_similarity(user_vector, faq_vectors)[0]

    best_idx   = np.argmax(similarities)
    best_score = similarities[best_idx]

    if best_score < threshold:
        return None, 0.0

    return FAQ_DATA[best_idx]['answer'], float(best_score)

# --- App Title ---
st.title("🤖 AI FAQ Chatbot")
st.markdown("### Ask me anything about Artificial Intelligence!")
st.markdown("---")

# --- Initialize Chat History ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        'role': 'assistant',
        'content': '👋 Hello! I am an AI FAQ Chatbot built by Obosoeye Anthony Peters. Ask me anything about Artificial Intelligence, Python, or Machine Learning!'
    })

# --- Display Chat History ---
for message in st.session_state.messages:
    if message['role'] == 'user':
        with st.chat_message('user'):
            st.write(message['content'])
    else:
        with st.chat_message('assistant'):
            st.write(message['content'])

# --- User Input ---
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message
    st.session_state.messages.append({
        'role': 'user',
        'content': user_input
    })

    # Find best answer
    answer, score = find_best_match(user_input)

    if answer:
        if score < 0.3:
            response = answer + "\n\n_(Low confidence — try rephrasing your question)_"
        else:
            response = answer
    else:
        response = "I am sorry, I could not find a matching answer. Try asking about AI, machine learning, Python, or chatbots!"

    # Add assistant response
    st.session_state.messages.append({
        'role': 'assistant',
        'content': response
    })

    st.rerun()

# --- Sidebar ---
with st.sidebar:
    st.markdown("### 📚 Topics I can answer:")
    st.markdown("- Artificial Intelligence")
    st.markdown("- Machine Learning")
    st.markdown("- Deep Learning")
    st.markdown("- Python Programming")
    st.markdown("- Natural Language Processing")
    st.markdown("- Computer Vision")
    st.markdown("- GitHub & Tools")
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.caption("CodeAlpha AI Internship | Obosoeye Anthony Peters")

# --- Footer ---
st.markdown("---")
st.caption("Built with Python, Streamlit & NLTK | CodeAlpha AI Internship | Obosoeye Anthony Peters")