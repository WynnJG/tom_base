from django.shortcuts import render

# Create your views here.

from .forms import SearchForm

def index(request):
	form = SearchForm()
	return render(request, 'my-nu.html', {'form':form})

