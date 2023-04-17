from django.contrib import messages
from django.shortcuts import *
from django.views import View
from .models import *
from .forms import *


# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')


def user_login(request):
    return render(request, 'user_login.html')


def add_user(request):
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    password = request.POST['password']
    shop_name = request.POST['shop_name']
    address = request.POST['address']
    city = request.POST['city']

    user = Merchant(name=name, email=email, mobile=mobile, password=password, shop_name=shop_name, address=address,
                    city=city)
    user.save()
    messages.warning(request, name + 'Has been registered. Please login now...')
    return redirect('user_login')


def login(request):
    if 'user' in request.session:
        return redirect('dashboard')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user_login = Merchant.objects.filter(email=email, password=password)
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
            request.session['user'] = d
        return redirect('user_login')


def user_logout(request):
    del request.session['user']
    messages.success(request, 'User has been logged out')
    return redirect('user_login')


class category(View):
    def get(self, request):
        if 'user' in request.session:
            form = CategoryForm()
            return render(request, "addcategory.html", {'form': form, 'pageTitle': Category})
        else:
            return redirect('user_login')

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been added')

        else:
            messages.success(request, 'Invalid Data')
        return redirect('addcategory')


def viewcategory(request):
    if 'user' in request.session:
        viewcategory = Category.objects.all()

        return render(request, 'viewCategory.html',
                      {'pageTitle': viewcategory, 'viewcategory': viewcategory})
    else:
        return redirect('user_login')


class products(View):
    def get(self, request):
        if 'user' in request.session:
            forms = ProductsForm()
            return render(request, "products.html", {'forms': forms, 'pageTitle': Products})
        else:
            return redirect('user_login')

    def post(self, request):
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():

            obj = form.save(commit=False)
            obj.Merchant_id = request.session['user']['id']
            form.save()
            messages.success(request, 'Product has been added')

        else:
            messages.success(request, 'Invalid Data')
        return redirect('products')


def viewProducts(request):
    if 'user' in request.session:
        viewcategory = Category.objects.all()
        viewproducts = Products.objects.all()

        return render(request, 'viewProducts.html',
                      {'pageTitle': viewProducts, 'viewproducts': viewproducts, 'viewcategory': viewcategory})
    else:
        return redirect('user_login')


def update_product(request, prodid):
    prod = Products.objects.get(id=prodid)
    allcat = Category.objects.all()
    return render(request, 'updateitems.html', {'product': prod, 'category': allcat})


def saveupdate(request, id):
    if request.method == "POST":
        prod = Products.objects.get(id=id)
        prod.name = request.POST["name"]
        prod.description = request.POST["description"]
        prod.price = request.POST["price"]
        prod.discount = request.POST["discount"]
        if "image" in request.FILES:
            prod.image = request.FILES["image"]
        prod.save()
        return redirect("viewproducts")


def delete_product(request, id):
    prod = Products.objects.get(id=id)
    prod.delete()
    return redirect('viewproducts')
