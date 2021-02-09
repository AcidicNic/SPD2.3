# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def get_area_under_graph(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_greatest_value(li):
    """Returns the greatest value in 'li'."""
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(get_greatest_value(li))

############################
def get_word_list(sentence):
    """Returns a list of words from the str 'sentence'."""
    words = sentence[0:].split(' ')
    return words

print(get_word_list('If you were a vegetable, you’d be a ‘cute-cumber.'))
