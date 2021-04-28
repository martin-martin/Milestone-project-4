from django.shortcuts import render
from .models import Product


def store(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "store/store.html", context)


def product_details(request, product_id):

    ind_product = Product.objects.get(id=product_id)

    context = {
        "ind_product": ind_product
    }
    return render(request, "store/product_details.html", context)
