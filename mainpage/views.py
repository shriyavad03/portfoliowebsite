from django.shortcuts import render

def show(request):
    return render(request, 'index.html')

def proj(request):
    return render(request, 'proj.html')

def cont(request):
    return render(request, 'cont.html')

def inte(request):
    return render(request, 'interests.html')



# Create your views here.
