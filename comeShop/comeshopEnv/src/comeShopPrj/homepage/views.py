from django.shortcuts import render,redirect
from django.contrib import messages
from .models import products
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def homepage(request):
    product = products.objects.all()
    data = {'products':product}
    return render(request,'homepage/landingPage.html', data)

def addproduct(request):
    if request.method == "POST":
        name=request.POST.get("p_name")
        price = request.POST.get("p_price")
        des = request.POST.get("p_des")
        image = request.FILES.get("p_image")
        new_product= products(name,price,des,image)
        new_product.save()
    return render(request,'homepage/addProduct.html')

def productShow(request,item_id):
    product = products.objects.all().filter(pk=item_id)
    print(product)
    return render(request,'homepage/productlist.html',{'product':product})

def login(request):
    if request.method == "POST":
        useremail = request.POST.get("email")
        userpw = request.POST.get("password")
        user = authenticate(request, username=useremail,password=userpw)
        print(user)
        if user is not None: # user takes the value given by the loginform
            user2 = User.objects.get(username=useremail)
            print(user2)
            content={'user':user2}
            return redirect('homepage',content)
        else:
            return render(request,'homepage/login.html',{"msg":"please try again"})
    return render(request,'homepage/login.html',{"msg":""})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cPassword = request.POST.get("confirm_password")
        if password != cPassword:
            messages.success(request,'password incorrect')
            return redirect(register)
        else:
            if authenticate(username=username,password= password) is None:
               user= User.objects.create_user(username,email,password)
               user.save()
               msg="welcome"
               return render(request,'homepage/landingPage.html',{"msg":msg})
            else:
                msg="User exist"
                return render(request,'homepage/register.html',{"msg":msg})
    return render(request,'homepage/register.html')