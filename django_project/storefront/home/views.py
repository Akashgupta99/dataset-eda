from django.shortcuts import render
from . import logic
# Create your views here.
def first_page(request):
    return render(request, 'index.html')

def second_page(request):
    return render(request, "index2.html")

def some_calc(request):
    if request.method == 'POST':
        if request.POST.get("NAME", False) and request.POST.get("PASSWORD", False):
            msg = logic.sql_execute(name=request.POST.get("NAME"), password = request.POST.get("PASSWORD"))
            return render(request, 'index2.html', {'msg': msg})
        
