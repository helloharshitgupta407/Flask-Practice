from flask import Flask, render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, 
                    BooleanField,DateTimeField,SelectField,
                    TextAreaField, TextField,RadioField )
from wtforms.validators import DataRequired
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField("what breed are you ?", validators=[DataRequired()])
    neutered =BooleanField("have you been neutered ?")
    mood= RadioField("please choose your mood:",choices=[('mood1','excited'),('mood2','sad'),('mood3','happy')])
    food_choice= SelectField('pick your favourite food:',
                            choices=[('chi','Chicken'),('bf','beeef'),('fish','Fish')])
    feedback=TextAreaField()
    submit =SubmitField('Submit') 

@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data 
        session['neutered']=form.neutered.data
        session['mood']=form.mood.data
        session['food']=form.food_choice.data
        session['feedback']=form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('index.html',form=form)
    
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
if __name__ == '__main__':
    app.run(debug=True)