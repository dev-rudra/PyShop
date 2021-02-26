from django.contrib import admin
from .models import Product, Offer


admin.site.register(Offer)


# from above one line code we got the specific admin so we need to customize that
# to solve the above issue need to create new class and need to pass as a parameter
# admin.ModelAdmin in the class.
# in the class body we need to overwrite the default setting


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# after defining the above setting we need to pass this class as a second parameter
# of register method

admin.site.register(Product, ProductAdmin)


