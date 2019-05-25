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
    The value of the neighbours_of_position() function is passed into this
    '''
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

def path_to_word(grid, path):
    '''
    Add all of the letters on the path to a string
    '''
    # Gets list of letters for the path and joins them into a string
    return ''.join([grid[p] for p in path])

'''
def word_in_dictionary(word, dict):
    ***This function is created after running the cProfile to isolate the method
    that is taking the most time. In this case is was to search whether a word
    was in the dictionary
    CAN BE DELETED AFTER PRUNING***
    return word in dict
'''

def search(grid, dictionary):
    '''
    Search through the paths to locate the words
    by matching the strings to words in the dictionary
    First we get the neighbors of every position in the grid
    and then we get the paths list to capture all paths that form valid words.
    We are storing paths rather than strings, as a letter could be repeated in
    the grid several times, if we had two letter A's and we saved a word with
    an A in it how would we know which A it is?
    '''
    neighbours = all_grid_neighbours(grid)
    paths = []
    # ***PRUNED CODE - UNPACK DICTIONARY TUPLE INTO THE OTHER TWO***
    full_words, stems = dictionary
    
    def do_search(path):
        '''
        We do a do_search function, which is a nested function.
        The do search function exists within the scope of the search function code.
        It can't be called directly. The do search function has access to the other
        variables defined within search such as the paths list which it can add to.
        The do search function can be called by the search function and can call
        itself recursively to build up paths. The search function starts to search
        by passing a single position to the do_search. This is a path of one letter.
        The do_search function converts whatever path that's given into a word and
        checks if it's in the dictionary. If the path makes a word it's added to the
        paths list, whether the path is a word or not. do_search gets each of the
        neighbors of the last letter and checks to make sure the neighboring letter
        isn't already in the path and then continues the searching from that letter.
        So do_search call itself eight times for each starting position and again
        for each of the various neighbors of each neighbor and so on for each
        position in the grid. We do a search and convert all the paths and make
        valid words into words and return them in a list.
        '''
        word = path_to_word(grid, path)
        '''
        if word in dictionary: - this was the original, but changed to the below
        After writing the word_in_dictionary() function, and we pass it
        arguments of word and dictionary
        if word_in_dictionary(word, dictionary):
        ***AFTER word_in_dictionary PRUNED, THIS NEEDS TO BE MODIFIED
        '''
        if word in full_words:
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    
    # We move out of do_search function and back into search function now
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)

def get_dictionary(dictionary_file):
    '''
    Load dictionary file
    Change the [] on the last line to {} instead, which ensures that the words
    are stored in a set, rather than a list. This speeds up the run time, as
    it is a better data structure
    ***FINAL STEP - PRUNING***
    Original code:
    with open(dictionary_file) as f:
        return {w.strip().upper() for w in f}
    Create a second dictionary to that contains all partial words (stems)
    Eg. If dictionary contains the words BUS and THIS, stems dictionary would
    contain B, BU, T, TH and THI. If the stems existed, we could do a
    simultaneous constant time lookup, rather than linear time lookup.
    ***Once this is done, we need to modify our search function
    '''
    # Creating two tuples with two sets - one set for full word, other for stems
    full_words, stems = set(), set()
    with open(dictionary_file) as f:
        # We iterate over the fictionary and get the full words and add it to full_words tuple
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            # Nested for loop for the stems
            for i in range(1, len(word)):
                stems.add(word[:i])
    
    # We then return the full words and stems
    return full_words, stems

def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))

def main():
    '''
    This is the function that will run the whole project
    '''
    # Generate a random board
    grid = make_grid(100,100)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    display_words(words)

'''
If we simply call main(), that will be run each time we run unittest too
We want to only run boggle.py when we actually want to run the game
We want to ignore it when we run our tests
This is achieved with the below code
'''
if __name__ == "__main__":
    main()
