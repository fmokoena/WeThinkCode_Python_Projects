import unittest
import mastermind
from unittest.mock import patch
from io import StringIO

class KnownValues(unittest.TestCase):
    def test_create_code(self):
        """Tests that the create_code function generates a random 4 digit code"""
        result = False
        expected = True
        numb = [1,2,3,4,5,6,7,8]
        for  i in range (0,100):
            code = mastermind.create_code()
            if len(code) == 4:
                for j in range(4):
                    if code[j] in numb:
                        result = True
                    else:
                        result = False
                        break
            else:
                break
        self.assertEqual(expected, result)

    def test_check_correctness(self):
        """Tests tht the check_correctness function checks the correctness of the players input and returns the appropriate boolean """
        with patch("sys.stdout", new = StringIO()) as fakeout:
            mastermind.check_correctness(11, 4)
        self.assertEqual(fakeout.getvalue() , "Congratulations! You are a codebreaker!\n")
        with patch("sys.stdout", new = StringIO()) as fakeout:
            mastermind.check_correctness(11, 0)
        self.assertEqual(fakeout.getvalue() , "Turns left: 0\n")

    @patch("sys.stdin", StringIO("1\n12\n123\n1234\n"))
    def test_get_answer_input(self):
        """Tests that the get_answer_input function only takes in 4 digit intergers"""
        with patch("sys.stdout", new = StringIO()) as fakeout:
            mastermind.get_answer_input()
        self.assertEqual(fakeout.getvalue(), """Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: """)
        
if __name__ =='__main__':
    unittest.main()
