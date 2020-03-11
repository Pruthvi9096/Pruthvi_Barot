from django.urls import path
from . import views

urlpatterns = [
    path("",views.display_all_products,name="display_all_products"),
    path("create_product/",views.create_product,name="product_create"),
    path("create_category/",views.create_category,name="category_create")
]