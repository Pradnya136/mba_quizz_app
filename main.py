from flask import Flask, render_template, abort
from models.dal import question_set

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/qus/<int:index>")
def questions(index):
    try:
        qus = question_set[index]
        return render_template("questions.html", qus=qus, index=index)

    except IndexError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
