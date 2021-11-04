from django.shortcuts import render
from . models import Student, Teacher
from django.db.models import Q

def home(request):
  student_data=Student.objects.all()
  #student_data=Student.objects.filter(marks=90)
  #student_data=Student.objects.exclude(marks=90)
  #student_data=Student.objects.order_by('?')
  #student_data=Student.objects.order_by('id').reverse()
  #student_data=Student.objects.order_by('id').reverse()[2:5]
  #student_data=Student.objects.values()
  #student_data=Student.objects.values('name','city')
  #student_data=Student.objects.values_list(named=True)
  #student_data=Student.objects.using('default')
  #student_data=Student.objects.dates('pass_date','year')
  # qs1=Student.objects.values_list('id','name',named=True)
  # qs2=Teacher.objects.values_list('id','name',named=True)
  # student_data=qs2.intersection(qs1 )
  # qs1=Student.objects.values_list('id','name',named=True)
  # qs2=Teacher.objects.values_list('id','name',named=True)
  # student_data=qs2.difference(qs1 )
  #student_data=Student.objects.filter(id=6) & Student.objects.filter(roll=106)
  #student_data=Student.objects.filter( Q(id=6) & Q(roll=106) )
  #student_data=Student.objects.filter(id=6) | Student.objects.filter(roll=107)
  print('Return :', student_data)
  print()
  print('SQL Query:',student_data.query)
  return render(request,'school/home.html',{'students':student_data})

