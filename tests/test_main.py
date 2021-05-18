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


    @patch('sys.stdin', StringIO("abc\n"))
    def test_step5_get_guess(self):
        with patch(('sys.stdout'), new = StringIO()):  
            output = hangman.get_guess("xyz")
            self.assertEqual("abc", output)


    def test_step6_validate_guess_invalid(self):
        output1 = hangman.validate_guess('0')
        output2 = hangman.validate_guess(1)
        output3 = hangman.validate_guess('$')
        output4 = hangman.validate_guess('abc')
        
        self.assertFalse(output1)
        self.assertFalse(output2)
        self.assertFalse(output3)
        self.assertFalse(output4)

    
    def test_step6_validate_guess_valid(self):
        output1 = hangman.validate_guess('A')
        output2 = hangman.validate_guess('a')
        output3 = hangman.validate_guess('Z')
        output4 = hangman.validate_guess('z')

        self.assertTrue(output1)
        self.assertTrue(output2)
        self.assertTrue(output3)
        self.assertTrue(output4)


    def test_step7_guessed_chars_list(self):
        hangman.add_guessed('a')
        hangman.add_guessed('b')
        hangman.add_guessed('c')
        hangman.add_guessed('d')

        self.assertEqual(['a', 'b', 'c', 'd'], hangman.guessed_chars)


    def test_step8_fill_char(self):
        self.assertEqual('ab_', hangman.fill_in_char('abc', 'a__', 'b'))
        self.assertEqual('a__', hangman.fill_in_char('abc', 'a__', 'a'))
        self.assertEqual('a__', hangman.fill_in_char('abc', 'a__', 'd'))

    
    def test_step9_draw_hangman(self):
            self.assertEqual('\n/----\n|\n|\n|\n|\n_______', 
                            hangman.draw_figure(4))
            self.assertEqual('\n/----\n|   0\n|\n|\n|\n_______', 
                            hangman.draw_figure(3))
            self.assertEqual('\n/----\n|   0\n|   |\n|   |\n|\n_______', 
                            hangman.draw_figure(2))
            self.assertEqual('\n/----\n|   0\n|  /|\\\n|   |\n|\n_______', 
                            hangman.draw_figure(1))
            self.assertEqual('\n/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______', 
                            hangman.draw_figure(0))