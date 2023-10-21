from django.shortcuts import render, redirect
from .formulaire import MessageForm

# Create your views here.


def index(request):
    return render(request, 'sites/index.html')


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MessageForm    
    return render(request, 'sites/contacts.html', {'form': form})


def about(request):
    return render(request, 'sites/about.html')
