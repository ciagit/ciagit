from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('cus_pro/<str:pk>',views.customerProfile, name = "customer_profile"),
    path('addcustomer/',views.addCustomer,name="addcustomer"),
    path('updateCustomer/<str:pk>',views.updateCustomer,name="updateCustomer"),
    path('deleteCustomer/<str:pk>',views.deleteCustomer,name="deleteCustomer"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('register/',views.register,name="register"),
]