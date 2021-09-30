from django.urls import path
from . import views
urlpatterns = [
    path('',views.forms,name="contact_form"),
    path('contact-list/',views.c_list)
]