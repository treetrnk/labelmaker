from django.shortcuts import render
from .models import Label

def index(request):
    context = {}
    context['labels'] = Label.objects.all().order_by('sku')
    return render(request, 'labels/generator.html', context)

def generate(request):

    context = {}

    return render(request, 'labels/generator.html')

