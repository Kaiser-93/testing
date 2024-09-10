from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    #listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # ! get all data from listing database 
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
     # ! pass database records into listings context
    context ={'listings': paged_listings}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    
    listing = get_object_or_404(Listing, pk=listing_id)
    context ={'listing': listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')