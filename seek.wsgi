import os
import sys
import site

app = str(__file__.split("/").pop().split(".").pop(0))
app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
virtual_dir = os.path.abspath(os.path.join(app_dir, "../"))
python_version = 'python%s' % sys.version[:3]
site_packages = os.path.join(virtual_dir, 'lib', python_version, 'site-packages')

# add current python env to dir
site.addsitedir(site_packages)

# put the Django project on sys.path
sys.path.insert(0, os.path.join(app_dir, app))
sys.path.insert(0, app_dir)
sys.path.insert(0, site_packages)

# bad hard coding
module = "eed.settings" 
os.environ["DJANGO_SETTINGS_MODULE"] = module

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

