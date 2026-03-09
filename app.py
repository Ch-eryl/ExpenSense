from flask import Flask, render_template, request
from analyzer import analyze_spending

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = None

    if request.method == "POST":
        file = request.files["file"]

        personality, burn, savings, advice = analyze_spending(file)

        result = {
            "personality": personality,
            "burn": burn,
            "savings": savings,
            "advice": advice
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
