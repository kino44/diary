from django.shortcuts import render
from .models import DiaryModel
from django.views.generic import ListView

class DiaryList(ListView):
  template_name = 'diaryapp/list.html'
  model = DiaryModel