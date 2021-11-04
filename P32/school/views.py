from django.shortcuts import render
from . models import Students,Teacher,Contractor

def home_view(request):
  student_data=Students.objects.all()
  teacher_data=Teacher.objects.all()
  contractor_data=Contractor.objects.all()
  return render(request,'school/home.html',{'sdisp':student_data,'tdisp':teacher_data,
  'cdisp':contractor_data})

