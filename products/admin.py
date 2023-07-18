from django.contrib import admin

# Register your models here.


from .models import Category, Product, Tag, Cart, CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(CartItem)