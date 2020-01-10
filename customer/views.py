from django.shortcuts import render
from customer.models import Customer

def index(request):
    return render(request,
        'customer/index.html',
        {
            'title': 'Customer',
            'bodystart': 'Customer',
            'customers': Customer.objects.all(),
            'bodystop': 'bodystop',
        }
    )
