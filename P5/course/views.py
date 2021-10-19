from django.shortcuts import render

def course_view(request):
  return render(request,'course/courseinfo.html')
