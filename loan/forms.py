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


# CREATE LoanForm 
class DepositForm(ModelForm):
    class Meta:
        model= CustomerAccount
        # fields= "__all__"
        fields=('account_number','balance'  )

        labels={
            'account_number': 'account_number',
            'balance': 'balance',

        }

        widgets={
           'account_number': forms.TextInput(attrs={'class': 'form-control','placeholder':' enter account number '}),
           'balance': forms.TextInput(attrs={'class': 'form-control','placeholder':'amount to deposit'}),

        }