class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def show_ingredients(self):
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"Започваме приготвянето на {self.name}...")
        steps = []
        if any("лук" in ingredient.lower() for ingredient in self.ingredients):
            steps.append("1. Загрейте тиган и добавете нарязан лук.")
        if any("месо" in ingredient.lower() for ingredient in self.ingredients):
            steps.append("2. Добавете месо и гответе, докато стане златисто.")
        if any("домати" in ingredient.lower() for ingredient in self.ingredients):
            steps.append("3. Добавете нарязани домати и разбъркайте.")
        if any("сол" in ingredient.lower() or "черен пипер" in ingredient.lower() for ingredient in self.ingredients):
            steps.append("4. Подправете със сол и черен пипер на вкус.")

        steps.append("5. Намалете огъня и оставете да къкри за 30 минути.")
        steps.append(f"{self.name} е готово!")

        for step in steps:
            print(step)


ingredients = []

while True:
    ingredient = input("Искате ли да добавите съставка? (да/не): ").strip().lower()
    if ingredient == "да":
        new_ingredient = input("Въведете име на нова съставка: ").strip()
        if new_ingredient:
            ingredients.append(new_ingredient)
        else:
            print("Моля, въведете валидно име на съставка.")
    elif ingredient == "не":
        break
    else:
        print("Моля, отговорете с 'да' или 'не'.")

recipe_name = input("Въведете име на рецептата: ").strip()
recipe = Recipe(recipe_name, ingredients)

recipe.show_ingredients()
recipe.cook()
