import unittest
from Jarvis import Jarvis
from utilities import textParser

class ParseDefualtNumberList(unittest.TestCase):
    def test_default_numparselist(self):
        """Contract: test that default_numparselist returns a list
            of default words that can be used by parse_number to parse specified 
            words to numerals
        """

        parselist = textParser.default_numparselist()
        parsekeys = parselist.keys()
        first_key = parsekeys[0]
        self.assertEqual('and', first_key)

        #Test that the list can be used as a parselist in parse_number
        #with a key from the list
        number_input = first_key
        skip, parsed_input = textParser.parse_number(number_input, numwords=parselist)
        self.assertEqual(1, skip)
        self.assertEqual(0, parsed_input)

    def test_parse_number_valid(self):
        """Contract: test a single numeral string gets parsed to its int value
        """
        number_input = "24"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(24, parsed_input)
        self.assertEqual(1, skip)

        number_input = "four"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(4, parsed_input)
        self.assertEqual(1, skip)

    def test_parse_number_add_scale(self):
        """Contract: test that a number gets scaled e.g '5 hundred' -> 500
            Chaining scales > 100 does not yield same results (feature?)
        """
        number_input = "19 hundred thousand"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(3, skip)
        self.assertEqual(19*100*1000, parsed_input)


        number_input = "19 thousand thousand"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(3, skip)
        self.assertEqual(19*1000+1000, parsed_input)

    def test_comma_separated_input(self):
        """Contract: test input separated by - and ,
            elements separated by - treated within () and evaluated first
            before adding scales
            elements separated by ', ' is the same as a whitespace
        """
        number_input = "5-5, 5-5, hundred, million"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(4, skip)
        self.assertEqual(((5+5)+(5+5))*100*1000000, parsed_input)

    def test_invalid_input(self):
        """Contract: test combinations of invalid input
            stops parsing when it encounters an invalid string
            and returns everything it has parsed up to that point
        """

        #the empty string
        number_input = ""
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(0, 0)
        self.assertEqual(0, parsed_input)

        #start with invalid element
        number_input = "gfdgdf 5"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(0, 0)
        self.assertEqual(0, parsed_input)

        #valid element followed by an invalid element
        number_input = "5 asdas"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(1, skip)
        self.assertEqual(5, parsed_input)

        #an invalid element between two valid
        number_input = "5 xmk2ask., 5"
        skip, parsed_input = textParser.parse_number(number_input)
        self.assertEqual(1, skip)
        self.assertEqual(5, parsed_input)

    def test_non_default_numwords(self):
        """Contract: Test giving a Non default parse list as second parameter
            and parsing something from that list, words not in list should yield 0
        """
        #non default words that can be parsed
        parselist = {}
        parselist["OnE"] = (1, 5656)

        #a word in the given list
        number_input = "OnE"
        skip, parsed_input = textParser.parse_number(number_input, numwords=parselist)
        self.assertEqual(1, skip)
        self.assertEqual(5656, parsed_input)

        #a word not in the given list -> 0
        number_input = "one"
        skip, parsed_input = textParser.parse_number(number_input, numwords=parselist)
        self.assertEqual(0, skip)
        self.assertEqual(0, parsed_input)

