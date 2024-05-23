from django.http import HttpResponse 
from django.shortcuts import redirect

#stops unathenticated user from viewing the login and register page
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
             return redirect("home")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator_one(view_func):
        def wrapper_func(request,*args,**kwargs):
            # print("Works****",allowed_roles)
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            
            else:
                return HttpResponse("You are not AUTHORIZED to access this page!")
            
        return wrapper_func
    return decorator_one

#admin-only decorator that restricts user from viewing a page
def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        
        if group =='customer':
            return redirect("user")
        
        if group=="admin":
            return view_func(request,*args,**kwargs)
    return wrapper_func
