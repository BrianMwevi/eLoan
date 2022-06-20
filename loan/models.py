from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=155)
    account_bal = models.URLField(max_length=255)
    date_created = models.DateField(auto_now_add=True, auto_now=False, blank=True)