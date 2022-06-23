from django import forms


from django.forms import ModelForm
from .models import *


# CREATE LoanForm
class LoanForm(ModelForm):
    class Meta:
        model = Loan
        # fields= "__all__"
        fields = ('amount', 'due_date')

        labels = {
            'Amount': 'amount',
            'Due Date': 'due_date',

        }

        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'due_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Clearance Date: yyyy-mm-dd'}),

        }


# CREATE LoanForm
class DepositForm(ModelForm):
    class Meta:
        model = CustomerAccount
        # fields= "__all__"
        fields = ('balance',)

        labels = {
            'Balance': 'balance'
        }

        widgets = {
            'balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount to deposit'}),

        }
