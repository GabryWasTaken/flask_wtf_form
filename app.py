from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecret'

class MyForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    freeform = TextAreaField('Free Form')
    selects = SelectField('Select', choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')])
    radios = RadioField('Radios', default='option1', choices=[('option1', 'Option1'), ('option2', 'Option2 ')])

@app.route('/', methods=['GET', 'POST'])  
def index():
    form = MyForm()
    if form.validate_on_submit():
        results = {
            'email' : form.email.data,
            'password' : form.password.data,
            'freeform' : form.freeform.data,
            'radios' : form.radios.data,
            'selects' : form.selects.data
        }
        return render_template('results.html', results=results)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)