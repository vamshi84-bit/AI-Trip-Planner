def generate_routes(source, destination):
    return {
        "car": {"time": "10 hrs", "price": 6000},
        "bus": {"time": "12 hrs", "price": 1200},
        "train": {"time": "9 hrs", "price": 2000},
        "flight": {"time": "1.5 hrs", "price": 5000},
        "best": {
            "cheapest": "bus",
            "fastest": "flight"
        }
    }