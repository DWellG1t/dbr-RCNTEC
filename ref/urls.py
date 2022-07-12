from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('tips/', views.tip, name="hr"),
    path('prince/', views.prince, name="prince")
]





