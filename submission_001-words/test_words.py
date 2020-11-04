import word_processor
import unittest

class MyTestCase(unittest.TestCase):
    words = 'These are indeed interesting, an obvious understatement, times. What say you?'
    def test_Transform_to_lowercase(self):
        words = word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you'],words)

    def test_Filter_words_on_length(self):
        words = word_processor.words_longer_than(10, 'These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['interesting','understatement'],words)
    
    def test_Spread_of_word_lengths(self):
        word_lengths = word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual({2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1},word_lengths)
    
    def test_Count_the_letters(self):
        char_count = word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual({'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0},char_count)

    def test_Reduce_to_highest_occurrence(self):
        popular_char = word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual('e',popular_char)