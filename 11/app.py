from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Student, Teacher, Course, StudentCourseSelection

app = Flask(__name__)
app.secret_key = 'somesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_student = Student(name=name, email=email, password=password)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        student = Student.query.filter_by(email=email, password=password).first()
        if student:
            session['student_id'] = student.student_id
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'student_id' not in session:
        return redirect(url_for('login'))
    student_id = session['student_id']
    courses = Course.query.all()
    return render_template('dashboard.html', courses=courses)

@app.route('/select_course', methods=['POST'])
def select_course():
    student_id = session['student_id']
    course_id = request.form['course_id']
    teacher_id = request.form['teacher_id']
    semester = request.form['semester']
    new_selection = StudentCourseSelection(student_id=student_id, course_id=course_id, teacher_id=teacher_id, semester=semester)
    db.session.add(new_selection)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
