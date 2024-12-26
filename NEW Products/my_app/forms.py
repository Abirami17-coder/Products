
from django.forms import ModelForm
from .models import *

class product_form(ModelForm):

    class Meta:
        model=product
        fields=['product_name','product_code','selling_price','original_price','product_qty']

