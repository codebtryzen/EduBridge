from flask import Flask, request, jsonify
from database import save_user_score, get_user_scores

app = Flask(__name__)

@app.route("/save-score", methods=["POST"])
def save_score():
    data = request.json
    username = data["username"]
    score = data["score"]
    save_user_score(username, score)
    return jsonify({"message": "Score saved!"})

@app.route("/get-scores/<username>", methods=["GET"])
def get_scores(username):
    scores = get_user_scores(username)
    return jsonify(scores)

if __name__ == "__main__":
    app.run(debug=True)
