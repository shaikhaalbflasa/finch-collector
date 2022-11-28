from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  # new route below 
  path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
  # class Based Views Below
  path('finches/create/', views.finchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', views.finchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete/', views.finchDelete.as_view(), name='finches_delete'),
  path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]

