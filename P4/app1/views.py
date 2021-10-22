from django.shortcuts import render

# Create your views here.

def learndj(request):
  course   = 'Django'
  duration = '4 Month'
  cost     = '8000 tk'
  course = {'sub':course, 'time':duration, 'amount':cost}
  return render(request,'app1/app1.html',course)

