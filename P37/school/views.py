from django.shortcuts import render
from .models import Students


def home_view(request):
  #stud_data=Students.objects.all()
  #stud_data=Students.stu.all()
  stud_data=Students.stu.get_stu_roll_range(201,203)

  return render(request,'school/home.html',{'sdisp':stud_data})

