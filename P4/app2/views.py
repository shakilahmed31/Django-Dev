from django.shortcuts import render

# Create your views here.

def learnpy(request):
  course   = 'Python'
  duration = '4 Month'
  cost     = '8000 tk'
  course = {'sub':course, 'time':duration, 'amount':cost}
  return render(request,'app2/app2.html',course)
