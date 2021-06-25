from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def product(request):
    return render(request, 'product.html')


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
