from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from uuid import uuid4
import config

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Lesson(db.Model):
    __tablename__ = 'lessons'
    id = db.Column(db.Integer, primary_key=True)
    school_date = db.Column(db.String(80))
    subject = db.Column(db.String(80))
    topic = db.Column(db.Text)
    homework = db.Column(db.Text)

    def __init__(self, school_date, subject, topic, homework):
        self.school_date = school_date
        self.subject = subject
        self.topic = topic
        self.homework = homework

    def __repr__(self):
        return f"Lesson({self.subject})"

@app.route('/')
def index():
    lessons = Lesson.query.filter(Lesson.topic.isnot(None) | Lesson.homework.isnot(None)).order_by(Lesson.school_date.desc()).all()
    return render_template('index.html', lessons=lessons)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=1234)
