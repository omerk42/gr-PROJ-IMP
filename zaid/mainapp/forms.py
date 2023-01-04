from django.forms import ModelForm

from .models import *

class AuctionForm(ModelForm):
      class Meta:
        model = Auction
        fields =  ['name','description','image','minimal_price']
      
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)

         self.fields['name'].widget.attrs['data-jsv-validators'] = 'require,length'
         self.fields['name'].widget.attrs['data-jsv-min'] = '6'
         self.fields['name'].widget.attrs['data-jsv-max'] = '255'

         self.fields['description'].widget.attrs['data-jsv-validators'] = 'require,length'
         self.fields['description'].widget.attrs['data-jsv-min'] = '6'
         self.fields['description'].widget.attrs['data-jsv-max'] = '255'

         
         self.fields['image'].widget.attrs['data-jsv-validators'] = 'require'

         self.fields['minimal_price'].widget.attrs['data-jsv-validators'] = 'require,length'
         self.fields['minimal_price'].widget.attrs['data-jsv-min'] = '0.0'
         self.fields['minimal_price'].widget.attrs['data-jsv-max'] = '999999.99'
         self.fields['minimal_price'].widget.attrs['value'] = '0'


