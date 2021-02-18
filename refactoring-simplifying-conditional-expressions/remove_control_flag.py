# by Kami Bigdely
# Remove control flag
def find_food(food, fridge):
    """Returns the value of 'food' if 'food' is in 'fridge'."""
    for item in fridge:
        if food.lower() in item.lower():
            return item

if __name__ == "__main__":
    food = 'wasabi'
    food_list = ['onion', 'cucumber', 'guacamole', 'kabob barg', 'wasabi']
    found_item = find_food(food, food_list)
    print(food, "Found: " + found_item  if found_item != None else "not found")
