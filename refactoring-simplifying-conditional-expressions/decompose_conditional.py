# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

toxins = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']

def make_alert_sound():
    print('made alert sound.')

def make_accept_sound():
    print('made acceptance sound')

def contains_toxins(ingredients):
    """Returns true if any item from 'toxins' is found in 'ingredients'."""
    return any(ingredient in toxins for ingredient in ingredients)


if __name__ == '__main__':
    # Tests our functions
    if contains_toxins(['sodium benzoate']):
        print('!!!')
        print('there is a toxin in the food!')
        print('!!!')
        make_alert_sound()
    else:
        print('***')
        print('Toxin Free')
        print('***')
        make_accept_sound()
