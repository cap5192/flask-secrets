from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='login')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
