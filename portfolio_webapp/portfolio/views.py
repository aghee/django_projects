from django.shortcuts import render,get_object_or_404,redirect
from .models import Project,Tag
from .forms import ContactForm


# Create your views here.
def home(request):
    projects=Project.objects.all()
    tags=Tag.objects.all()
    context={
        "projects":projects,
        "tags":tags
    }
    return render(request,"home.html",context)

def contact(request):
    form=ContactForm()
    if request.method =="POST":
        form=ContactForm(request.POST)
        # print("*********",request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context={
        "form":form
    }
    return render(request,"contact.html",context)

def about(request):
    return render(request,"about.html")

def project(request,id):
    project=get_object_or_404(Project,pk=id)
    return render(request,"project.html",{"project":project})
