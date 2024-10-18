from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Teacher(db.Model):
    teacher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    research_projects = db.Column(db.Text, nullable=True)
    patents = db.Column(db.Text, nullable=True)
    academic_background = db.Column(db.Text, nullable=True)

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_type = db.Column(db.String(10), nullable=False)  # 'theory' or 'lab'
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'))

class StudentCourseSelection(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), primary_key=True)
    semester = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'))
    feedback = db.Column(db.Text)
