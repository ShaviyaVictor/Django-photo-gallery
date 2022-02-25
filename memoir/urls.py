from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='Memoir~Home'),
    path('gallery/', views.gallery, name='Gallery'),

]
 