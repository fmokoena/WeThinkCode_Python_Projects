import unittest
import world.obstacles as obstacles
from unittest.mock import patch
from io import StringIO

class MyTestCase(unittest.TestCase):

    def test_obstacle_list(self):
        """tests that the get_obstacles function returns a list of tupels"""
        obstacles.random.randint = lambda a, b: 1
        result = obstacles.get_obstacles()
        self.assertEqual(result , [(1,1)])

    def test_is_position_blocked(self):
        """tests that the is_postion_blocked function returns True if there is an obstacle in the postion"""
        obstacles.random.randint = lambda a, b: 1
        obstacles.get_obstacles()
        result = obstacles.is_position_blocked(1,1)
        obstacles.ob_be_gone()
        self.assertEqual(result , True)  

    def test_is_path_blocked(self):
        """tests that the is_path_blocked function returns True if there is an obstacle in the path"""
        obstacles.random.randint = lambda a, b: 1
        obstacles.get_obstacles()
        result = obstacles.is_path_blocked(2,0,2,20)
        obstacles.ob_be_gone()
        self.assertEqual(result , True)  

    def test_obstacle_postions(self):
        """tests that the obstacle_positons function prints out the coordinates of the obstacles"""
        obstacles.ob_be_gone()
        obstacles.random.randint = lambda a, b: 1
        obstacles.get_obstacles()
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.obstacle_positions()
        #obstacles.ob_be_gone()
        self.assertEqual(fake_out.getvalue() , """There are some obstacles:
- At position 1,1 (to 5,5)
- At position 1,1 (to 5,5)\n""")  

if __name__ == "__main__":
    unittest.main()