from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch



# Create your views here.
def home(request):
 return render(request, 'home.html')
  # return HttpResponse('<h1>My First Django Route!</h1>')


def about(request):
  return render(request, 'about.html')
  # return HttpResponse('<h1>About the CatCollector</h1>')


# Add new view
def finches_index(request):
  Finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'Finches': Finches  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })