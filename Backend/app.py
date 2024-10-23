from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

quizzes = []
flashcards = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/quizzes', methods=['GET'])
def get_quizzes():
    return jsonify(quizzes)

@app.route('/api/quizzes', methods=['POST'])
def create_quiz():
    new_quiz = request.json
    quizzes.append(new_quiz)
    return jsonify(new_quiz), 201

@app.route('/api/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify(flashcards)

@app.route('/api/flashcards', methods=['POST'])
def create_flashcard():
    new_flashcard = request.json
    flashcards.append(new_flashcard)
    return jsonify(new_flashcard), 201

@app.route('/quizzes')
def quizzes_page():
    return render_template('quizzes.html')

@app.route('/flashcards')
def flashcards_page():
    return render_template('flashcards.html')

if __name__ == '__main__':
    app.run(debug=True)
