from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    l=[1,2,3,4,5]
    return render_template('basic2.html',l=l)
if __name__ == '__main__':
    app.run(debug=True)
