"""
    First we need to install pillow (to our env) for image uploads:
        pip3 install pillow
        pip freeze > requirements.txt
"""

# In settings.py:
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
