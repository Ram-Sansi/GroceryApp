from django.contrib import messages
from django.shortcuts import *
from django.views import View
from .models import *


# Create your views here.

def client_login(request):
    return render(request, 'customer/client_login.html')


def add_client(request):
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    password = request.POST['password']
    dob = request.POST['dob']
    address = request.POST['address']
    city = request.POST['city']

    client = Client(name=name, email=email, mobile=mobile, password=password, dob=dob, address=address,
                    city=city)
    client.save()
    messages.warning(request, name + 'Has been registered. Please login now...')
    return redirect('client_login')


def login(request):
    if 'client' in request.session:
        return redirect('dashboard')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user_login = Client.objects.filter(email=email, password=password)
        if len(user_login) == 0:
            messages.warning(request, "Invalid Username Or Password")
        else:
            messages.success(request, "Login Successful!")
            d = {
                'id': user_login[0].id,
                'email': email,
                'name': user_login[0].name,
                'mobile': user_login[0].mobile
            }
            request.session['client'] = d
        return redirect('client_login')


def client_logout(request):
    del request.session['client']
    messages.success(request, 'User has been logged out')
    return redirect('client_login')


def index(request):
    return render(request, 'customer/index.html')
