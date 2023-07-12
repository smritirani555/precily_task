import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request

app = Flask(__name__)

def find_similarity(text1, text2):
    """
    Finds the semantic similarity between two sentences.

    Args:
        text1 (str): The first sentence.
        text2 (str): The second sentence.

    Returns:
        float: The similarity score between the two sentences.
    """

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_score = cosine_similarity(tfidf_matrix)[0][1]
    return similarity_score

@app.route("/", methods=["POST"])
def similarity():
    """
    API endpoint that returns the similarity score between two sentences.

    Args:
        request (dict): The request body.

    Returns:
        dict: The response body.
    """

    text1 = request.json["text1"]
    text2 = request.json["text2"]
    similarity_score = find_similarity(text1, text2)
    response = {
        "similarity_score": similarity_score
    }
    return response

if __name__ == "__main__":
    app.run(debug=True)
