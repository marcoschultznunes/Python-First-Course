"""
In our Stores app, we would need to create a class called Pizzeria and
add the following fields:

    Name of the pizzeria: The name should not be longer
    than 200 characters. The field cannot be left blank.
    The name does not have to be unique.

    Street: Up to 400 characters or can be left blank.
    
    City: Up to 200 characters and cannot be left blank.
    
    State: For now, let’s concentrate on US pizzerias
    only and add a list of all states.
    
    Zip code: It should be five digits, and we can leave it
    blank with a default value of 0.
    
    Website: It should be a URL or can be left blank.
    
    Phone number: Format should be ten digits, no
    parentheses or dashes.
    
    Description of a pizzeria: It should be plain text
    or can be left blank.
    
    Pizzeria image or logo: Attached png or jpg file, stored
    in a special folder – pizzeriaImages – and could be left
    blank. We will place there a default image.
    
    Email: This field could be left blank or be up to 200
    characters.

Also, I usually add an active field, as a Boolean value, to filter later by
current records. If the pizzeria goes out of the business, we would mark it
as inactive.
"""

# blank=True => Specifies that forms do not require the field to make requests.
# null=True => Makes the column accept NULL as a value

from django.db import models
from django.core.validators import MinLengthValidator

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

    logo_image = models.ImageField(
        upload_to='pizzariaImages', default='pizzariaImages/pizzaLogo.png', blank=True
    )

    email = models.EmailField(max_length=256, blank=True)

    active = models.BooleanField(default=True)

"""
    For the image field we'll install a package called pillow:
        pip3 install pillow
        pip freeze > requirements.txt
"""

"""
    Migrations:

    Then, we'll make the migrations:
        python manage.py makemigrations

    and migrate:
        python manage.py migrate
"""

# Finally, we also need to add the model to stores/admin.py
from django.contrib import admin

from .models import Pizzeria

admin.site.register(Pizzeria)
