from django.shortcuts import render
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

data = {
    'title': 'Главная страница',
    'values': ['Some', 'Hello', '123']
}
# Create your views here.
def index(requests):
    return render(requests, 'main/index.html', data)

def about(requests):
    return render(requests, "main/about.html")

def login(requests):
    return render(requests, "main/login.html")

@login_required
def profile_view(requests):
    return render(requests, "main/profile.html")
