import unittest
import sys
import re
import packages.translate as translate

from Jarvis import Jarvis
from StringIO import StringIO

class TranslateTest(unittest.TestCase):

    def test_generic_query(self):
        """ contract:
            The translate.main function shall return a correct translation from
            english to swedish, as per the Google-translate standard.
        """
        # set up query parameters and oracle for assertion
        params = ['english', 'swedish', 'my name is jarvis']
        oracle = u'jag heter jarvis'

        # hijack the file descriptors for simulating user input/output
        sys.stdin = StringIO(''.join(map(lambda p: '%s\n' % p, params)))
        sys.stdout = output = StringIO()

        translate.main(Jarvis())

        # extract the translation from stdout
        sys.stdout  = sys.__stdout__
        pattern = r'\[\w+\] ((?:.+ ?)*)'
        translation = re.findall(pattern, output.getvalue().split('\n')[8])

        if (translation):
            self.assertEqual(oracle, translation[0])
        else:
            self.fail('There was no matching output after translation. If the format of the output has changed, the regex used in the test may be obsolete.')

    def tearDown(self):
        """ return file descriptors to their absolute origin """
        sys.stdin   = sys.__stdin__
        sys.stdout  = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
