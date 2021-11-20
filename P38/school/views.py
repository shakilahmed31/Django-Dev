from django.shortcuts import render
from .models import Students ,ProxyStudent


def home_view(request):
  #stud_data=Students.objects.all()
  #stud_data=Students.stu.all()
  #stud_data=Students.stu.get_stu_roll_range(201,203)
  stud_data=ProxyStudent.objects.all()

  return render(request,'school/home.html',{'sdisp':stud_data})

