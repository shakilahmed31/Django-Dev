from django.shortcuts import render
from .models import Students


def home_view(request):
  stud_data=Students.stu.all()

  return render(request,'school/home.html',{'sdisp':stud_data})

