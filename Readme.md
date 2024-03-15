# Email Spam Classifier

![Email Spam Classifier](https://i0.wp.com/pctechmag.com/wp-content/uploads/2018/05/spam-email.jpg?resize=780%2C470&ssl=1)


This is a simple web application built with Streamlit that allows users to input a sentence, and the app predicts whether the sentence is spam or not using a machine learning model trained on email data.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
3. Run the app by executing the following command:
4. Open your web browser and go to the provided URL (usually http://localhost:8501) to use the app.
5. Enter a sentence in the text input box, and the app will predict whether it's spam or not.
6. My app hosted on streamlit cloud: https://manish-kt-email-spam-classifier-app-5pnhlj.streamlit.app/

## Features

- User-friendly interface: The app has a simple and intuitive interface, making it easy for users to interact with.
- Real-time predictions: Users can get instant predictions on whether their input sentence is classified as spam or not.
- Downloadable model: Users have the option to download the trained machine learning model used by the app.

## Model Details

The machine learning model used in this app is a MultinomialNB classifier trained on a dataset of labeled email data. The model was trained using the TF-IDF (Term Frequency-Inverse Document Frequency) vectorization technique to convert text data into numerical features.

## Dataset

The dataset used for training the model is not included in this repository. However, you can use any labeled email dataset to train your own model. Ensure that the dataset contains two columns: 'text' (email content) and 'label' (spam or not spam).

Dataset link: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Dependencies

- Streamlit
- Scikit-learn

## Acknowledgments

This project was inspired by the need for effective spam detection mechanisms in email systems. Special thanks to the Streamlit team for creating an amazing tool for building interactive web applications with Python.

