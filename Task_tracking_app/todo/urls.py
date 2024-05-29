from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete

urlpatterns=[
    path("",TaskList.as_view(),name="all_tasks"),
    path("task/<int:pk>/",TaskDetail.as_view(),name="detailtask"),
    path("task-create/",TaskCreate.as_view(),name="createtask"),
    path("task-update/<int:pk>",TaskUpdate.as_view(),name="updatetask"),
    path("task-delete/<int:pk>",TaskDelete.as_view(),name="deletetask"),
]