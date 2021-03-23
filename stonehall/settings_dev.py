import os

ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = '*)_dq)$**@msqrwwp!0gxq)7&17ym6-mgmt8d+d_oz9mf=80-!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stonehall_db',
        'USER': 'stonehall_user',
        'PASSWORD': 'devpass',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('STONEHALL_EMAIL_FROM')
EMAIL_HOST_PASSWORD = os.getenv('STONEHALL_EMAIL_FROM_PASSWORD')
EMAIL_PORT = 587

EMAIL_TO = os.getenv('STONEHALL_EMAIL_TO')