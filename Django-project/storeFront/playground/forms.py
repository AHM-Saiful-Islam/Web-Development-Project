from django import forms
from .models import Member
from .models import Product

class MemberForm(forms.ModelForm):
    
    class Meta:
        model = Member
        fields = ("fname", "lname", "email", "password", "age")


class ProductForm(forms.ModelForm):   # ProductForm extends ModelForm in forms
    
    class Meta: # provides metadata about the form. it specifies the model and the fields to be included in the form.
        model = Product      # form will save the data in Product model
        fields = ("name", "description", "stock", "category", "price", "company")


