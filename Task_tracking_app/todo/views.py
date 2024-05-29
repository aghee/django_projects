from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
#default template:_list.html, context=object_list-can be overriden
class TaskList(ListView):
    model=Task
    context_object_name="tasks"

#default template:_detail.html, context=object-can be overriden
class TaskDetail(DetailView):
    model=Task
    context_object_name="task"
    template_name="todo/task.html"

#default template:_form.html, context=object-can be overriden
class TaskCreate(CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('all_tasks')

#default template:_form.html context=object -can be overriden
class TaskUpdate(UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('all_tasks')

#default template:_confirm_delete.html context=object -can be overriden
class TaskDelete(DeleteView):
    model=Task
    # fields='__all__'
    success_url=reverse_lazy('all_tasks')
    template_name="todo/task_confirmation_delete.html"

    