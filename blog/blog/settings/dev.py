from .common import *


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i((!c$bv(7g6vxkwvvxg-9@99fs8=^bka^bh6@!nq5cwfuh^dk'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'mrk',
        'PASSWORD': '2404',
        'HOST': 'localhost',
        'PORT': '',
    }
}