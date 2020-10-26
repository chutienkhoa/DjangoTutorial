from django.db import models


# Create your models here.
class DrawTable(models.Model):
    column1 = models.CharField(max_length=250)
    column2 = models.CharField(max_length=200)


class UserModel(models.Model):
    model_name = models.CharField(max_length=250)
    user = models.CharField(max_length=250)
    accuracy = models.FloatField()

    def __str__(self):
        return self.model_name


class DataModel(models.Model):
    model_name = models.CharField(max_length=250)
    precision = models.FloatField()
    recall = models.FloatField()
    accuracy = models.FloatField()

    def __str__(self):
        return self.model_name + str(self.precision)

    def get_data_model_by_name(self, model_name):
        query = "SELECT * FROM repository_datamodel WHERE model_name = '{0}'".format(model_name)
        data_model = DataModel.objects.raw(query)
        # for model in data_model:
        #     print(model)
        return data_model

    @staticmethod
    def get_precision():
        return DataModel.precision