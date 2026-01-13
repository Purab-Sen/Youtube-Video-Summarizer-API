from chain import get_answer_of_question
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health-check", methods=['GET'])
def hello():
    return jsonify({"message":"server is running"})

@app.route("/search", methods=['GET'])
def search():
    video_id = request.args.get("video_id")
    question = request.args.get("question")

    try:
        answer = get_answer_of_question(video_id, question)
        return jsonify({"answer": answer}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
