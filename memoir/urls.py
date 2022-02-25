from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='Memoir~Home'),
    path('gallery/', views.gallery, name='Memoir~Gallery'),
    path('about/', views.about, name='Memoir~About'),
    path('login/', views.login, name='Memoir~Login'),

]
 