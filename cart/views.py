from django.shortcuts import render, redirect
from store.models import Product


def cart(request):
    if request.method == "POST":
        form_data = request.POST
        id = form_data["id"]
        product = Product.objects.get(id=id)


        request.session.get("cart_items", [])

        
        cart_items = []

        cart_items.append(product.product_name)
        cart_items.append(product.product_description)
        cart_items.append(product.product_price)

        request.session["cart_items"] += [cart_items]

        print(request.session["cart_items"])

        return redirect("store")
        

    else:

        
        return render(request, "cart/cart.html")
