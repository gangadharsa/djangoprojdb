from django.shortcuts import render
from .models import Product

# Create your views here.
def input(request):
    return render(request,'input.html')
def insert(request):
    pid1=int(request.POST['t1'])
    pname1=request.POST['t2']
    pcost1=float(request.POST['t3'])
    pmfdt1=request.POST['t4']
    pexpdt1=request.POST['t5']
    f=Product(pid=pid1,pname=pname1,pcost=pcost1,
              pmfdt=pmfdt1,pexpdt=pexpdt1)
    f.save()
    return render(request,'links.html')
def display(request):
    recs=Product.objects.all()
    return render(request,'display.html',{'records':recs})
