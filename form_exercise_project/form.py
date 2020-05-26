from flask import Flask,session,render_template,redirect,flash,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class SimpleForm(FlaskForm):
    breed = StringField('What breed are you?')
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form =SimpleForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data 
        flash('You just changed your breed to:')
        return redirect(url_for('index'))
    return render_template('index.html',form=form)
if __name__ == '__main__':
    app.run(debug=True)