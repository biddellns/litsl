# [LiT Starleague](www.nicbiddell.com/litsl/)
Django web app to manage SC2 leagues modeled off the GSL format.

## Installation

This application relies on environment variables for secret settings. You will need to initialize:

**Django Settings** 
- DJANGO_SETTINGS_MODULE *(Recommended: litsl.settings.local)*
- SECRET_KEY
- ALLOWED_HOSTS *(Recommended: "'127.0.0.1', 'localhost'")*

**If using PostgreSQL**
- DB_NAME
- DB_USER
- DB_USER_PW

**To use Battle.net API with Django-Allauth**
- BNET_KEY
- BNET_SECRET
- BNET_REDIRECT_URI_Base *(Your site)*

## Libraries 
- [Django Allauth](https://github.com/pennersr/django-allauth)
- [Django SingleActiveObjectMixin](https://github.com/byteweaver/django-singleactiveobject)
- [Django-Widget-Tweaks](https://github.com/kmike/django-widget-tweaks)
