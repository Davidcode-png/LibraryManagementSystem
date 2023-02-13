from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        labels = {
            'first_name':'Name',
            'username':'Matric No/Staff No',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-outline form-control','placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-outline form-control','placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'class':'form-outline form-control','placeholder':'Email'})
        self.fields['username'].widget.attrs.update({'class':'form-outline form-control','placeholder':'Matric No/Staff No'})
        self.fields['password1'].widget.attrs.update({'class':'form-outline form-control','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-outline form-control','placeholder':'Confirm Password'})
