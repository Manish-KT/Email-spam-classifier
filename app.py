import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Load the model
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# Create the UI
st.title('Email Spam Classifier')

# Get user input
email = st.text_input('Enter the email text')

# 1. preprocess the data

def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # remove punctuation
    text = [word for word in text if word.isalnum()]

    # keep alpha numeric words
    text = [word for word in text if word.isalpha()]

    # remove stop words
    text = [word for word in text if word not in nltk.corpus.stopwords.words('english')]

    return " ".join(text)

transformed_email = text_transform(email)


# 2. vectorize the data
vector_input = tfidf.transform([transformed_email])

# 3. predict the result
result = model.predict(vector_input)

# 4. display the result
if st.button('Predict'):
    if result[0] == 1:
        st.write('Spam')
    else:
        st.write('Not Spam')

