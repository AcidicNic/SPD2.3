# by Kami Bigdely
# Consolidate conditional expressions
SHIRAZI_SALAD_INGREDIENTS = ["cucumber", "tomato", "onion", "lemon juice"]

def dice(ingredients):
    """Dices 'ingredients'."""
    print("diced all ingredients.")

def mix_all(diced_ingredients):
    """Mixes the diced ingredients in 'diced_ingredients'."""
    print("mixed all.")

def add_salt():
    """Adds a dash salt."""
    print("added salt.")

def pour(liquid):
    """Pours 'liquid'."""
    print(f"poured {liquid}.")

def contains_all_ingredients(ingredients, required_ingredients):
    """Returns True if 'ingredients' contains every item in
    'required_ingredients'.
    """
    for ingredient in required_ingredients:
        if ingredient not in ingredients:
            return False
    return True

def make_shirazi_salad(ingredients):
    """Makes a salad, if all ingredients are present."""
    if not contains_all_ingredients(ingredients, SHIRAZI_SALAD_INGREDIENTS):
        print("lacks ingredients.")
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour("lemon juice")
    print("Your yummy shirazi salad is ready!")

if __name__ == "__main__":
    make_shirazi_salad(["cucumber", "tomato", "lemon juice", "onion"])
