# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, something):
    """Appends 'something' to 'mix', then returns 'mix'..."""
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    """."""
    print('mixed ice with cream.')
    return ['ice', 'cream']

def make_drink(drink, addons):
    """."""
    mix = []
    if 'coffee' in drink:
        mix = add(mix, 'coffee')
    if 'strawberry milkshake' in drink:
        mix = add(mixer_ice_with_cream(), 'strawberry')
    mix = add(mix, addons)
    return mix

if __name__ == '__main__':
    final_drink = make_drink('strawberry milkshake', ['milk', 'sugar'])
    print(final_drink)
