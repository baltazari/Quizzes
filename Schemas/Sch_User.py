from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    email: str
    birthday: str
    phone: str


class hash_pass(User):
    password: str


class Date(hash_pass):
    create_at: datetime = datetime.now().strftime("%d-%m-%y %H:%M")
    update_at: datetime = datetime.now().strftime("%d-%m-%y %H:%M")
