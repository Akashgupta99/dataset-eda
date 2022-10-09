from django.urls import path
from . import views
from . import logic

urlpatterns = [
    path('', views.first_page),
    path('script.js', views.second_page),
    path('some_calc', views.some_calc, name="submited")
]