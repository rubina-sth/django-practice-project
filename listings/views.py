from django.core import paginator
from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .options import bedroom_choices, state_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {
        'listings': page_obj
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    listings = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'request_values': request.GET,
    }
    return render(request, 'listings/search.html', context)
