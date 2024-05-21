import unittest
from auto_suggest import auto_suggest

class AdditionalTestCases(unittest.TestCase):

    # Test Cases to Validate the No. of i/p words
    def test_more_than_5_words(self):
        input_words = ['bbbbb', 'bbb', 'bb', 'b', 'bbbbb','auekfh']
        search_pattern = 'bbb'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['bbbbb', 'bbb', 'bbbbb'])

    def test_less_than_5_words(self):
        input_words = ['bbbbb', 'bbb']
        search_pattern = 'abc'
        self.assertEqual(auto_suggest(input_words, search_pattern), [])

    def test_exactly_5_words(self):
        input_words = ['take', 'make', 'check', 'ack', 'rake']
        search_pattern = 'ck'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['check', 'ack'])

    # Test Cases to Validate Regex functionality

    def test_matching_prefix(self):
        input_words = ['premier', 'premonition', 'prestige', 'pretext', 'prevaricate']
        search_pattern = 'pre*'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['premier', 'premonition', 'prestige', 'pretext', 'prevaricate'])

    def test_matching_suffix_additional(self):
        input_words = ['discretion', 'extension', 'inclusion', 'permission', 'rejection']
        search_pattern = '*sion'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['extension', 'inclusion', 'permission'])

    def test_pattern_on_on_both_ends(self):
        input_words = ['start', 'stark', 'stack', 'slack', 'starkey']
        search_pattern = '*ta*'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['start', 'stark', 'stack', 'starkey'])

    def test_matches_part(self):
        input_words = ['vwxyz', 'klmnop', 'efghij', 'abcdel', 'pqrst']
        search_pattern = 'lm'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['klmnop'])

    def test_matches_pattern(self):
        input_words = ['appla', 'applz', 'apple', 'apples', 'applet']
        search_pattern = 'app*e'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['apple'])

    def test_no_match(self):
        input_words = ['zebra', 'lion', 'tiger', 'elephant', 'giraffe']
        search_pattern = 'monkey'
        self.assertEqual(auto_suggest(input_words, search_pattern), [])


    def test_special_characters(self):
        input_words = ['c#', 'c++', 'c@', 'c&', 'c$']
        search_pattern = 'c#'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['c#'])


    def test_mixed_case_sensitivity(self):
        input_words = ['Rebate', 'Create', 'PerforAte', 'Navigate', 'Operate']
        search_pattern = 'rate'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['PerforAte'])

    def test_digits_and_letters(self):
        input_words = ['a2', 'b3', 'c1', 'd4', 'e1']
        search_pattern = '1'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['c1', 'e1'])

    def test_overlapping_matches(self):
        input_words = ['inn', 'ann', 'sonnet', 'tonnage', 'connotation']
        search_pattern = 'nn'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['inn', 'ann', 'sonnet', 'tonnage', 'connotation'])

    def test_empty_search_pattern_additional(self):
        input_words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
        search_pattern = ''
        self.assertEqual(auto_suggest(input_words, search_pattern), ['apple', 'banana', 'orange', 'grape', 'kiwi'])

    def test_matching_entire_word(self):
        input_words = ['yes', 'no', 'maybe', 'sometimes', 'never']
        search_pattern = 'yes'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['yes'])

    def test_complex_pattern(self):
        input_words = ['abc123', '123abc', 'a1b2c3', '3c2b1a', '1c2a3']
        search_pattern = '1*3'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['1b2c3'])

    def test_substring_not_at_start_or_end(self):
        input_words = ['abracadabra', 'alakazam', 'hocuspocus', 'prestidigitation', 'magic']
        search_pattern = 'abra'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['abracadabra'])

    def test_repeated_characters(self):
        input_words = ['bbbbb', 'bbb', 'bb', 'b', 'bbbbb']
        search_pattern = 'bbb'
        self.assertEqual(auto_suggest(input_words, search_pattern), ['bbbbb', 'bbb', 'bbbbb'])
    

if __name__ == '__main__':
    unittest.main()
