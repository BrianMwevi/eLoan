from django.db import models
from django.contrib.auth.models import AbstractUser
# from loan.models import Account


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(default='default.jpg',upload_to='pics/')
    phone = models.CharField(max_length=200,blank=True,null=True)
    account = models.CharField(max_length=200,blank=True,null=True)
    account = models.CharField(max_length=200,blank=True,null=True)
    is_lender = models.BooleanField(default=False)
    is_applicant= models.BooleanField(default=False)

    
    def __str__(self):
        return self.name