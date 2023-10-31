import os

from dotenv import find_dotenv, load_dotenv
from pathlib import Path

load_dotenv(find_dotenv())

# Global constants
MAX_LENGTH = 128
PHONE_MAX_LENGTH = 15
PHONE_MIN_LENGTH = 9

LOCATION_CHOICES = (
    ('MS', 'Moscow'),
    ('SP', 'Saint Petersburg'),
    ('EK', 'Ekaterinburg'),
    ('KZ', 'Kazan'),
)

EDUCATION_CHOICES = (
    ('HI', 'High'),
    ('SC', 'Secondary'),
    ('SC', 'Specialized secondary'),
    ('HU', 'High unfinished'),
)

COURSE_CHOICES = (
    ('PR', 'Programming'),
    ('DA', 'Data analytic'),
    ('DE', 'Desing'),
    ('MR', 'Marketing'),
    ('MN', 'Management'),
)

WORK_FORMAT_CHOICES = (
    ('RM', 'Remote'),
    ('OF', 'Office'),
    ('MX', 'Mix'),
)

EMPLOYMENT_CHOICES = (
    ('<1', 'Less 1'),
    ('<3', 'From 1 to 3'),
    ('<6', 'From 3 to 6'),
    ('>6', 'More 6'),
)


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ['DEBUG']

# For run in Docker
# ALLOWED_HOSTS = ['*']

# For run in production
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(' ')


INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'vacancies.apps.VacanciesConfig',
    'candidates.apps.CandidatesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'django_celery_results',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'career_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'career_tracker.wsgi.application'

# For SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# For Postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('POSTGRES_DB', 'django'),
#         'USER': os.getenv('POSTGRES_USER', 'django'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
#         'HOST': os.getenv('DB_HOST', ''),
#         'DB_PORT': os.getenv('DB_PORT', 5432),
#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
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

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'],
}

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'collected_static'


# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
