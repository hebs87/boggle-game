def make_grid(width, height):
    '''
    1. Make an empty boggle grid after writing the first test to test for empty grid = return {}
    2. Create a grid that will hold all the tiles for the boggle game
    '''
    # Creates a dictionary with the row column tuple as the key and a space as the value
    return {(row, col): ' '
        for row in range(height)
        for col in range(width)}
    