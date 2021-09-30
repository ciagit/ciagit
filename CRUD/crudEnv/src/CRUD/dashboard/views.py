from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import CustomerForm,CreateUserForm
from .filters import CustomerFilter
def homepage(request):
    cusData = Customer.objects.all()
    myFilter = CustomerFilter(request.GET,queryset=cusData)
    cusData = myFilter.qs
    context = {'cus':cusData,'myFilter':myFilter}
    return render(request,'dashboard/landing.html',context)
def customerProfile(request,pk):
    cusProfile=Customer.objects.filter(id=pk)
    context = {'cusPro':cusProfile}
    return render(request,'dashboard/customerPro.html',context)
def addCustomer(request):
    form=CustomerForm()
    if request.method=='POST':
        print(request.POST)
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'dashboard/addCustomer.html',context)

def updateCustomer(request,pk):
    cus=Customer.objects.get(id=pk)
    form=CustomerForm(instance=cus)
    if request.method=='POST':
        form=CustomerForm(request.POST,instance=cus)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'dashboard/addCustomer.html',context)

def deleteCustomer(request,pk):
    cus=Customer.objects.get(id=pk)
    if request.method=='POST':
        cus.delete()
        return redirect('/')
    context={'item':cus}
    return render(request,'dashboard/deleteCus.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)#save the data
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account created succesfully'+user)
            return redirect('login')
    context={'form':form}
    return render(request,'dashboard/register.html',context)


def loginPage(request):
    if request.method=='POST':
        useremail = request.POST.get('username')
        userpassword = request.POST.get('password')

        user = authenticate(request, username=useremail,password=userpassword)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or password incorrect')
    context={}
    return render(request,'dashboard/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

