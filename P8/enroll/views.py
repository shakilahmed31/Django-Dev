from django.shortcuts import render
from .models import Students



def srudent_view(request):

  stud=Students.objects.all()

  return render(request,'enroll/sdetails.html',{'stu':stud})
