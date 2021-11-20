from django.shortcuts import render


# def show_data(request ,mid):
#   student ={'v1':mid}
#   #return render(request,'durl/index.html',{'v1':mid})
#   return render(request,'durl/index.html',student)

def home_view(request):
  return render(request,'durl/home.html')

def show_data(request ,mid):
  if mid==1:
    student ={'v1':mid ,'name':'Sabia'}
  if mid==2:
    student ={'v1':mid ,'name':'Tahsin'}
  if mid==3:
    student ={'v1':mid ,'name':'Prarthona'}
  #return render(request,'durl/index.html',{'v1':mid})
  return render(request,'durl/index.html',student)


def show_sub_data(request ,mid ,msid):
  if mid==1 and msid==5:
    student ={'v1':mid ,'name':'Sabia', 'info':'sub details'}
  if mid==2 and msid==6:
    student ={'v1':mid ,'name':'Tahsin','info':'sub details'}
  if mid==3 and msid==7:
    student ={'v1':mid ,'name':'Prarthona','info':'sub details'}
  #return render(request,'durl/index.html',{'v1':mid})
  return render(request,'durl/index.html',student)
