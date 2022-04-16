import unittest

class CustomerTest(unittest.TestCase):
    def test_createCustomer(self):
        CustomerTest.first_name = "customer1"
        CustomerTest.email = "cutomer1@gmail.com"
        CustomerTest.password ="123456"

    def test_register(self):
        return self
    def test_isExists(self):
        if self.email == "cutomer1@gmail.com":
            return True

        return False
