from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard", dashboard,  name ="dashboard"),
    path("user_login", user_login, name="user_login"),
    path("add_user", add_user, name="add_user"),
    path("login", login, name="login"),
    path("user_logout", user_logout, name='user_logout'),

    # category url
    path("addcategory", category.as_view(), name="addcategory"),
    path("viewcategory", viewcategory, name="viewcategory"),

    # products url

    path("products", products.as_view(), name="products"),
    path("viewproducts", viewProducts, name='viewproducts'),
    path("update_product/<int:prodid>", update_product, name='update_product'),
    path("delete_product/<int:id>", delete_product, name='delete_product'),
    path("saveupdate/<int:id>", saveupdate, name='saveupdate'),

]
