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


