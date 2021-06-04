from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator
from listings.options import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.all()
    is_mvp = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'is_mvp': is_mvp
    }
    return render(request, 'pages/about.html', context)
