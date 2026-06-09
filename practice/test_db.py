# from database import sessionlocal
# from models import User

# db = sessionlocal()

# # new_user = User(
# #     name="pawan",
# #     email="kalyan@email.com"
# # )

# # db.add(new_user)

# # db.commit()
# # db.refresh(new_user)

# # print(new_user.id)
# # print(new_user.name)
# # print(new_user.email)

# #===========QUERY DATA==============
# # users = db.query(User).all()


# # for user in users:
# #     print(user.id,user.name,user.email)


# #=========QUERY DATA FIRST()=========

# # user = db.query(User).first()

# # print(user.email)

# #==========filter============
# #1
# # user = db.query(User).filter(User.id == 2).first()

# # print(user.id,user.name)

# #2
# # users = db.query(User).filter(User.name== 'Rahul').all()

# # for user in users:
# #     print(user.id, user.name)


# #===============update===========
# # user = db.query(User).filter(User.id == 1).first()

# # user.name = "srikanth"

# # db.commit()
# # db.refresh(user)

# # print(user.name)

# #==============delete===================
# # user = db.query(User).filter(User.id == 2).first()

# # if not user:
# #     print("user not found")

# # else:
# #     db.delete(user)
# #     db.commit()

# #     print('Deleted')



#==============testing=======================================================
# from utils import create_access_token

# token = create_access_token({'user_id':1})

# print('token=',token)


from utils import create_access_token, verify_access_token

token = create_access_token(
    {"user_id": 15}
)

print(
    verify_access_token(token)
)