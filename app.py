from flask import Flask, render_template, request
from services.ai_service import generate_ai_plan

app = Flask(__name__)

def generate_routes(source, destination):
    return {
        "car": {
            "time": "10 hrs",
            "price": 6000,
            "path": [source, "Highway", "City Center", destination]
        },
        "bus": {
            "time": "12 hrs",
            "price": 1200,
            "path": [source + " Bus Stand", "Mid Stop", destination + " Bus Stop"]
        },
        "train": {
            "time": "9 hrs",
            "price": 2000,
            "path": [source + " Railway Station", "Junction", destination + " Station"]
        },
        "flight": {
            "time": "1.5 hrs",
            "price": 5000,
            "path": [source + " Airport", "Air Route", destination + " Airport"]
        },
        "best": {
            "cheapest": "bus",
            "fastest": "flight"
        }
    }
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]
        days = int(request.form["days"])
        budget = int(request.form["budget"])

        plan = generate_ai_plan(source, destination, days, budget)

        total_cost = int(budget * 0.7)
        remaining = budget - total_cost
        percent = int((total_cost / budget) * 100) if budget else 0

        result = {
            "plan": plan,
            "budget": budget,
            "cost": {
                "total": total_cost,
                "remaining": remaining
            },
            # ✅ FIX HERE
            "routes": generate_routes(source, destination),
            "percent": percent
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)