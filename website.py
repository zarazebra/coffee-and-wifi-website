from flask import Flask, render_template
from database import CafeResearch
app = Flask(__name__)


@app.route("/")
def home():
    caferesearch = CafeResearch()
    cafes = caferesearch.get_all_cafes()
    return render_template("index.html", cafes=cafes)


if __name__ == "__main__":
    app.run(debug=True)
