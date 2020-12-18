from repository.repo_user_sirc import UserSircRepo
from app_model.models import SircUser

userRepo = UserSircRepo()
users = userRepo.getAllUser()
for ele in users:
    print(ele.id)
    print(ele.username)
    print(ele.address)
    print(ele.password)
    print("===")

idMax = userRepo.getMaxId().id
print(idMax)
# =========insert by batch============#
listSircUser = []
sircUserAdd = SircUser(5,"Minh","abc123","HaiPhong")
sircUserAdd1 = SircUser(6,"Nghia","abc123","HaiPhong")
sircUserAdd2 = SircUser(7,"Son","abc123","HaiPhong")
listSircUser.append(sircUserAdd)
listSircUser.append(sircUserAdd1)
listSircUser.append(sircUserAdd2)
SircUser.objects.bulk_create(listSircUser)