# -*- coding: utf-8 -*-
#/usr/lib/python3
import os, sys
sys.path.append('/home/ubuntu/PycharmProjects/djangoProject/social')
sys.path.append('/home/ubuntu/PycharmProjects/djangoProject/social/social')
sys.path.append('/home/ubuntu/PycharmProjects/djangoProject/virtualenv/MyEnvSocial/lib/python3.6/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

