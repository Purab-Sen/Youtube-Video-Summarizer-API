from chain import get_answer_of_question
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/hello", methods=['GET'])
def hello():
    return jsonify({"message":"Hi chanchal"})

@app.route('/search', methods=['GET'])
def search():
    video_id = request.args.get("video_id")
    question = request.args.get("question")
    answer = get_answer_of_question(video_id,question)
    return jsonify({"message": answer})

if __name__ == '__main__':
    app.run(debug=True)
