import json


def task() -> float:
    with open("input.json", 'r') as json_file:
        json_data = json.load(json_file)
    total_sum = sum([dict["score"] * dict["weight"] for dict in json_data])
    return round(total_sum, 3)


print(task())
