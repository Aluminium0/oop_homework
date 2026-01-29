#Task 1

def read_cook_book(file_path):
    cook_book = {}

    with open(file_path, encoding="utf-8") as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            count = int(file.readline().strip())
            ingredients = []

            for _ in range(count):
                line = file.readline().strip()
                name, quantity, measure = line.split(" | ")

                ingredients.append({
                    "ingredient_name": name,
                    "quantity": int(quantity),
                    "measure": measure
                })

            cook_book[dish_name] = ingredients
            file.readline()

    return cook_book


cook_book = read_cook_book("recipes.txt")
print(cook_book)


# Task 2


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            continue

        for ingredient in cook_book[dish]:
            name = ingredient["ingredient_name"]
            measure = ingredient["measure"]
            quantity = ingredient["quantity"] * person_count

            if name in shop_list:
                shop_list[name]["quantity"] += quantity
            else:
                shop_list[name] = {
                    "measure": measure,
                    "quantity": quantity
                }

    return shop_list


# Example
shop_list = get_shop_list_by_dishes(
    ["Запеченный картофель", "Омлет"],
    2,
    cook_book
)

print(shop_list)
