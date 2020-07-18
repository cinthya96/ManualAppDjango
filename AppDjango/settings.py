import os



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'r7r)yo)#)#0pvogidtmy38@f+3ip@3q-w6nwjxhafnl)-9=b$%'

DEBUT = True

ALLOWED_HOSTS =[]


INSTALLED_APPS =[
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE =[
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.crsf.CrsfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF =  'AppDjango.urls '

TEMPLATES = [
    {
        'BACKEND ': 'django.template.backends.django.Djangotemplates',
        'DIRS ':[os.path.join(BASE_DIR,'templates')],
        'APP_DIRS ': True,
        'OPTIONS ': {
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AppDjango.wsgi.application'


DATABASE = {
    'default': {
        'ENGINE': 'django.db.backend.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MininumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_LION= True

USE_TZ= True


STACTIC_URL= '/static/'
