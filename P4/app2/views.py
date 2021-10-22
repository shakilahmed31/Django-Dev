from django.shortcuts import render
from datetime import datetime

def learnpy(request):
  course   = 'Python'
  duration = '4 Month'
  cost     = '8000 tk'
  d        = datetime.now()
  course = {'sub':course, 'time':duration, 'amount':cost,'dt':d }
  return render(request,'app2/app2.html',course)
