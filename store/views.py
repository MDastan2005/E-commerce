from django.shortcuts import render

# Create your views here.
def store(request):
	context = {'rows': [['header1', 'header2', 'header3'],
					    ['header4', 'header5', 'header6']],
			   'cart_total': 0}
	return render(request, "store/store.html", context);


def cart(request):
	context = {'cart_total': 0}
	return render(request, "store/cart.html", context);


def checkout(request):
	context = {}
	return render(request, "store/checkout.html", context);
