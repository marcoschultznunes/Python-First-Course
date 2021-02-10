from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class Pizzeria(models.Model): 
    name = models.CharField(max_length=200, validators=[MinLengthValidator(2)], blank= False)
    street = models.CharField(max_length=400, validators=[MinLengthValidator(2)], blank=False)
    city = models.CharField(max_length=200, validators=[MinLengthValidator(2)], blank= False)
    
    state = models.CharField(
        max_length=2, validators=[MinLengthValidator(2)], blank= True
    )

    zipcode = models.IntegerField(default=0, blank=True)
    website = models.URLField(max_length=420, blank=True)

    phone = models.CharField(
        max_length=10, blank=True
    )

    description = models.TextField(blank=True)

    # pip3 install pillow; pip freeze > requirements.txt

    logo_image = models.ImageField(
        upload_to='pizzariaImages', default='pizzariaImages/pizzaLogo.png', blank=True
    )

    email = models.EmailField(max_length=256, blank=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.city)
    

