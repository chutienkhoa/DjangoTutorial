import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from repository.repo_model import UserModelRepo, DataModelRepo, DrawTableRepo

user_repo = UserModelRepo()
user_model = user_repo.get_user_model()
for ele in user_model:
    print(ele.user)
    print(ele.model_name)

data_model_repo = DataModelRepo()
data_model = data_model_repo.get_model_name_by_name("KNN")
for ele in data_model:
    print(ele.model_name)
    print(ele.id)
    print(ele.acc)

print("----Luc select phai co truogn key-")
data1 = data_model_repo.test2()
for ele in data1:
    print(ele.acc)
    print(ele.recall)

print("--tra ve tupple data, khong co ORM---")
raw_table = DrawTableRepo()
data2 = raw_table.get_raw_data()
for ele in data2:
    print(len(ele))