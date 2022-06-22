from django.db import models
from django.contrib.auth.models import AbstractUser
# from loan.models import CustomerAccount



# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(default='default.jpg',upload_to='pics/')
    phone = models.CharField(max_length=200,blank=True,null=True)
    # account= models.ForeignKey(
    #     CustomerAccount, on_delete=models.CASCADE, related_name='account_no')
   
    loan = models.CharField(max_length=200,blank=True,null=True)
    is_lender = models.BooleanField('Is_lender',default=False)
    is_applicant= models.BooleanField('Is_applicant',default=False)

    
    def __str__(self):
        return self.username