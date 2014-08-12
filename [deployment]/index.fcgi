#!/usr/bin/python
import sys, os

# Add a custom Python path. (optional)
#TODO: cahnge the django and libraries to /usr/local/lib/python2.7/dist-packages/django-1.6.5/

sys.path.insert(0, "/home/malek/sites/")
sys.path.insert(0, "/home/malek/sites/aka/")
sys.path.insert(0, "/home/malek/Lib/django.1.2/")


# Switch to the directory of your project.
os.chdir("/var/www/portal/")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "your.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
