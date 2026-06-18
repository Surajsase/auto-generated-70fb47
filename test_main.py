import unittest
from unittest.mock import patch
from io import StringIO
import sys
from main import hello

class TestHelloFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_hello(self, mock_stdout):
        hello()
        self.assertEqual(mock_stdout.getvalue(), 'hi\n')

if __name__ == '__main__':
    unittest.main()