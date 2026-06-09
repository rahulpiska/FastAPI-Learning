# from database import SessionLocal
# from models import Post

# db = SessionLocal()

# post = db.query(Post).filter(Post.id == 6).first()

# print(post.owner.name,post.owner.id)


from utils import hash_password

print(hash_password("rahul123"))