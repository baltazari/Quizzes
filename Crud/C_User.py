from datetime import datetime

from Models import User
from Schemas import Sch_User
from sqlalchemy.orm import Session
from Utilites import Hash_Pass


def create_user(db: Session, user: Sch_User.hash_pass):
    new_user = User.User(
        user_name=user.user_name,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone,
        password=Hash_Pass.hash_pass(user.password),
        create_at=datetime.now().strftime("%d-%m-%y %H:%M"),
        update_at=datetime.now().strftime("%d-%m-%y %H:%M"),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
