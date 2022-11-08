from django.shortcuts import render
from frontend import *

def kompyuter1(request):
    return render(request,'acer.html')

def kompyuter2(request):
    return render(request,'hp.html')

def kompyuter3(request):
    return render(request,'windows.html')


