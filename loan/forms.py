from django import forms


from django.forms import ModelForm
from .models import *




# CREATE LoanForm 
class LoanForm(ModelForm):
    class Meta:
        model= Loan
        # fields= "__all__"
        fields=('amount','due_date'  )

        labels={
            'amount': 'amount',
            'due_date':'due_date',

        }

        widgets={
           'amount': forms.TextInput(attrs={'class': 'form-control','placeholder':' loan amount '}),
           'due_date': forms.TextInput(attrs={'class': 'form-control','placeholder':' clearance date yyyy-mm-dd'}),

        }