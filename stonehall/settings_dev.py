import os

ALLOWED_HOSTS = ['u1333982.isp.regruhosting.ru', 'www.u1333982.isp.regruhosting.ru']

SECRET_KEY = '*)_dq)$**@msqrwwp!0gxq)7&17ym6-mgmt8d+d_oz9mf=80-!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u1333982_default',
        'USER': 'u1333982_default',
        'PASSWORD': 'HfIoZl!9',
        'HOST': '127.0.0.1',
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('STONEHALL_EMAIL_FROM')
EMAIL_HOST_PASSWORD = os.getenv('STONEHALL_EMAIL_FROM_PASSWORD')
EMAIL_PORT = 587

EMAIL_TO = os.getenv('STONEHALL_EMAIL_TO')

CACHE_TIMEOUT = 30
