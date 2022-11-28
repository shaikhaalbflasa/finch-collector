from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm


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
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 'finch': finch , 'feeding_form': feeding_form})

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
 
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class finchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/'

class finchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age' , 'imag']
  success_url = '/finches/'

class finchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'