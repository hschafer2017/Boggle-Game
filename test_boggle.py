import unittest
from boggle import *
from string import ascii_uppercase

class TestBoggle(unittest.TestCase): 
    def test_empty_grid(self): 
        grid = make_grid(0,0)
        self.assertEqual(grid, {})
    
    def test_not_empty_grid(self): 
        grid = make_grid(2,2)
        self.assertEqual(len(grid), 4)
        
    def test_grid_has_uppercase(self):
        grid = make_grid(2,2)
        
        print(grid)
        
        for c in grid.values(): # will return a list of values in the grid 
            self.assertIn(c, ascii_uppercase)
            
            
    def test_neighbours_of_cell(self): 
        neighbours = get_neighbours((3,4))
        
        expected = [
            (2,3),
            (3,3),
            (4,3),
            (4,4),
            (4,5),
            (3,5),
            (2,5), 
            (2,4), 
            ]
        
        self.assertEqual(neighbours, expected)

    def test_all_grid_neighbours(self):
        actual = all_grid_neighbours(make_grid(2,2))
        expected = {
            (0,0):[(1,0), (0,1), (1,1)], 
            (1,0):[(0,0), (0,1), (1,1)], 
            (0,1):[(1,0), (0,0), (1,1)], 
            (1,1):[(1,0), (0,1), (0,0)] 
        }
        self.assertDictEqual(actual,expected)