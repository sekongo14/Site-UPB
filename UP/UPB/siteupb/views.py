from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'sites/index.html')


def contact(request):
    return render(request, 'sites/contacts.html')


def about(request):
    return render(request, 'sites/about.html')
