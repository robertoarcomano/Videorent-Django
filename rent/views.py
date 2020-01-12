from django.shortcuts import render
from rent.models import Rent

def index(request):
    return render(request,
        'rent/index.html',
        {
            'title': 'Rent',
            'bodystart': 'Rent',
            'rents': Rent.objects.all(),
            'bodystop': 'bodystop',
        }
    )
