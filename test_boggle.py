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
    
    