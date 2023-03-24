
from django.contrib import admin
from django.urls import path
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',StudentView.as_view(),name='home'),
    path('insert/',StudentInsert.as_view(),name='insert'),
    path('accounts/login/',LoginVIew.as_view(),name='login'),
    path('accounts/register/',Signup.as_view(),name='register'),
    path('accounts/logout/',LogoutView.as_view(),name='logout'),
    path('deleteStudent/<pk>/',StudentDelete.as_view(),name='delete'),
    path('editStudent/<pk>/',StudentEdit.as_view(),name='edit')
]
