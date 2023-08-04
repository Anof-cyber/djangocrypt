from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('myprofile', views.myprofile, name='getmyprofile'),
    path('getallusers', views.getallusers, name='getallusers'),
    path('getall', views.getall, name='getall'),
    path('getall2', views.getall2, name='getall2'),
    path('getuser', views.getuser, name='getuser'),
    path('getuser2', views.getuser2, name='getuser2'),
    path('getuser3', views.getuser3, name='getuser3'),
    path('getuser4', views.getuser4, name='getuser4'),
    path('getuser5', views.getuser5, name='getuser5'),
    path('demo', views.home, name='home'),

    path('complete-body/example/1', views.login, name='login'),
    path('complete-body/api/1', views.loginuser, name='loginuser'),

    path('complete-body/example/2', views.login2, name='login2'),
    path('complete-body/api/2', views.loginuser2, name='login2'),


    path('paramtervalue/example/1', views.login3, name='login3'),
    path('paramtervalue/api/1', views.loginuser3, name='login3'),
    
    path('paramterkeyvalue/example/1', views.login4, name='login4'),
    path('paramterkeyvalue/api/1', views.loginuser4, name='login4'),

    path('custom-request/example/1', views.login5, name='login5'),
    path('custom-request/api/1', views.loginuser5, name='login5'),

    path('custom-request-edit/example/1', views.login6, name='login6'),
    path('custom-request-edit/api/1', views.loginuser6, name='login6'),

    path('custom-request-edit/example/2', views.login7, name='login7'),
    path('custom-request-edit/api/2', views.loginuser7, name='login7'),

    path('RSA/example/1', views.RSALogin, name='RSA'),
    path('RSA/api/1', views.loginuser8, name='login8'),
]
