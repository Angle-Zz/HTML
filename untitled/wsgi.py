"""
为项目配置WSGI

它将WSGI可调用对象公开为'application'的模块变量
"""

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled.settings')

application = get_wsgi_application()
"""
import os
import sys

path = '/home/Angle-Zz/HTML'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'untitled.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
