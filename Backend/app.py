from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for quizzes
quizzes = {
    'maths': ["What is 2 + 2?", "What is the square root of 16?"],
    'physics': ["What is the formula for force?", "What is Newton's second law?"],
    'biology': ["What is the powerhouse of the cell?", "What is DNA?"],
    'chemistry': ["What is the chemical formula for water?", "What is pH?"]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quizzes')
def quizzes_page():
    subject = request.args.get('subject')
    questions = quizzes.get(subject, [])
    return render_template('quizzes.html', subject=subject, questions=questions)

@app.route('/flashcards')
def flashcards_page():
    subject = request.args.get('subject')
    # You can replace this with actual flashcard data
    return render_template('flashcards.html', subject=subject)

if __name__ == '__main__':
    app.run(debug=True)
