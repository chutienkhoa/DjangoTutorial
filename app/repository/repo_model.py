import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
django.setup()
from django.db import connection

from repository.models import UserModel, DataModel, DrawTable


class UserModelRepo:
    def __init__(self):
        pass

    def get_user_model(self):
        query = "SELECT * FROM repository_usermodel"
        return UserModel.objects.raw(query)


class DataModelRepo:
    def __init__(self):
        pass

    def get_model_name_by_name(self, name):
        # query = "SELECT model_name, accuracy FROM repository_datamodel WHERE model_name = '{0}'".format(name)
        return DataModel.objects.raw(
            "SELECT id, model_name, accuracy as acc FROM repository_datamodel WHERE model_name = %s",
            [name])

    def get_model_filter(self):
        return DataModel.objects.filter(accuracy__gt=1)

    def test2(self):
        return DataModel.objects.raw(
            "select a.id, a.accuracy as acc, b.recall from repository_usermodel a inner join repository_datamodel b on a.model_name = b.model_name")

class DrawTableRepo:
    def __init__(self):
        pass

    def get_raw_data(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM repository_drawtable"
            # query = "select a.accuracy as acc, b.recall from repository_usermodel a inner join repository_datamodel b on a.model_name = b.model_name"
            cursor.execute(query)
            row = cursor.fetchall()
        return row
