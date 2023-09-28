from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(kulfi, cart):
    keys = cart.keys()
    for id in keys:
        if id and id!='null' and int(id) == kulfi.id:
            return True
    return False

@register.filter(name="cart_quantity")
def cart_quantity(kulfi, cart):
    keys = cart.keys()
    for id in keys:
        if id and id!='null' and int(id) == kulfi.id:
            return cart.get(id)
    return 0