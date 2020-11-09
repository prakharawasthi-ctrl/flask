from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)
# 'mysql://root:@localhost/codin'

class Contacts(db.Model):
    '''
    sno,phone_num,name,email,msg,date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=True ,default=datetime.utcnow())
    email = db.Column(db.String(20), nullable=False)


@app.route("https://myschool-avm.herokuapp.com/")
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/post")
def post():
    return render_template('post.html')


@app.route("https://hello-mom.herokuapp.com/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''ADD ENTRY TO THE DATABASE'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, email=email, phone_num=phone, msg=message),
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


app.run(debug=True)
