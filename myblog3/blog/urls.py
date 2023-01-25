from django.urls import path
from blog.views import *
from django import forms

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/<int:pk>', DetailView.as_view(), name='detail_post'),
    path('cat/<slug:slug>', CategoryView.as_view(), name='category_view'),
    #path('/register', RegisterUser.as_view(), name='register'),

]

