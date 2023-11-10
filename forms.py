from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, RadioField, BooleanField, FloatField
from wtforms.validators import DataRequired, URL


class AddCafeForm(FlaskForm):
    name = StringField("Name Of Cafe", validators=[DataRequired()])
    map_url = StringField("Maps URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = BooleanField("Sockets")
    has_toilet = BooleanField("Toilet")
    has_wifi = BooleanField("WiFi")
    can_take_calls = BooleanField("Calls")
    seats = RadioField("No. Of Seats", choices=["0-10", "10-20", "20-30", "30-40", "40-50", "50+"], validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", default="£", validators=[DataRequired()])
    submit = SubmitField("Add new cafe")
