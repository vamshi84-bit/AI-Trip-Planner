def calculate_cost(days, budget):
    budget = int(budget)

    transport = int(budget * 0.4)
    hotel = int(budget * 0.3)
    food = int(budget * 0.2)

    total = transport + hotel + food
    remaining = budget - total

    return {
        "transport": transport,
        "hotel": hotel,
        "food": food,
        "total": total,
        "remaining": remaining
    }