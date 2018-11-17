from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'index.html')


def careers(request):
    return render(request, 'index.html')


def planroom(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'index.html')
