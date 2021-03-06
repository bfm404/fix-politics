from django.shortcuts import render, redirect
from .models import Location, Impact, Criteria
from .forms import SearchForm
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
def index(request):
    """The home page for Fix Politics."""
    return render(request, 'index.html')

def locations(request):
    """Show all locations."""
    locations = Location.objects.order_by('date_added')
    locations = locations.exclude(desc='world')
    context = {'locations': locations}
    return render(request, 'locations.html', context)

def impacts(request):
    """Show all impacts."""
    impacts = Impact.objects.order_by('date_added')
    context = {'impacts': impacts}
    return render(request, 'impacts.html', context)


def search(request):
    """Show all impacts."""
    ARROW = r'&nbsp;&#8611;&nbsp;'
    crit = None
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        if request.user.is_anonymous:
            form = SearchForm()             # blank search form
        else:
            crit = request.user.profile.criteria
            form = SearchForm(instance=crit)  # pre-filled with profile

    else:
        # POST data submitted; process data.
        form = SearchForm(data=request.POST)      
        if form.is_valid():
            criteria = form.save()
            text = criteria.location.hierarchy
            if text.startswith('world.'):
                text = text[5:].replace('.', ARROW)	
            criteria.text = text  
            criteria.save()
            
            impacts = criteria.impacts.all()
            for impact in impacts:
                text += impact.text

            return redirect('fixpol:results', search_id=criteria.id)

    context = { 'form': form }
    return render(request, 'search.html', context)


def results(request, search_id):
    criteria = Criteria.objects.get(id=search_id)
    context = { 'text': criteria.text} 
    return render(request, 'results.html', context)


def criteria(request, search_id):
    """Show search criteria."""
    criteria = Criteria.objects.get(id=search_id)
    context = {'criteria': criteria}
    return render(request, 'criteria.html', context)

def share(request):
    return render(request, 'share.html')

   

