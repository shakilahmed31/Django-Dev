from django.shortcuts import render
from . models import Student


def home(request):
  #student_data=Student.objects.get(name='Tamim')
  #student_data=Student.objects.first()
  #student_data=Student.objects.order_by('name').first()
  #student_data=Student.objects.last()
  #student_data=Student.objects.order_by('name').last()
  #student_data=Student.objects.latest('pass_date')
  #student_data=Student.objects.all()
  #one_date=Student.objects.get(pk=1)
  #st_data=Student.objects.create(name='Hasan',roll=212,city='cumilla',marks=90,pass_date='2019-10-2')
  #st_data,created=Student.objects.get_or_create(name='Sumon',roll=213,city='cumilla',marks=90,pass_date='2019-10-2')
  #st_data=Student.objects.filter(marks=90).update(city='Pass')
  #st_data ,created =Student.objects.update_or_create(id=7,name='Tamim',defaults={'name':'Tamim Hossen'})
  #print('Value Check :', st_data)
  #print('check: ',student_data.filter(pk=one_date.pk).exists())
  #print('data base existency :', student_data.exists())
  #print('SQL Query :', student_data)
  all_student_data=Student.objects.all()
  for stu in all_student_data:
    stu.city='Dhaka'
  st_data=Student.objects.bulk_update(all_student_data ,['city']) 


  return render(request,'school/home.html',{'students':st_data})

