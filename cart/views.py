from django.shortcuts import render, redirect
from store.models import Product


def cart(request):
    if request.method == "POST":
        form_data = request.POST
        id = form_data["id"]
        product = Product.objects.get(id=id)

        if "cart" not in request.session:
            request.session["cart"] = []

        cart = request.session["cart"]

        request.session["product_name"] = product.product_name
        product_name = request.session["product_name"]
        cart += [product_name]

        request.session["product_description"] = product.product_description
        product_description = request.session["product_description"]
        cart += [product_description]

        request.session["product_price"] = product.product_price
        product_price = request.session["product_price"]
        cart += [product_price]

        
        for i in cart:
            print(i)

    return redirect("store")
