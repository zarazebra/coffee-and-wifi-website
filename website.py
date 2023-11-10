from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from database import CafeDatabase, Cafe
from forms import AddCafeForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
bootstrap = Bootstrap5(app)
cafe_database = CafeDatabase()


@app.route("/")
def show_home():
    return render_template("index.html")


@app.route("/overview")
def show_overview():
    cafes = cafe_database.get_all_cafes()
    #value = request.form.get("inlineRadioOptions2")
    return render_template("overview.html", cafes=cafes)


@app.route("/<int:cafe_id>")
def show_details(cafe_id):
    cafe = cafe_database.select_cafe(cafe_id)
    return render_template("cafe.html", cafe=cafe)


@app.route("/new")
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )
        cafe_database.add_cafe(new_cafe)
        cafe_database.convert_price_to_float()
        flash("The new cafe has successfully been added!")
        return redirect(url_for("add_cafe"))

    return render_template("suggestion.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
