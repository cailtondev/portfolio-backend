# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

from .environment import BASE_DIR

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles_build'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
