from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
   # new route below 
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),

]
