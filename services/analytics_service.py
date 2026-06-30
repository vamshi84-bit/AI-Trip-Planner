def generate_chart_data(cost):
    return {
        "labels": ["Transport", "Hotel", "Food", "Misc"],
        "values": [
            cost["transport"],
            cost["hotel"],
            cost["food"],
            cost["misc"]
        ]
    }