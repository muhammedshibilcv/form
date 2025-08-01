from django.shortcuts import render, redirect
from .forms import Loging_form

# Create your views here.
def home(req):
    return render(req, 'home.html')


def form(req):
    if req.method == 'POST':
        form = Loging_form(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'home.html', {'form': form})
    else:
        form = Loging_form()
    return render(req, 'forms.html', {'form': form})