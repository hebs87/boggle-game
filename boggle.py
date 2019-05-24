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

def neighbours_of_position(coords):
    '''
    Get neighbours of a given position
    '''
    row = coords[0]
    col = coords[1]
    
    # Assign each of the neighbours
    # Top-left to top-right
    top_left = (row - 1, col -1)
    top_center = (row - 1, col)
    top_right = (row - 1, col +1)
    
    # Left to right
    left = (row, col - 1)
    # The `(row, col)` coordinates passed to this function are situated here (this is the center element with coords of (0,0))
    right = (row, col + 1)
    
    # Bottom-left to bottom-right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    # Return all the defined variables
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    '''
    Get all of the possible neighbours for each position in the grid
    '''
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours