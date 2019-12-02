from flask import Flask, render_template, url_for
from register import Register, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'shhhh'

@app.route("/")
@app.route("/homepage/")
def homepage():
    return render_template('homepage.html')

@app.route("/beer/")
def beer():
    return render_template('beer.html')

@app.route("/cider/")
def cider():
    return "Cider"

@app.route("/whiskey/")
def whiskey():
    return "Whiskey"

@app.route("/rum/")
def rum():
    return"Rum"

@app.route("/gin/")
def gin():
    return "Gin"

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = Register()
    return render_template('signup.html', title='Sign Up', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
