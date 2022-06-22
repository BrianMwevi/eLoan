from re import A
from django.contrib import admin
from loan.models import CustomerAccount, Loan, Creditor, Debtor, Transaction

admin.site.register(CustomerAccount)
admin.site.register(Loan)
admin.site.register(Creditor)
admin.site.register(Debtor)
admin.site.register(Transaction)
