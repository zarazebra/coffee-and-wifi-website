from flask import Flask, render_template
from database import CafeDatabase
app = Flask(__name__)


@app.route("/")
def show_home():
    return render_template("index.html")


@app.route("/overview")
def show_overview():
    cafe_database = CafeDatabase()
    cafes = cafe_database.get_all_cafes()
    return render_template("overview.html", cafes=cafes)


@app.route("/<int:cafe_id>")
def show_details(cafe_id):
    cafe_database = CafeDatabase()
    cafe = cafe_database.select_cafe(cafe_id)
    return render_template("cafe.html", cafe=cafe)


@app.route("/new")
def add_cafe():
    return render_template("suggestion.html")


if __name__ == "__main__":
    app.run(debug=True)
