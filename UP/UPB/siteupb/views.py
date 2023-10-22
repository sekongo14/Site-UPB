from django.shortcuts import render, redirect
from .formulaire import MessageForm
from django.urls import reverse

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


def renseigne(request):
    return render(request, 'sites/renseigne.html')


# def admin(request):
#     admin_url = reverse('admin:index')
#     return render(request, 'sites/index.html', {'admin_url': admin_url})