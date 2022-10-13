#Imports flask and other useful things

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/tribes')
def tribes():
    return render_template('tribes.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form')
def login():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#Setting basic queries

#tribe = tribe.query.filter_by(location="").order_by(tribe.name).all()
