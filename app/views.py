from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'HEMA'}
    return render(request,'looping.html',d)
