from django import template

register = template.Library()

@register.filter(name='price_currency')
def price_currency(number):
    return "BDT "+str(number)



@register.filter(name='multiplication')
def multiplication(number , number1):
    return number * number1

