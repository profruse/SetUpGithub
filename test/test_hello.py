import unittest
from hello_source import hello


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("Hello, CIS 189!", hello.hello_message())


if __name__ == '__main__':
    unittest.main()

# comment
