from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    tags=models.ManyToManyField(Tag,related_name="project")
    link=models.URLField(max_length=200,blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project=models.ForeignKey(Project,related_name="images",on_delete=models.CASCADE)
    image=models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"
class Contact(models.Model):
    name=models.CharField(max_length=100,null=False)
    organization=models.CharField(max_length=100,null=True,blank=True)
    phone_number=models.CharField(max_length=15,null=False)
    email=models.EmailField(max_length=100,verbose_name="email address",null=False)
    message=models.TextField(max_length=1000,null=False)
    

