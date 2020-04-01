from django.shortcuts import render


def home(request):
    fulltext = request.GET['fulltext']
    return render(request, 'home.html', {'fulltext': fulltext})