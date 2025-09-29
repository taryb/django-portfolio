"""
Django settings for portfolio_site project (Django 5.2.6)
Production-ready for Render + Porkbun domain: taryb.dev
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------
# Security / Debug
# -----------------------------------------------------------------------------
# Set this in Render (Settings → Environment):
# SECRET_KEY = <a long, random value>
SECRET_KEY = os.getenv("SECRET_KEY", "!!!-REPLACE-ME-FOR-LOCAL-ONLY-!!!")

# Optionally set DEBUG in env for local dev:
# DEBUG=true  (anything truthy)
# DEBUG = os.getenv("DEBUG", "false").lower() in {"1", "true", "yes"}
DEBUG = True

ALLOWED_HOSTS = [
    "taryb.dev",
    "www.taryb.dev",
    # Keep the Render hostname during cutover (replace with your actual one or remove later):
    os.getenv("RENDER_EXTERNAL_HOSTNAME", "").strip() or "your-service.onrender.com",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "https://taryb.dev",
    "https://www.taryb.dev",
]

# Trust X-Forwarded-Proto from Render so Django knows it’s HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Tighten cookies when not in DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE   = not DEBUG

# (Optional but recommended once DNS/HTTPS is stable; increase max_age over time)
# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7   # 1 week to start; raise to 31536000 later
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# -----------------------------------------------------------------------------
# Applications
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolio",  # your app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise must be directly after SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Your top-level templates directory (e.g., templates/portfolio/base.html)
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio_site.wsgi.application"

# -----------------------------------------------------------------------------
# Database (SQLite for now; can switch to Postgres later)
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -----------------------------------------------------------------------------
# Password validation
# -----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------------------------------------------------------
# Internationalization
# -----------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Los_Angeles"
USE_I18N = True
USE_TZ = True

# -----------------------------------------------------------------------------
# Static files (served by WhiteNoise in production)
# -----------------------------------------------------------------------------
STATIC_URL = "static/"

# where your source assets live (e.g., static/css/style.css)
STATICFILES_DIRS = [BASE_DIR / "static"]

# where collectstatic will place files for production
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise: gzip + brotli for better performance
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# -----------------------------------------------------------------------------
# Default primary key field type
# -----------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------------------------------------------
# Minimal logging (helpful on Render)
# -----------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}
