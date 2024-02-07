from pathlib import Path
from dotenv import load_dotenv
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'cailtonoliveira.com',
    'cailtonoliveira.com',
    'www.cailtonoliveira.com',
    'www.cailtonoliveira.com',
    'portfolio-backend-git-feature-api-cailtondevs-projects.vercel.app',
    'portfolio-backend-git-feature-api-cailtondevs-projects.vercel.app',
    'backend.cailtonoliveira.com.br',
    'backend.cailtonoliveira.com.br',
    'graceful-longma-9a1bff.netlify.app',
    'graceful-longma-9a1bff.netlify.app'
]

ROOT_URLCONF = 'portfolio_app.urls'
WSGI_APPLICATION = 'portfolio_app.wsgi.app'

# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Snippet to put apps in subfolder
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../apps'))
