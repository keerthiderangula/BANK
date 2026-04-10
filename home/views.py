from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def wonder(request):
    return render(request,'wonder.html')

def chan(request):
    return render(request,'chan.html')

def dora(request):
    return render(request,'dora.html')

def krishna(request):
    return render(request,'krishna.html')

def stuart(request):
    return render(request,'stuart.html')