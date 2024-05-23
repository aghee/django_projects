from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("login/",views.loginpage,name="loginuser"),
    path("logout/",views.logoutuser,name="logoutuser"),
    path("register/",views.registerpage,name="registeruser"),
    path("user/",views.userpage,name="user"),
    path("products/",views.product,name="product"),
    path("customer/<str:pk>/",views.customer,name="customer"),
    path("create_order/<str:pk>/",views.create_order,name="create_order"),
    path("update_order/<str:pk>/",views.update_order,name="update_order"),
    path("delete_order/<str:pk>/",views.delete_order,name="delete_order"),
    path("create_customer/",views.create_customer,name="create_customer"),
    path("update_customer/<str:pk>/",views.update_customer,name="update_customer"),
    path("delete_customer/<str:pk>/",views.delete_customer,name="delete_customer"),
    # path("user/",views.userpage,name="userpage"),   
    # path("status/",views.status_count,name="status"),
]