from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from depedencies import get_db

from .models import User
from .schema import Token, UserCreate, UserLogin

user_router = APIRouter()


@user_router.post("/signup")
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    user = User(username=user_data.username, email=user_data.email)
    user.hash_password(user_data.password)
    db.add(user)
    db.commit()
    return {"message": "User has been created"}


@user_router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if user is None or not user.verify_password(user_data.password):
        raise HTTPException(status_code=401, default="Invalid Credentials")
    token = user.generate_token()
    return Token(access_token=token, token_type="bearer")
