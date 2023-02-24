from django.shortcuts import render
from .models import Product, Order, OrderItem, Customer

# Create your views here.


def get_order(request) -> tuple[Order | dict, OrderItem | list]:
    """
    Function to get order and orderitem objects from user if authenticated.
    Else return similar duplicates.
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, complete=False)
        ordered_items = order.orderitem_set.all()
    else:
        ordered_items = []
        order = {'get_item_number': 0, 'get_total_price': 0}
    return (order, ordered_items)


def store(request):
    products = Product.objects.all()
    order, _ = get_order(request)
    context = {'products': products,
               'order': order}
    return render(request, "store/store.html", context)


def cart(request):
    order, ordered_items = get_order(request)
    context = {'ordered_items': ordered_items,
               'order': order}
    return render(request, "store/cart.html", context)


def checkout(request):
    order, ordered_items = get_order(request)
    context = {'ordered_items': ordered_items,
               'order': order}
    return render(request, "store/checkout.html", context)
