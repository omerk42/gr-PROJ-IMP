from django.shortcuts import render, redirect
from ..forms import AuctionForm
from ..models import Auction
from django.contrib import messages
from django.http import HttpResponse
import logging
from django.shortcuts import get_object_or_404

# Create your views here.
def auctions(request):
    auctions = Auction.objects.all()    
    context = {"auctions":auctions}
    return render(request, "auctions/index.html",context=context)

def show_auction(request,auction_id):
    auction = get_object_or_404(Auction,pk=auction_id)
    context = {"auction":auction}
    return render(request, "auctions/show.html",context=context)

def new_auction(request):
    if not request.user.is_authenticated:
        return redirect("account_login")
    context = {"form": AuctionForm}

    return render(request, "auctions/new.html", context=context)


def create_auction(request):
    if not request.user.is_authenticated:
        return redirect("account_login")
    if request.method == "POST":
        form = AuctionForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Auctions added successfully")
                return redirect("auctions")
            except Exception as e:
                logger = logging.getLogger(__name__)
                logger.error(str(e))
                messages.error(request, "an error occurred try again later")
                return redirect("new_auction")
        else:
            context = {"form": form}
            return render(request, "auctions/new.html", context=context)

    else:
        context = {"form": AuctionForm}
        return render(request, "auctions/new.html", context=context)
