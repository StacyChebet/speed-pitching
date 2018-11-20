from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    profile = TextAreaField("Tell us about you", validators = [Required()])
    submit = SubmitField("Pitch")