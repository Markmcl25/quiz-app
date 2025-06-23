from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load questions
with open('questions.json') as f:
    questions = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        selected = request.form.get(f'q{i}')
        if selected == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
