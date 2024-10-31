#SampleApp1/urls.py file

from django.urls import path;	#new
from SampleApp1 import views;

urlpatterns = [ 
	path('one/', views.f11), 
	path('two/', views.f22),
	path('Developer/',views.f33),
];
