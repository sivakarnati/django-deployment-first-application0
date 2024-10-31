from django.shortcuts import render;
from django.http import HttpResponse

#Create your views here...
def f11(request): 
	return HttpResponse("<h1>Hello from SampleApp1 f11()</h1><hr />"); 
def f22(request): 
	return HttpResponse("<h1>Hello from SampleApp1 f22()</h1><hr />");