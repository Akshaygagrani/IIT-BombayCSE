import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'form_siteB/settings')

import django
django.setup()

# Fake population script

import random
from info_app,models import faculty_form
from faker import Faker

fakegen = Faker() 
