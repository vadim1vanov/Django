from django.shortcuts import render


data = {
    'title': 'Главная страница',
    'values': ['Some', 'Hello', '123']
}
# Create your views here.
def index(requests):
    return render(requests, 'main/index.html', data)

def about(requests):
    return render(requests, "main/about.html")



