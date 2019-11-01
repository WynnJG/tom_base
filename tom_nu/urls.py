from django.urls import path
from django.views.generic import TemplateView
from .views import index 

app_name = 'tom_nu'

urlpatterns = [
	path('', index, name='home'),
]
