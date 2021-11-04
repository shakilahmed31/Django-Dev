from django.shortcuts import render
from .models import ExamCenter , Students

def home_view(request):
  student_data=Students.objects.all()
  center_data=ExamCenter.objects.all()
  
  return render(request,'school/home.html',{'stud':student_data,'exud':center_data})

