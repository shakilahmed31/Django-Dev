from django.shortcuts import render
from . models import ExamCenter,MyExamCenter

def home_view(request):
  exa=ExamCenter.objects.all()
  mexa=MyExamCenter.objects.all()
  return render(request,'school/home.html',{'dexa':exa,'dmexa':mexa})

