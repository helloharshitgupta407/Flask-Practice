from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    some_variable='Harshit'
    letters=list(some_variable)
    cast_dict= {'cast_name':'Gupta'}
    return render_template('basic1.html',my_variable=some_variable, letters=letters, cast_dict=cast_dict)
if __name__ == '__main__':
    app.run(debug=True)
