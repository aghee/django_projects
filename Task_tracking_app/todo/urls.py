from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,logoutUser
# from django.contrib.auth.views import LogoutView


urlpatterns=[
    path("",TaskList.as_view(),name="all_tasks"),
    path("login/",CustomLoginView.as_view(),name="login"),
    # path("logout/",LogoutView.as_view(next_page="login"),name="logout"),
    path("logout/",logoutUser,name="logout"),
    path("task/<int:pk>/",TaskDetail.as_view(),name="detailtask"),
    path("task-create/",TaskCreate.as_view(),name="createtask"),
    path("task-update/<int:pk>",TaskUpdate.as_view(),name="updatetask"),
    path("task-delete/<int:pk>",TaskDelete.as_view(),name="deletetask"),
]