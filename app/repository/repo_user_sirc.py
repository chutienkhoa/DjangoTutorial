import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
django.setup()
from django.db import connection

from app_model.models import SircUser

class UserSircRepo:
    def __init__(self):
        pass

    def getAllUser(self):
        query = "SELECT * FROM sirc_user"
        return SircUser.objects.raw(query)

    def getMaxId(self):
        query = "SELECT * FROM sirc_user order by id DESC limit 1"
        return SircUser.objects.raw(query)[0]
