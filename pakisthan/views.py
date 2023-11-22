from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def imran(request):
    return render(request,'imran.html')

def shaikh(request):
    return HttpResponse('<h1> shaikh is good bowler</h1>')