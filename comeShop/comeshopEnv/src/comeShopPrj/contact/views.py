from django.shortcuts import render
from .models import Messages
# Create your views here.
def forms(request):
    if request.method == "POST":
        name= request.POST.get('f_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact_no')
        message =request.POST.get('msg')
        new_message = Messages(name,email,contact,message)
        new_message.save()
    return render(request,'contact/contact.html')

def c_list(request):
    new_message = Messages.objects.all()
    data = {'newMessage':new_message}
    return render(request,'contact/contact_list.html', data)