from django.db import models

# Create your models here.



class LoginForm(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)





class ContactForm(models.Model):

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



    contact_name = models.CharField(max_length=30)
    #phone_number = forms.IntegerField(required=True,widget=forms.NumberInput)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number =models.CharField(max_length=200) # validators should be a list
    rating       =models.IntegerField()
    neighbourhood =models.CharField(max_length=200,choices=NEIGHBOURHOOD_CHOICES)

    comments = models.TextField()
