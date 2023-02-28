import my_settings

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
DEBUG = True
LANGUAGE_CODE = "ko"
TIME_ZONE = "Asia/Seoul"
USE_TZ = True


DATABASES = my_settings.DATABASES
SECRET_KEY = my_settings.SECRET_KEY
MIDDLEWARE = my_settings.MIDDLEWARE
TEMPLATES = my_settings.TEMPLATES
STATIC_URL = my_settings.STATIC_URL
STATIC_ROOT = my_settings.STATIC_ROOT
INSTALLED_APPS = my_settings.INSTALLED_APPS
ROOT_URLCONF = my_settings.ROOT_URLCONF