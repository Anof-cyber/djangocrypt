from django.urls import path
from . import views

urlpatterns = [
    path('myprofile', views.myprofile, name='getmyprofile'),
    path('getallusers', views.getallusers, name='getallusers'),
    path('getall', views.getall, name='getall'),
    path('getall2', views.getall2, name='getall2'),
    path('getuser', views.getuser, name='getuser'),
    path('getuser2', views.getuser2, name='getuser2'),
    path('getuser3', views.getuser3, name='getuser3'),
    path('getuser4', views.getuser4, name='getuser4'),
    path('getuser5', views.getuser5, name='getuser5'),
    path('', views.home, name='home'),
]
