import unittest
from utilities import textParser
from datetime import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import re


class ParseDateTest(unittest.TestCase):

    def test_parse_date_1(self):
        #contract: verifies that a datetime object is returned in idx=1 of returned obj with the 
        #inputed string's year month and day
        input_string = "2017-03-12"
        res = textParser.parse_date(input_string)
        self.assertEqual(1, res[0]) #when split is applied on input string argument
        self.assertEqual(2017, res[1].year)
        self.assertEqual(3, res[1].month)
        self.assertEqual(12, res[1].day)

    def test_parse_date_2(self):
        #contract: verifies that a datetime object is returned in idx=1 of returned obj  
        #and that year of that is +1 of current year when input is 'in one year....'
        current_year = dt.now().date().year
        current_month = dt.now().date().month
        current_day = dt.now().date().day
        input_string = "in one year and zero month and zero day and zero hour"
        res = textParser.parse_date(input_string)
        self.assertEqual((current_year+1), res[1].year)
        self.assertEqual(current_month, res[1].month)
        self.assertEqual(current_day, res[1].day)


if __name__ == '__main__':
  unittest.main()