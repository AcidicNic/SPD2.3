# by Kami Bigdely
# Extract Class
FOOD_DATA = {
    "Butternut Squash Soup":[
        45, True, "soup", "North African",
        ["butter squash", "onion", "carrot", "garlic", "butter",
            "black pepper", "cinnamon", "coconut milk"],
        [
            "1. Grill the butter squash, onion, carrot and garlic in the oven until they get soft and golden on top.",
            "2. Put all in blender with butter and coconut milk. Blend them till they become puree. Then move the content into a pot. Add coconut milk. Simmer for 5 mintues."
        ]
    ],
    "Shirazi Salad":[
        5, True, "salad", "Iranian",
        ["cucumber", "tomato", "onion", "lemon juice"],
        [
            "1. dice cucumbers, tomatoes and onions.",
            "2. put all into a bowl", "3. pour lemon juice.",
            "3. add salt.", "4. Mixed them thoroughly"
        ]
    ],
    "Homemade Beef Sausage":[
        60, False, "deli", "All",
        ["sausage casing", "regular ground beef", "garlic", "corriander seeds",
            "black pepper seeds", "fennel seed", "paprika"],
        [
            "1. In a blender, blend corriander seeds, black pepper seeds, fennel seeds and garlic to make the seasonings.",
            "2. In a bowl, mix ground beef with the seasoning.",
            "3. Add all the content to a sausage stuffer. Put the casing on the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"
        ]
    ]
}
BOLD = '\033[1m'
END = '\033[0m'

class Food:
    """Represents a food."""
    def __init__(self, name, prep_time, veg, type,
                cuisine, ingredients, recipe):
        self.name = name
        self.prep_time = prep_time
        self.veg = veg
        self.type = type
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.recipe_steps = recipe

    def get_pretty_recipe(self):
        """Returns a str of the recipe list"""
        return '\n\t'.join(self.recipe_steps)

    def print_summary(self):
        """Prints all of this food's information."""
        print(get_bold(self.name))
        print(f"{get_bold('Prep Time')}: {self.prep_time} min")
        print(f"{get_bold('Veggie')}: {'Yes' if self.veg else 'No'}")
        print(f"{get_bold('Type')}: {self.type}")
        print(f"{get_bold('Cuisine')}: {self.cuisine}")
        print(f"{get_bold('Ingredients')}: {', '.join(self.ingredients)}")
        print(f"{get_bold('Recipe')}: \n\t{self.get_pretty_recipe()}")

def get_bold(text):
    """Returns 'text' formatted to look bold."""
    return f"{BOLD}{text}{END}"

def dict_to_food(data):
    """Returns a list of Food objects created form a dict."""
    food_list = []
    for key, value in FOOD_DATA.items():
        food = Food(key, value[0], value[1], value[2],
                    value[3], value[4], value[5])
        food_list.append(food)
    return food_list

if __name__ == '__main__':
    foods = dict_to_food(FOOD_DATA)
    for food in foods:
        food.print_summary()
        print("\n***\n")
