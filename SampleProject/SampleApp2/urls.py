#SampleApp2/urls.py

from django.urls import path;	#new
from SampleApp2 import views;

urlpatterns = [ 
	path('three/', views.f33), 
	path('four/', views.f44),
];