import unittest
class ordersTest(unittest.TestCase):
    def test_createOrder(self):
        self.product = "Black shirt"
        self.customer = "Customer 1"
        self.quantity = 5
        self.price = 500
        self.address = "Dhanmondi,Dhaka"
        self.phone = "12345678876"
        self.status = "Pending"

    def test_placeOrder(self):
        self.save()
