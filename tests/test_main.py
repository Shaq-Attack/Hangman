import unittest
import hangman
from io import StringIO
from unittest.mock import patch

class Test_Hangman(unittest.TestCase):

    @patch('sys.stdin', StringIO("e\n"))
    def test_step1_select_difficulty_easy(self):
        with patch(('sys.stdout'), new = StringIO()):            
            output = hangman.select_difficulty()
            self.assertEqual("Easy.txt", output)
    

    @patch('sys.stdin', StringIO("Medium\n"))
    def test_step1_select_difficulty_medium_full_word(self):
        with patch(('sys.stdout'), new = StringIO()):            
            output = hangman.select_difficulty()
            self.assertEqual("Medium.txt", output)
    

    @patch('sys.stdin', StringIO("y\nh"))
    def test_step1_select_difficulty_wrong_then_hard(self):
        with patch(('sys.stdout'), new = StringIO()):            
            output = hangman.select_difficulty()
            self.assertEqual("Hard.txt", output)


    def test_step2_read_file_nonexistant(self):
        output = hangman.read_file('testing.txt')
        self.assertEqual(['Failed', 'Malfunction', 'blunder'], output)
    

    def test_step2_read_file_exists(self):
        output = hangman.read_file('test.txt')
        self.assertEqual(['Success\n', 'Success'], output)


    def test_step3_choose_word(self):
        words_list = hangman.read_file('test.txt')
        output = hangman.choose_word(words_list)
        self.assertEqual('Success', output)


    def test_step4_hide_chars(self):
        count = 0
        output = hangman.hide_chars('abcd')

        for x in output:
            if x == '_':
                count += 1
        self.assertEqual(3, count)

    
    def test_step5_valid_guess_invalid(self):
        output1 = hangman.valid_guess('0')
        output2 = hangman.valid_guess(1)
        output3 = hangman.valid_guess('$')
        output4 = hangman.valid_guess('abc')
        
        self.assertFalse(output1)
        self.assertFalse(output2)
        self.assertFalse(output3)
        self.assertFalse(output4)

    
    def test_step5_valid_guess_valid(self):
        output1 = hangman.valid_guess('A')
        output2 = hangman.valid_guess('a')
        output3 = hangman.valid_guess('Z')
        output4 = hangman.valid_guess('z')

        self.assertTrue(output1)
        self.assertTrue(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)


    def test_step6_guessed_chars_list(self):
        hangman.add_guessed('abcd')
        self.assertEqual(['a', 'b', 'c', 'd'], hangman.guessed_chars)