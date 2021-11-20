from django.db.models.aggregates import Avg ,Sum, Max,Min,Count
from django.shortcuts import render
from . models import Student

def home(request):
  st=Student.objects.all()
  tavg=st.aggregate(Avg('marks'))
  Total=st.aggregate(Sum('marks'))
  Maximum=st.aggregate(Max('marks'))
  Minimum=st.aggregate(Min('marks'))
  all_count=st.aggregate(Count('marks'))
  context={'student':st,'Total_Avg':tavg ,'Summation':Total,'Maximum':Maximum,'Minimum':Minimum,'counter':all_count}
  #average=st.aggregate(Avg('marks'))
  #st=Student.objects.filter(name__exact='Sabia')
  #st=Student.objects.filter(name__iexact='sabia')
  #st=Student.objects.filter(name__contains='A')
  #st=Student.objects.filter(marks__in=[70])
  #st=Student.objects.filter(marks__gt=70)
  #st=Student.objects.filter(marks__lt=70)
  #st=Student.objects.filter(name__istartswith='A')
  #st=Student.objects.filter(name__startswith='a')
  #st=Student.objects.filter(roll__isnull=False)
  print('Return :',st)
  print()
  print('SQL Query :', st.query)

  return render(request,'school/home.html',context)
