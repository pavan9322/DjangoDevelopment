from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm 
from django import forms


#this is the login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))




#this is the user feedback form
class ContactForm(forms.Form):

    LAVINGTON = 'LN'
    KAREN = 'KN'
    NGONG = 'ND'
    WOODLEY = 'WY'
    NEIGHBOURHOOD_CHOICES = (
        (LAVINGTON, 'Lavington'),
        (KAREN, 'Karen'),
        (NGONG, 'Ngong Road'),
        (WOODLEY, 'Woodley'),
    )



    contact_name = forms.CharField(required=True)
    #phone_number = forms.IntegerField(required=True,widget=forms.NumberInput)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number =forms.CharField(label=u'Phone', max_length=200) # validators should be a list
    rating       =forms.IntegerField(required=True,max_value=10,min_value=0)
    neighbourhood = forms.ChoiceField(required=True, choices=NEIGHBOURHOOD_CHOICES)

    comments = forms.CharField(required=True,widget=forms.Textarea)
