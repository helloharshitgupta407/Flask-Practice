from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    userlogin=True
    return render_template('basic2login.html',userlogin=userlogin)
if __name__ == '__main__':
    app.run(debug=True)
