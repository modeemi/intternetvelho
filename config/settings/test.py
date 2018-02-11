# -*- coding: utf-8 -*-

import os

from .local import *  # noqa

SECRET_KEY = env('DJANGO_SECRETKEY', default='thisisthedummydjangosecretkey')
RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY', default=None)
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY', default=None)

os.environ.setdefault('RECAPTCHA_DISABLE', 'True')
