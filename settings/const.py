from . import get_env_variable


SECRET_KEY = get_env_variable('SECRET_KEY')
ADMIN_SITE_URL = get_env_variable('ADMIN_SITE_URL')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
