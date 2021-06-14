from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': "django e-ecommerce"
    }
    return render(request, 'index.html', context)
