from flask import Flask, render_template, request
from src.main import analyze_aspects, analyze_overall

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sentence = request.form.get("sentence")
        aspects_input = request.form.get("aspects")

        aspects = [a.strip() for a in aspects_input.split(",") if a.strip()]

        if not sentence or len(aspects) == 0:
            return render_template("index.html", error="Enter text and at least one aspect")

        aspect_results = analyze_aspects(sentence, aspects)
        overall_result = analyze_overall(sentence)

        return render_template(
            "index.html",
            sentence=sentence,
            aspect_results=aspect_results,
            overall=overall_result
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)