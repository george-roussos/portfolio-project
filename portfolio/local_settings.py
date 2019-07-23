SECRET_KEY = 'gpo=q#_++bx207zha7sj&%LAH@r64q$zlm0^&qm97n@ggzk7_c0&4'

ALLOWED_HOSTS = ['167.71.56.202','localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER':'djangodbman',
        'PASSWORD':'django1234',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

DEBUG = False
