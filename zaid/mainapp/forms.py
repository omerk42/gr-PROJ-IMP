from django.forms import ModelForm

from .models import *

class AuctionForm(ModelForm):
     class Meta:
        model = Auction
        fields =  ['name','description','image','minimal_price'] 