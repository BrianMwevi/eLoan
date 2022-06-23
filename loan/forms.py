from django import forms
from accounts.models import User
from .models import create_profile

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('name', 'email','image','account','phone')
        




