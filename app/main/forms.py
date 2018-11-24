from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class AddPitch(FlaskForm):
    name = StringField("Title", validators=[Required()])
    category = SelectField("category",choices=[("Business", "Business"),("Funny","Funny"),("Pick-up lines","Pick-up lines"),("Promotion","Promotion")])
    content = TextAreaField("Pitch", validators=[Required()])
    submit = SubmitField("Pitch!")

class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Comment")

class UpdateProfile(FlaskForm):
    profile = TextAreaField("Tell us about you", validators = [Required()])
    submit = SubmitField("Add")