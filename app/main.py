from flask import Flask, jsonify

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Learn DevOps", "done": False},
    {"id": 2, "task": "Build CI/CD Pipeline", "done": False}
]

@app.route("/")
def home():
    return "Welcome to the To-Do API For Assignment 2"

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
