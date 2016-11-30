from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Items
from django.http import Http404

# Create your views here.
#the login_required decoratoe doesnt allow access without authentication

@login_required(login_url="login/")
def home(request):
	item = Items.objects.exclude(units=0)
	return render(request, "home.html", {
        'items': item,
    })

def item_detail(request, id):
    try:
        item = Items.objects.get(id=id)
    except Items.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'item_detail.html', {
        'items': item,
    })


