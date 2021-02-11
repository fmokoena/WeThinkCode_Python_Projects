import unittest
import robot
from unittest.mock import patch
from io import StringIO
import world.obstacles as obstacles

class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("BMO\noff\n"))
    def test_name_robot(self):
        """tests that the users input returns as the robots name"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.name_robot()
        self.assertEqual(fake_out.getvalue(), "What do you want to name your robot? BMO: Hello kiddo!\n")


    def test_help(self):
        """tests that the help command prints out a list containing all the valid commands and their purpose"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            robot.process_command("help","BMO")
        self.assertEqual(fake_out.getvalue(), """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves the robot forward  
BACK -  moves the robot bacK
RIGHT - turns the robot right
LEFT - turns the robot left
SPRINT - gives the robot a short burst of speed and extra distance
REPLAY - replays previous movements
SILENT - only prints position when robot is replayed
REVERSE - replays previous movements in backwards order
    \n""")
    
    def test_history(self):
        """tests that the program suceeds in capturing the movement commands as a list"""
        result = robot.command_history("forward 10")
        self.assertEqual(result , ["forward 10"])


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
            obstacles.random.randint = lambda a, b: 0
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
            obstacles.random.randint = lambda a, b: 0
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
            obstacles.random.randint = lambda a, b: 0
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
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 190 steps.
 > BMO now at position (0,190).
BMO: What must I do next? BMO: Sorry, I cannot go outside my safe zone.
 > BMO now at position (0,190).
BMO: What must I do next? BMO: Shutting down..
""")

    @patch("sys.stdin", StringIO("BMO\nforward 10\nback 5\nreplay\noff\n"))
    def test_replay_movement(self):
        """tests that the robot replays correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 10 steps.
 > BMO now at position (0,10).
BMO: What must I do next?  > BMO moved back by 5 steps.
 > BMO now at position (0,5).
BMO: What must I do next?  > BMO moved forward by 10 steps.
 > BMO now at position (0,15).
 > BMO moved back by 5 steps.
 > BMO now at position (0,10).
 > BMO replayed 2 commands.
 > BMO now at position (0,10).
BMO: What must I do next? BMO: Shutting down..
""")

    @patch("sys.stdin", StringIO("BMO\nforward 10\nback 5\nreplay silent\noff\n"))
    def test_replay_silent(self):
        """tests that the robot silently replays correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 10 steps.
 > BMO now at position (0,10).
BMO: What must I do next?  > BMO moved back by 5 steps.
 > BMO now at position (0,5).
BMO: What must I do next?  > BMO replayed 2 commands silently.
 > BMO now at position (0,10).
BMO: What must I do next? BMO: Shutting down..
""")

    @patch("sys.stdin", StringIO("BMO\nforward 10\nback 5\nreplay reversed\noff\n"))
    def test_replay_reversed(self):
        """tests that the robot replays in reverse correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 10 steps.
 > BMO now at position (0,10).
BMO: What must I do next?  > BMO moved back by 5 steps.
 > BMO now at position (0,5).
BMO: What must I do next?  > BMO moved back by 5 steps.
 > BMO now at position (0,0).
 > BMO moved forward by 10 steps.
 > BMO now at position (0,10).
 > BMO replayed 2 commands in reverse.
 > BMO now at position (0,10).
BMO: What must I do next? BMO: Shutting down..
""")

    @patch("sys.stdin", StringIO("BMO\nforward 10\nback 5\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent(self):
        """tests that the robot silently replays correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 10 steps.
 > BMO now at position (0,10).
BMO: What must I do next?  > BMO moved back by 5 steps.
 > BMO now at position (0,5).
BMO: What must I do next?  > BMO replayed 2 commands in reverse silently.
 > BMO now at position (0,10).
BMO: What must I do next? BMO: Shutting down..
""")

    @patch("sys.stdin", StringIO('BMO\nforward 1\nforward 2\nforward 3\nreplay a\noff\n'))
    def test_replay_invalid(self):
        """tests that the robot replays within the given range correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        output = fake_out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 1 steps.
 > BMO now at position (0,1).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,3).
