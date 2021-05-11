import unittest
from app.parser import parse

class ParserTest(unittest.TestCase):

    def test_fail_without_url(self):
        with self.assertRaises(SystemExit):
            parse("--output /".split())
    
    def test_fail_without_output(self):
        with self.assertRaises(SystemExit):
            parse("--url www.example.com".split())
    
    def test_username_is_read(self):
        args = parse("-u www.example.com -o /tmp/1.txt -l foo".split())
        self.assertEqual(args['login'], "foo")
    
    def test_password_is_read(self):
        args = parse("-u www.example.com -o /tmp/1.txt -l foo -p bar".split())
        self.assertEqual(args['password'], "bar")