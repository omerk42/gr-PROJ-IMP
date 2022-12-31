from django.shortcuts import render,redirect
from ..forms import AuctionForm
# Create your views here.
def auctions(request):
    return render(request,"base.html")


def new_auction(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context= {"form":AuctionForm}
 
    return render(request,"auctions/new.html",)

def create_auction(request):
    pass