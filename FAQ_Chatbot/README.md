# 🤖 FAQ Chatbot

## Project Description
An NLP-powered FAQ Chatbot built with Python and Streamlit.
It uses cosine similarity and TF-IDF to match user questions
to the most similar FAQ and return the best answer.

## Features
- Natural Language Processing using NLTK
- TF-IDF vectorization for text matching
- Cosine similarity for finding best answers
- 20 FAQ entries covering AI and Machine Learning topics
- Clean chat interface built with Streamlit
- Clear chat button
- Sidebar showing available topics

## Technologies Used
- Python 3.x
- Streamlit
- NLTK
- scikit-learn
- NumPy

## How to Run
1. Install requirements:
   pip install -r requirements.txt
2. Download NLTK data:
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
3. Run the app:
   streamlit run app.py
4. Open browser at:
   http://localhost:8501

## Author
Obosoeye Anthony Peters — CodeAlpha AI Internship
```

Press **Ctrl+S** to save.

Then in the terminal:
```
git add .
```
```
git commit -m "Update README with project details"
```
```
git push