import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
django.setup()

from repository.models import UserModel

class UserModelRepo:
    def __init__(self):
        pass

    def get_user_model(self):
        query = "SELECT * FROM repository_usermodel"
        return UserModel.objects.raw(query)


