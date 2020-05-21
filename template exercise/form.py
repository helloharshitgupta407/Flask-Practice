from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    name=request.args.get('name')
    a=0
    b=0
    c=0
    for i in range(len(name)):
        if name[i].isupper():
            a=1
        if name[i].islower():
            b=1
    if name[-1].isdigit():
        c=1
    return render_template('check.html',a=a,b=b,c=c)

    
if __name__ == '__main__':
    app.run(debug=True)