from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.


def demo(request):
    obj = Place.objects.all()
    team =Team.objects.all()
    return render(request, "index.html",{'result':obj,'team':team})

#
# def about(request):
#     return render(request,"about.html")
#
#
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     z= x+y
#     return render(request,'result.html',{'addition':z})
