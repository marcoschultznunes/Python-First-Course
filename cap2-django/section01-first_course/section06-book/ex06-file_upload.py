"""
    After installing pillow:

    pip3 install pillow
    pip freeze > requirements.txt

    We add this to settings.py
"""
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


"""
    Also don't forget the attribute which we already defined on the pizzeria model:
"""
logo_image = models.ImageField(
    upload_to='pizzariaImages', default='pizzariaImages/pizzaLogo.png', blank=True
)



"""
    Note: all that's missing is validation and timestamp file naming
"""
