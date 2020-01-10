from django.shortcuts import render
from customer.models import Customer

def index(request):
    return render(request,
        'index.html',
        {
            'title': 'title',
            'bodystart': 'bodystart',
            'customers': Customer.objects.all(),
            'bodystop': 'bodystop',
        }
    )
