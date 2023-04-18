from django.urls import path
from .views import *

urlpatterns = [

    # user urls

    path("", index, name="index"),
    path("client_login", client_login, name="client_login"),
    path("add_client", add_client, name="add_client"),
    path("login", login, name="login"),
    path("client_logout", client_logout, name="client_logout"),
    path("view", view, name="view"),
    path("viewProductByCategory/<int:id>", viewProductByCategory, name="viewProductByCategory"),
    path("searchproducts", searchproducts, name="searchproducts"),
]
