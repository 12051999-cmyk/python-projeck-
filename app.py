from flask import Flask,escape,request,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wahyu355@localhost/bem'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Berita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(80))
    isi = db.Column(db.String(80))
    status = db.Column(db.Integer)

@app.route('/')
def index():
     
    date = Berita.query.all()

    return render_template("index.html",date=date)


@app.route('/index/save', methods=['POST'])
def indexsave():

    judul = request.form['user']
    isi = request.form['pasword']
    status = 1

    date = Berita(
        judul = judul,
        isi = isi,
        status = status,
    )

    db.session.add(date)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/index/delete/<id>',methods=['GET'])
def indexdelete(id):

    date = Berita.query.filter_by(id=id).first()

    db.session.delete(date)
    db.session.commit()

    return redirect(url_for('index'))

app.run(debug=True)