BMO: What must I do next?  > BMO moved forward by 3 steps.
 > BMO now at position (0,6).
BMO: What must I do next? BMO: Sorry, I did not understand 'replay a'.
BMO: What must I do next? BMO: Shutting down..""", output)

    @patch("sys.stdin", StringIO('BMO\nforward 1\nforward 2\nforward 3\nreplay 2\noff\n'))
    def test_replay_range(self):
        """tests that the robot replays within the given range correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        output = fake_out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 1 steps.
 > BMO now at position (0,1).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,3).
BMO: What must I do next?  > BMO moved forward by 3 steps.
 > BMO now at position (0,6).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,8).
 > BMO moved forward by 3 steps.
 > BMO now at position (0,11).
 > BMO replayed 2 commands.
 > BMO now at position (0,11).
BMO: What must I do next? BMO: Shutting down..""", output)

    @patch("sys.stdin", StringIO('BMO\nforward 1\nforward 2\nforward 3\nforward 4\nforward 5\nreplay 2-4\noff\n'))
    def test_replay_two_ranges(self):
        """tests that the robot replays within the given range values correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        output = fake_out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 1 steps.
 > BMO now at position (0,1).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,3).
BMO: What must I do next?  > BMO moved forward by 3 steps.
 > BMO now at position (0,6).
BMO: What must I do next?  > BMO moved forward by 4 steps.
 > BMO now at position (0,10).
BMO: What must I do next?  > BMO moved forward by 5 steps.
 > BMO now at position (0,15).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,17).
 > BMO moved forward by 3 steps.
 > BMO now at position (0,20).
 > BMO replayed 2 commands.
 > BMO now at position (0,20).
BMO: What must I do next? BMO: Shutting down..""", output)

    @patch("sys.stdin", StringIO('BMO\nforward 1\nforward 2\nforward 3\nforward 4\nforward 5\nreplay 2-a\noff\n'))
    def test_replay_invalid_two_ranges(self):
        """tests that the robot replays within the given range values correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        output = fake_out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 1 steps.
 > BMO now at position (0,1).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,3).
BMO: What must I do next?  > BMO moved forward by 3 steps.
 > BMO now at position (0,6).
BMO: What must I do next?  > BMO moved forward by 4 steps.
 > BMO now at position (0,10).
BMO: What must I do next?  > BMO moved forward by 5 steps.
 > BMO now at position (0,15).
BMO: What must I do next? BMO: Sorry, I did not understand 'replay 2-a'.
BMO: What must I do next? BMO: Shutting down..""", output)

    @patch("sys.stdin", StringIO('BMO\nforward 1\nforward 2\nforward 3\nreplay 2 reversed\noff\n'))
    def test_replay_range_reversed(self):
        """tests that the robot replays within the reversed range correctly"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        output = fake_out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BMO: Hello kiddo!
BMO: What must I do next?  > BMO moved forward by 1 steps.
 > BMO now at position (0,1).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,3).
BMO: What must I do next?  > BMO moved forward by 3 steps.
 > BMO now at position (0,6).
BMO: What must I do next?  > BMO moved forward by 2 steps.
 > BMO now at position (0,8).
 > BMO moved forward by 1 steps.
 > BMO now at position (0,9).
 > BMO replayed 2 commands in reverse.
 > BMO now at position (0,9).
BMO: What must I do next? BMO: Shutting down..""", output)

    @patch("sys.stdin", StringIO("BMO\nforward 1\noff\n"))
    def test_obstacles(self):
        """tests that the obstacle's coordinates are printed"""
        with patch('sys.stdout', new = StringIO()) as fake_out:
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()
        self.assertEqual(fake_out.getvalue(), """What do you want to name your robot? BMO: Hello kiddo!
There are some obstacles:
- At position 1,1 (to 5,5)
BMO: What must I do next?  > BMO moved forward by 1 steps.
 > BMO now at position (0,1).
BMO: What must I do next? BMO: Shutting down..
""")


if __name__ == "__main__":
    unittest.main()