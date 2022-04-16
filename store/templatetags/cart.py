from django import template

register = template.Library()

@register.filter(name='in_cart')
def in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='quantity')
def quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name='total_price')
def total_price(product  , cart):
    return product.price * quantity(product , cart)


@register.filter(name='cart_total_price')
def cart_total_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += total_price(p , cart)

    return sum
    