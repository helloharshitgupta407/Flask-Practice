from flask import Flask 
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>hello harshit</h1>' 
@app.route('/information')
def info():
    return '<h1>hello harshit 1234</h1>'
@app.route('/puppy/<name>')
def puppy(name):
    return '<h1>puppy name is {}</h1>'.format(name)
if __name__ == '__main__':
    app.run()
