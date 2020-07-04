from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
#    return HttpResponse('hi there!  Im hello word!')
  return render(request ,'about.html')

def home(request):
#     return HttpResponse('ALI')
  return render(request ,'Home.html')
