from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomLoginView(LoginView):
    template_name="todo/login.html"
    fields="__all__"
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy("all_tasks")
    
# class CustomLogoutView(LogoutView):
#     def get_success_url(self):
#         return reverse_lazy("login")

def logoutUser(request):
    logout(request)
    return redirect("login")

#default template:_list.html, context=object_list-can be overriden
class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name="tasks"

#default template:_detail.html, context=object-can be overriden
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name="task"
    template_name="todo/task.html"

#default template:_form.html, context=object-can be overriden
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('all_tasks')

#default template:_form.html context=object -can be overriden
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('all_tasks')

#default template:_confirm_delete.html context=object -can be overriden
class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    # fields='__all__'
    success_url=reverse_lazy('all_tasks')
    template_name="todo/task_confirmation_delete.html"

    