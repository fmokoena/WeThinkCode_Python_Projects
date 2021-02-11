import unittest
import word_processor

class MyTestCase(unittest.TestCase):

    def test_converts_to_lowercase(self):
        """tests if the convert_to_word_list function converts a string into a list of lowercased words"""
        result = word_processor.convert_to_word_list("ONCE A LifeTime Twice A DAY")
        expect = ['once', 'a', 'lifetime', 'twice', 'a', 'day']
        self.assertEqual(expect,result )


    def test_return_words_over_length(self):
        """tests that the word_longer_than function returns words that are longer than the given length"""
        result = word_processor.words_longer_than(6,"once a lifetime twice a day")
        expect = ['lifetime']
        self.assertEqual(expect,result )


    def test_returns_word_lengths(self):
        """tests that the words_length_map function returns a dictionary with the lengths of every word and how many times that given length occurs"""
        result = word_processor.words_lengths_map("once a lifetime twice a day")
        expect = {1: 2, 3: 1, 4: 1, 5: 1, 8: 1}
        self.assertEqual(expect, result)


    def test_letter_count(self):
        """tests that the letter_count_map function returns a dictionary containing all the letters of the alphabet and how many times each letter occurs in a string"""
        result = word_processor.letters_count_map("once a lifetime twice a day")
        expect = {'a': 3, 'b': 0, 'c': 2, 'd': 1, 'e': 4, 'f': 1, 'g': 0, 'h': 0, 'i': 3, 'j': 0, 'k': 0, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 2, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 1, 'z': 0}
        self.assertEqual(expect, result)


    def test_highest_occurence(self):
        """tests that the function returns the most frequently occuring letter in a string"""
        result = word_processor.most_used_character("once a lifetime twice a day")
        expect = 'e'
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()