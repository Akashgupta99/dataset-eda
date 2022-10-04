from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function -> (takes request -> response)
# basically a request handler or action or in django: view

def say_hello(request, name = None):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': name})
