from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path("reset_password/",auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="password_reset"),
    path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path("reset_password_complete",auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),name="password_reset_complete"),
    # path("user/",views.userpage,name="userpage"),   
    # path("status/",views.status_count,name="status"),
]

'''
Password Reset -using authentication views
Submit email form  - PasswordResetView.as_view()
Email sent success message -PasswordResetDoneView.as_view()
Link to password reset form in email -PasswordResetConfirmView.as_view()
Password successfully changed message -PasswordResetCompleteView.as_view()

'''