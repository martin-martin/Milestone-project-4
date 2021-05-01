from django.shortcuts import render, redirect
from store.models import Product


def cart(request):
    if request.method == "POST":
        form_data = request.POST
        id = form_data["id"]
        product = Product.objects.get(id=id)

        try:
            request.session.get("cart_items", [])

            cart_item = []

            price = product.product_price
            price *= 0.25

            item = {
                "name": product.product_name,
                "description": product.product_description,
                "price": price
            }

            cart_item.append(item)

            request.session["cart_items"] += [cart_item]

        except KeyError:
            print("Key not found")

        return redirect("store")

    else:

        cart_items = request.session.get("cart_items", [])
        context = {
            "cart_items": cart_items
        }

        return render(request, "cart/cart.html", context)
