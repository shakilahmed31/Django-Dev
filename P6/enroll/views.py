from django.shortcuts import render
from enroll.models import Student


def studentinfo(request):
  stud=Student.objects.all()
  print("My Output:", stud )



  return render(request,'enroll/studetails.html',{'stu':stud})
