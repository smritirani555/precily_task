from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/api/similarity', methods=['POST'])
def get_similarity():
    data = request.get_json()
    text1 = data['text1']
    text2 = data['text2']
    similarity_score = find_similarity(text1, text2)
    response = {'similarity score': similarity_score}
    return jsonify(response)

def find_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_score = cosine_similarity(tfidf_matrix)[0][1]
    return similarity_score

if __name__ == '__main__':
    app.run()
