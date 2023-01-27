from django.shortcuts import render
from app.models import *

# Create your views here.
def dept(request):
    qsd=Department.objects.all()
    d={'dept':qsd}

    return render(request,'depart.html',d)

def emp(request):
    qse=Employe.objects.all()
    d={'emp':qse}

    return render(request,'employee.html',d)
