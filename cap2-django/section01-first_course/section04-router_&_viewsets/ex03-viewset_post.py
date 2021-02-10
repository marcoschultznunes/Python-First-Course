"""
    By default, model viewsets require authentication for create update and delete.
    So to test these methods of the user viewset i'll disable authentication,
    by going to settings.py and adding the following code:
"""

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}


"""
    In Django Rest Framework we need to add a slash at the end of the POST, PUT or PATCH request.
    This can be disabled adding APPEND_SLASH=False to settings.py, but it is not recommended
    as you also need to set trailing_slash=False for each and every router you gotta use.

    The Django team recommends this append slash concept.
"""


"""
    Now i can test my POST request with insomnia.

    Request:

    POST http://127.0.0.1:8000/app/users/

    {
	    "name": "Mr Big Benga",
	    "email": "mbb@gmail.com",
	    "password": "cudoKrl"
    }


    Response:

    {
        "id": 2,
        "name": "Mr Big Benga",
        "email": "mbb@gmail.com",
        "password": "cudoKrl",
        "created_at": "2021-01-27T09:44:02.745585Z",
        "updated_at": "2021-01-27T09:44:02.745635Z"
    }

"""

# PATCH, PUT & DELETE should work as normal also.
