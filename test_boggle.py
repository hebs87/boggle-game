'''
unittest framework uses classes and inheritance
To create tests, we will create a class that inherits from the testcase class in the framework
Then we write methods inside that class for the actual tests
'''
import unittest
# Here, we import boggle, as this is where the code that we're testing resides
import boggle
# Here we import the ascii_uppercase function from the string library - these are the 26 ASCII uppercase characters from A-Z
from string import ascii_uppercase

'''
SAMPLE TEST TO ENSURE THAT UNITTEST IS WORKING - THIS CAN BE DELETED ONCE THIS HAS BEEN ESTABLISHED
#Create a class that inherits from the Testcase()
class test_boggle(unittest.TestCase):
    # Now, write a method beginning with test_, which is the convention for Python tests
    def test_is_this_thing_on(self):
        # Use the assertEqual() method and ask if 1 == 0
        self.assertEqual(1, 1)
'''

class TestBoggle(unittest.TestCase):
    '''
    Our test suite for boggle solver
    '''
    
    def test_can_create_empty_grid(self):
        '''
        Test to see if we can create an empty grid
        '''
        # Here we make a grid with no rows or columns - boggle is the file we've imported and make_grid is the function that we've created in boggle.py
        grid = boggle.make_grid(0,0)
        # Test assertion is that a grid with no rows or columns has a length of 0
        self.assertEqual(len(grid),0)
    
    def test_grid_size_is_width_times_height(self):
        '''
        Test is to ensure that the total size of the grid
        is equal to width * height
        '''
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)
    
    def test_grid_coordinators(self):
        '''
        Test to see that all of the coordinates inside of the grid can be accessed
        These are horizontal, vertical and diagonal neighbours
        '''
        grid = boggle.make_grid(2,2)
        # assertIn() method tests whether the relevant coordinates are in the grid
        self.assertIn((0,0), grid)
        self.assertIn((0,1), grid)
        self.assertIn((1,0), grid)
        self.assertIn((1,1), grid)
        # assertNotIn() method ensures that 2,2 is not in the grid
        self.assertNotIn((2,2), grid)
    
    def test_grid_is_filled_with_letters(self):
        '''
        Ensure that each of the coordinates in the grid contains letters
        '''
        grid = boggle.make_grid(2,3)
        # Test creates a grid and then ensures that each of the characters in the test are uppercase letters
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
    
    def test_neighbours_of_a_position(self):
        '''
        Ensure that a position has 8 neighbours
        '''
        coords = (1,2)
        # We call functions that we will define after writing the test
        neighbours = boggle.neighbours_of_position(coords)
        #This takes the position of a grid and returns the 8 neighbours that it should have
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
    
    def test_all_grid_neighbours(self):
        '''
        Ensure that all of the grid positions have neighbours (this accounts for the edge and corner pieces)
        In (2,2) grid, every position touches every other position, so the neighbours of any position are other three positions in the grid
        '''
        grid = boggle.make_grid(2,2)
        # We get all the neighbours for the grid - dictionary where key is the position but value is list of neighbouring positions
        neighbours = boggle.all_grid_neighbours(grid)
        # Asserts the length of the neighbours dictionary, which should be equal to the grid length
        self.assertEqual(len(neighbours), len(grid))
        # The for loop iterates through the other positions - we create the others list, which is the full grid minus the current position
        for pos in grid:
            others = list(grid)
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
    
    def test_converting_a_path_to_a_word(self):
        '''
        Ensure that paths can be converted to words
        '''
        # Make random grid for now, we just want to turn letters into a string and make a word, regardless of whether the word exists
        grid = boggle.make_grid(2, 2)
        # We can access any letter in the grid by its coordinates, in this case it's 0,0
        # Ensures the function returns the same string as we manually select in the game
        oneLetterWord = boggle.path_to_word(grid, [(0,0)])
        twoLetterWord = boggle.path_to_word(grid, [(0,0), (1,1)])
        self.assertEqual(oneLetterWord, grid[(0,0)])
        self.assertEqual(twoLetterWord, grid[(0,0)] + grid[(1,1)])
    
    def test_search_grid_for_words(self):
        '''
        Ensure that certain patterns can be found in a path_to_word
        '''
        # Create a mock grid with letters A, B, C and D so we can control our letters
        grid = {(0,0): 'A', (0,1): 'B', (1,0): 'C', (1,1): 'D',}
        # Define a dictionary of three words - two in the grid and should be found, one not in the grid and should not be found
        twoLetterWord = 'AB'
        threeLetterWord = 'ABC'
        notThereWord = 'EEE'
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
    
    def test_load_dictionary(self):
        '''
        Test that the 'get_dictionary' function returns a dictionary that has
        a length greater than 0
        '''
        # The file name is of a file we will create in our workspace
        # We will get the data from a word file website
        dictionary = boggle.get_dictionary('words.txt')
        self.assertGreater(len(dictionary), 0)
    
    