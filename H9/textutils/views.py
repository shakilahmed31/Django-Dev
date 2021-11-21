from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  params={'name':'Sabia', 'place':'Dhaka'}
  return render(request,'index.html', params)

def analyze(request):  
  djtext=request.GET.get('text' , 'default')
  rpunc=request.GET.get('text' , 'off')
  fullcaps=request.GET.get('fullcaps','off')
  nliner=request.GET.get('nliner','off')
  #analyzed=djtext 
    
  if rpunc =='on':
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed =" "
    for char in djtext:
      if char not in punc:
        analyzed= analyzed + char
    params={'purpose':'Remove Punc','analyze_text':analyzed}
    return render(request,'analyze.html',params)
  
  elif(fullcaps=='on'):
    analyzed=" "
    for ch in djtext:
      analyzed=analyzed + ch.upper()
    params={'purpose':'Change to upper Case','analyze_text':analyzed}
    return render(request,'analyze.html',params)

  elif(nliner=='on'):
    analyzed=" "
    for ch in djtext:
      if ch !="\n":
        analyzed=analyzed + ch
    params={'purpose':'New Line Remove','analyze_text':analyzed}
    return render(request,'analyze.html',params)
  else:
    return HttpResponse('Error')


def capfirst(request):
  return HttpResponse('Capitalize First')

def newlineremove(request):
  return HttpResponse('newlineremove')

def spaceremover(request):
  return HttpResponse('spaceremover')

def charcount(request):
  return HttpResponse('charcount')

