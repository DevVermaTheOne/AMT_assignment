import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('punkt_tab')


driver = webdriver.Chrome()
url = 'https://animemangatoon.com/castle-swimmer-unveiling-new-prophecy/'
driver.get(url)
html = BeautifulSoup(driver.page_source, "html.parser")

result = html.find_all(class_="content-inner")
description = ""
for item in result:
    next_line = item.text
    description = description + next_line

sentences = sent_tokenize(description)


# function to get the final response based on similarity
def get_response(user_input):
    vectorizer = TfidfVectorizer().fit_transform(sentences + [user_input])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors[-1:], vectors[:-1])

    # Get the most similar sentence
    idx = cosine_sim.argsort()[0][-1]
    return sentences[idx]


# implementation of basic chat system
def chat():
    print("Welcome to the Castle Swimmer Chatbot! Type 'exit' to leave.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


chat()
