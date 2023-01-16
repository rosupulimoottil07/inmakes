from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def detail(request):
    return render(request,"detail.html")
def thank(request):
    return HttpResponse("Thank you")
def arithmetic(request):
    return render(request,"main.html")
def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res1=x+y
    res2=x-y
    res3=x/y
    res4=x*y
    return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
