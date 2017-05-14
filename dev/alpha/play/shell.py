# client
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "client.settings")
django.setup()

# user
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user.settings")
django.setup()