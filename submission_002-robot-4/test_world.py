import unittest
import world.text.world
import world.obstacles as obstacles
from unittest.mock import patch
from io import StringIO

class MyTestCase(unittest.TestCase):

    def test_world_positon(self):
        """tests that the coordinates of the robot are correctly displayed"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            world.text.world.track_position(100, 50, "BMO", False)
        world.text.world.blobal_bariables(0)
        self.assertEqual(fake_out.getvalue(), """ > BMO now at position (50,100).
""")

    def test_world_range(self):
        """tests that the robot doesnt move outside the world range"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            world.text.world.check_position_range(201, 0, ["forward" , "201"], "BMO", False)

        self.assertEqual(fake_out.getvalue(), """BMO: Sorry, I cannot go outside my safe zone.
 > BMO now at position (0,0).
""")

    def test_world_obstacle(self):
        """tests that the robot doesnt move over obstacles"""
        obstacles.random.randint = lambda a, b: 1
        obstacles.get_obstacles()
        #result = obstacles.is_position_blocked(1,1)
        #obstacles.ob_be_gone()
        with patch('sys.stdout', new = StringIO()) as fake_out:
            world.text.world.check_position_range(3, 1, ["forward" , "3"], "BMO", False)

        self.assertEqual(fake_out.getvalue(), """Sorry, there is an obstacle in the way.
 > BMO now at position (0,0).\n""") 


if __name__ == "__main__":
    unittest.main()