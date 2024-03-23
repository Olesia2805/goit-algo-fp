
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    sorted_items = dict(sorted(items.items(), key=lambda item: item[1]['calories'], reverse=True))

    for item, value in sorted_items.items():
        if remaining_budget >= value['cost']:
            chosen_items.append(item)
            total_calories += value['calories']
            remaining_budget -= value['cost']

    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    num_items = len(item_names)

    dp_table = [[0 for _ in range(budget + 1)] for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(1, budget + 1):
            item_cost = items[item_names[i - 1]]['cost']
            item_calories = items[item_names[i - 1]]['calories']
            if item_cost <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - item_cost] + item_calories)
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    chosen_items = []
    temp_calories = dp_table[num_items][budget]
    remaining_budget = budget
    i = num_items
    w = budget

    while i > 0 and temp_calories > 0:
        if temp_calories != dp_table[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            temp_calories -= items[item_names[i - 1]]['calories']
            remaining_budget -= items[item_names[i - 1]]['cost']
            w -= items[item_names[i - 1]]['cost']
        i -= 1


    return dp_table[num_items][budget], budget - remaining_budget, chosen_items

if __name__ == '__main__':

    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(greedy_result, dp_result)
