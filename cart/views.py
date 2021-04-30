from django.shortcuts import render, redirect
from store.models import Product


def cart(request):
    if request.method == "POST":
        form_data = request.POST
        id = form_data["id"]
        product = Product.objects.get(id=id)

        cart_items = request.session.get("cart_items", []) # On any python dicts, you can use the get("key", default)

        item_exists = False
        for v in cart_items:
            if v.id == product.id:
                item_exists = True
                break
        
        if item_exists:
            cart_items.append(product)

        request.session["cart_items"] = cart_items
        context = {
            "cart_items": cart_items
        }

        

        return redirect("store")

    else:

        cart_items = request.session.get("cart_items", [])
        
        context = {
            "cart_items": cart_items
        }


        return render(request, "cart/cart.html", context)
