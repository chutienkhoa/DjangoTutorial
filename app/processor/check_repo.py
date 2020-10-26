import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from repository.repo_model import UserModelRepo

user_repo = UserModelRepo()
user_model = user_repo.get_user_model()
for ele in user_model:
    print(ele.user)
    print(ele.model_name)