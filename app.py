from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/conUs')
def conUs():
    return render_template('contactUs.html')

@app.route('/faq')
def faq():
    return render_template('FAQ.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/termsAndCon')
def TaC():
    return render_template('termsAndCon.html')

if __name__ == '__main__':
    app.run()