import unittest
class productTest(unittest.TestCase):
    def test_createProduct(self):
        self.name = "Black shirt"
        self.price = 500
        self.category = "Men"
        self.description = "Cotton casual shirt"

    def test_str__(self):
        return self.name