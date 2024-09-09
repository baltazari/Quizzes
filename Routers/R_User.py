from Crud import C_User
from Data.Db_Conection import SessionLocal, engine
from Dependencies import get_db
from fastapi import APIRouter, Depends
from Models import User
from Schemas import Sch_User
from sqlalchemy.orm import Session

User.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/create_user")
async def create_user(user: Sch_User.hash_pass, db: Session = Depends(get_db)):
    return C_User.create_user(db=db, user=user)
