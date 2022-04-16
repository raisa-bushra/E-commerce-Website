import unittest

class categoryTest(unittest.TestCase):
    name = "Men"

    def test__str__(self):
        return self.name
