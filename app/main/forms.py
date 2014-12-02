from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Username', validators=[Required()])
    room = StringField('Room', validators=[Required()])
    room2 = StringField('Room2', validators=[Required()])
    mafia = StringField('Mafia', validators=[Required()])
    narrator = StringField('Narrator', validators=[Required()])
    #not_mafia = StringField('Not Mafia', validators=[Required()])
    submit = SubmitField('Enter Chatroom')
