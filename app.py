from flask import Flask, render_template, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__ , static_folder="static/")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


quiz_categories = ['General Knowledge', 'Science', 'History', 'Geography', 'Sports']

# questions_data = {
#     'General Knowledge': [
#         {
#             'question_text': 'What is the capital of France?',
#             'options': ['Paris', 'London', 'Berlin', 'Madrid'],
#             'answer': 'Paris',
#         },
#         {
#             'question_text': 'Who wrote "Romeo and Juliet"?',
#             'options': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Mark Twain'],
#             'answer': 'William Shakespeare',
#         },
#         {
#             'question_text': 'What is the largest mammal?',
#             'options': ['Blue Whale', 'Elephant', 'Giraffe', 'Hippopotamus'],
#             'answer': 'Blue Whale',
#         },
#         {
#             'question_text': 'What is the currency of Japan?',
#             'options': ['Japanese Yen', 'Chinese Yuan', 'Euro', 'US Dollar'],
#             'answer': 'Japanese Yen',
#         },
#         {
#             'question_text': 'Who painted the Mona Lisa?',
#             'options': ['Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet'],
#             'answer': 'Leonardo da Vinci',
#         },
#     ],
#     'Science': [
#         {
#             'question_text': 'What is the chemical symbol for gold?',
#             'options': ['Au', 'Ag', 'Fe', 'Cu'],
#             'answer': 'Au',
#         },
#         {
#             'question_text': 'Which planet is known as the Red Planet?',
#             'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
#             'answer': 'Mars',
#         },
#         {
#             'question_text': 'What is the powerhouse of the cell?',
#             'options': ['Mitochondria', 'Nucleus', 'Ribosome', 'Endoplasmic Reticulum'],
#             'answer': 'Mitochondria',
#         },
#         {
#             'question_text': 'What is the speed of light?',
#             'options': ['299,792 kilometers per second', '150,000 kilometers per second', '450,000 kilometers per second', '600,000 kilometers per second'],
#             'answer': '299,792 kilometers per second',
#         },
#         {
#             'question_text': 'Who developed the theory of relativity?',
#             'options': ['Albert Einstein', 'Isaac Newton', 'Galileo Galilei', 'Stephen Hawking'],
#             'answer': 'Albert Einstein',
#         },
#     ],
#     'History': [
#         {
#             'question_text': 'In which year did World War II end?',
#             'options': ['1945', '1918', '1939', '1955'],
#             'answer': '1945',
#         },
#         {
#             'question_text': 'Who was the first President of the United States?',
#             'options': ['George Washington', 'Thomas Jefferson', 'John Adams', 'James Madison'],
#             'answer': 'George Washington',
#         },
#         {
#             'question_text': 'What ancient civilization built the pyramids?',
#             'options': ['Ancient Egyptians', 'Ancient Greeks', 'Mayans', 'Romans'],
#             'answer': 'Ancient Egyptians',
#         },
#         {
#             'question_text': 'Who is known as the "Father of Computer Science"?',
#             'options': ['Alan Turing', 'Bill Gates', 'Steve Jobs', 'Ada Lovelace'],
#             'answer': 'Alan Turing',
#         },
#         {
#             'question_text': 'When was the Declaration of Independence signed?',
#             'options': ['1776', '1789', '1800', '1825'],
#             'answer': '1776',
#         },
#     ],
#     'Geography': [
#         {
#             'question_text': 'Which river is the longest in the world?',
#             'options': ['Nile', 'Amazon', 'Yangtze', 'Mississippi'],
#             'answer': 'Nile',
#         },
#         {
#             'question_text': 'What is the capital of Australia?',
#             'options': ['Canberra', 'Sydney', 'Melbourne', 'Brisbane'],
#             'answer': 'Canberra',
#         },
#         {
#             'question_text': 'In which continent is the Sahara Desert located?',
#             'options': ['Africa', 'Asia', 'North America', 'South America'],
#             'answer': 'Africa',
#         },
#         {
#             'question_text': 'What is the highest mountain in the world?',
#             'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
#             'answer': 'Mount Everest',
#         },
#         {
#             'question_text': 'Which country is known as the "Land of the Rising Sun"?',
#             'options': ['Japan', 'China', 'South Korea', 'Vietnam'],
#             'answer': 'Japan',
#         },
#     ],
#     'Sports': [
#         {
#             'question_text': 'In which sport is the Davis Cup awarded?',
#             'options': ['Tennis', 'Golf', 'Cricket', 'Football'],
#             'answer': 'Tennis',
#         },
#         {
#             'question_text': 'Who is the all-time leading scorer in NBA history?',
#             'options': ['Kareem Abdul-Jabbar', 'LeBron James', 'Kobe Bryant', 'Michael Jordan'],
#             'answer': 'Kareem Abdul-Jabbar',
#         },
#         {
#             'question_text': 'What is the diameter of a standard basketball hoop in inches?',
#             'options': ['18 inches', '20 inches', '22 inches', '24 inches'],
#             'answer': '18 inches',
#         },
#         {
#             'question_text': 'Which country won the FIFA World Cup in 2018?',
#             'options': ['France', 'Croatia', 'Brazil', 'Germany'],
#             'answer': 'France',
#         },
#         {
#             'question_text': 'Who holds the record for the most Olympic gold medals?',
#             'options': ['Michael Phelps', 'Usain Bolt', 'Simone Biles', 'Serena Williams'],
#             'answer': 'Michael Phelps',
#         },
#     ],
# }

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    option_text = db.Column(db.String(255), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_question.id'))
  
class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    category_name_db = db.Column(db.String(255), nullable=False)
    options = db.relationship('Option', backref='question', lazy=True)

with app.app_context():
    db.create_all()

# def add_question(category_name, question_text, options, answer):
#     existing_question = QuizQuestion.query.filter_by(
#         category_name_db=category_name, question_text=question_text).first()

#     if not existing_question:
#         question = QuizQuestion(question_text=question_text, answer=answer, category_name_db=category_name)
#         db.session.add(question)
#         db.session.commit()

#         for option_text in options:
#             option = Option(option_text=option_text, question=question)
#             db.session.add(option)
#             db.session.commit()

# with app.app_context():
#      for category_name, question_list in questions_data.items():
#         for question_data in question_list:
#             add_question(category_name, question_data['question_text'], question_data['options'], question_data['answer'])



@app.route('/', methods=['GET'])
def quiz_home():
    return render_template('starting_page.html', categories=quiz_categories)


@app.route('/start_quiz', methods=['GET', 'POST'])
def main_quiz():
    if request.method == 'POST':
        data = request.form.get('button_value')
        questions = (
            QuizQuestion.query
            .filter_by(category_name_db=data)
            .options(db.joinedload(QuizQuestion.options))
            .all()
        )

        return render_template('index.html',header_data = data, question_list_start=questions)
    
@app.route('/expired')
def expired():
    return render_template('expired.html')

@app.route('/starting', methods=['GET'])
def starting():
    return render_template('starting_page.html', categories=quiz_categories)

@app.route('/submit_quiz', methods=['POST', 'GET'])
def submit_quiz():
    user_answers = {}
    for key, value in request.form.items():
        
        if key.startswith('question_'):
            question_id = key.split('_')[1]
            user_answers[question_id] = value

    correct_answers = {}
    for question in QuizQuestion.query.options(db.joinedload(QuizQuestion.options)).all():
        correct_answers[question.id] = question.answer

    user_answers = {int(k): v for k, v in user_answers.items()}


    score = sum([1 for q_id, user_ans in user_answers.items() if user_ans == correct_answers.get(q_id)])
    
    return render_template('result.html', score=score, total_questions=len(correct_answers))
    
# @app.route('/testing_sql')
# def display():
#     questions = (
#             QuizQuestion.query
#             .options(db.joinedload(QuizQuestion.options))
#             .all()
#         )
#     return render_template('display.html', question_data = questions)



if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, port=3000)