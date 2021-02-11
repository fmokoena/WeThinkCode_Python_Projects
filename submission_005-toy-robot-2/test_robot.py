import unittest
import robot
from unittest.mock import patch
from io import StringIO

class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("BMO\noff\n"))
    def test_name_robot(self):
        """tests that the users input returns as the robots name"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.name_robot()
        self.assertEqual(fake_out.getvalue(), "What do you want to name your robot? BMO: Hello kiddo!\n")


    def test_help(self):
        """tests that the help command prints out a list containing all the valid commands and their purpose"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.process_command("help","BMO")
        self.assertEqual(fake_out.getvalue(), """I can understand these commands:

    OFF  - Shut down robot

    HELP - provide information about commands

    forward 0 - moves the robot forward "0" steps 
    "0" represents a value that you must input

    back 0 -  moves the robot backwards "0" steps
    "0" represents a value that you must input

    right - turns the robot right

    left - turns the robot left

    sprint - gives the robot a short burst of speed and extra distance
    \n""")
    

    @patch("sys.stdin", StringIO("BMO\nalbatross\noff\n"))
    def test_invalid(self):
        """tests that the program prints a string and returns to input when an invalid command is submitted"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next? BMO: Sorry, I did not understand 'albatross'.
BMO: What must I do next? BMO: Shutting down..
""")


    @patch("sys.stdin", StringIO("BMO\nforward 10\nback 5\noff\n"))
    def test_movement(self):
        """tests that the robot moves correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 10 steps.
 > BMO now at position (0,10).
BMO: What must I do next?  > BMO moved back by 5 steps.
 > BMO now at position (0,5).
BMO: What must I do next? BMO: Shutting down..
""")


    @patch("sys.stdin", StringIO("BMO\nright\nleft\noff\n"))
    def test_turning(self):
        """tests that the robot turns correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO turned right.
 > BMO now at position (0,0).
BMO: What must I do next?  > BMO turned left.
 > BMO now at position (0,0).
BMO: What must I do next? BMO: Shutting down..
""")


    @patch("sys.stdin", StringIO("BMO\nsprint 5\noff\n"))
    def test_sprint(self): 
        """tests that the robot sprints correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 5 steps.
 > BMO moved forward by 4 steps.
 > BMO moved forward by 3 steps.
 > BMO moved forward by 2 steps.
 > BMO moved forward by 1 steps.
 > BMO now at position (0,15).
BMO: What must I do next? BMO: Shutting down..
""")


    @patch("sys.stdin", StringIO("BMO\nforward 190\nforward 11\noff\n"))
    def test_area_restricted(self):
        """tests that the robot can not and does not move outside of a certain range"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 190 steps.
 > BMO now at position (0,190).
BMO: What must I do next? BMO: Sorry, I cannot go outside my safe zone.
 > BMO now at position (0,190).
BMO: What must I do next? BMO: Shutting down..
""")


if __name__ == "__main__":
    unittest.main()