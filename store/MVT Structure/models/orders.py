
from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    def createOrder(self):
        self.product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
        self.customer = models.ForeignKey(Customer,
                                     on_delete=models.CASCADE)
        self.quantity = models.IntegerField(default=1)
        self.price = models.IntegerField()
        self.address = models.CharField(max_length=50, default='', blank=True)
        self.phone = models.CharField(max_length=50, default='', blank=True)
        self.date = models.DateField(default=datetime.datetime.today)
        self.status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

