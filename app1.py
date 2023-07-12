from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-similarity', methods=['POST'])
def calculate_similarity():
    data = request.json
    text1 = data['text1']
    text2 = data['text2']
    similarity_score = find_similarity(text1, text2)
    response = {'similarity score': similarity_score}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
