from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from products.models import Product,Cart,CartItem
from django.contrib import messages




#function for listing all products
def Products_List(request):

	if request:
		products=Product.objects.all()
		if products:
			context={"products":products}
	return render(request, "product_list.html", context)


#function for all detail of a product
def Products_Detail(request,id):
	if request:
		product=get_object_or_404(Product, id=id)
		if product:
			context={"product":product}
	return render(request, "product_detail.html", context)



#function of product adding into a cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    if product.stock <= 0:
        messages.error(request, 'Product is out of stock.')
    else:
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if not item_created:
            if cart_item.quantity < product.stock:
                cart_item.quantity += 1
                cart_item.save()
                messages.success(request, 'Product added to cart successfully.')
            else:
                messages.error(request, 'Reached maximum available quantity for this product.')
        else:
            messages.success(request, 'Product added to cart successfully.')

    
    return redirect('detail', id=product.id)