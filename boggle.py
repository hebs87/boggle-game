# This needs to imported into our document, as well as the test document
from string import ascii_uppercase
# Choice function returns an item from a list at random (in this case, it will be from the ascii_uppercase list)
from random import choice


def make_grid(width, height):
    '''
    1. Make an empty boggle grid after writing the first test to test for empty grid = return {}
    2. Create a grid that will hold all the tiles for the boggle game
    '''
    # Creates a dictionary with the row column tuple as the key and a choice of uppercase ascii characters as the value
    return {(row, col): choice(ascii_uppercase)
        for row in range(height)
        for col in range(width)}
    