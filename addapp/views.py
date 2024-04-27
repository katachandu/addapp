from django.shortcuts import render
from django.http import HttpResponse

#create  your views here.
#
def input(request):
  return render(request, 'input.html')
def add(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    i=int(x)
    j=int(y)
    z=i+j
    con_dict= {"sum":z}
    return render(request,'result.html',context=con_dict)
