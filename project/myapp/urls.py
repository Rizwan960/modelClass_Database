"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    path("homePage/",views.index,name="myindex"),
    path('data/',views.data,name='Mydata'),
    path("del/<int:id>",views.delete,name='del'),
    path("updt/<int:id>",views.update,name='upd'),
    path("signup/", views.signUp, name='signup'),
    path("", views.loginn, name='login'),
    path("myLogout",views.logoutt,name="mylogout"),
    path("activate/<str:id>/", views.activate, name="activate"),
    path("reset",PasswordResetView.as_view(template_name='passwordReset.html'),name='resetView'),
    path("password_reset/done/",PasswordResetDoneView.as_view(template_name='passwordResetDone.html'),name='password_reset_done'),
    path("password_confirm/<uidb64>/<token>",PasswordResetConfirmView.as_view(template_name='passwordResetConfirm.html'),name='password_reset_confirm'),
    path("password_complete/",PasswordResetCompleteView.as_view(template_name='passwordRestComplete.html'),name='password_reset_complete')

]
