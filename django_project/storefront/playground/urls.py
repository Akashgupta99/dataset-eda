from django.urls import path
from . import views

# RRLConf
urlpatterns = [
    path('hello/', views.say_hello, {"name": "Akash"})
]