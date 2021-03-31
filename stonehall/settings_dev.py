import os

ALLOWED_HOSTS = ['xn--80akngadii6d9c.xn--p1ai', 'www.xn--80akngadii6d9c.xn--p1ai']

SECRET_KEY = 'v2wfbc3fz0b(#b#olicd6^vvj48klvsl8dg7ie2r@qa$hhbjo'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u1002778_new_db',
        'USER': 'u1002778_user',
        'PASSWORD': 'db_password',
        'HOST': '127.0.0.1',
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'stonehall.info@gmail.com'
EMAIL_HOST_PASSWORD = 'esposti100p'
EMAIL_PORT = 587

EMAIL_TO = 'admin@каменьхолл.рф'

CACHE_TIMEOUT = 60 * 60 * 24
