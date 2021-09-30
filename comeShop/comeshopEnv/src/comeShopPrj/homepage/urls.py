from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage, name="homepage"),
    path('addProduct/',views.addproduct, name="addProduct"),
    #  path('productList/',views.productList,name="product-list"),
    path('product_show/<int:item_id>', views.productShow, name="product_show"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login")
]