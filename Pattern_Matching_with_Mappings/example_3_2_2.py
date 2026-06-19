food = dict(category="ice cream", flavor="vanilla", cost=199)

match food:
    case {"category": "ice cream", **details}:
        print(f"Ice cream details: {details}")
