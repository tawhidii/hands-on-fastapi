from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from db import db_user


router = APIRouter(
  prefix='/user',
  tags=['user']
)

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
  return db_user.create_user(db, request)

# Read All users
@router.get('/', response_model=List[UserDisplay])
def get_all_user(db: Session = Depends(get_db)):
  return db_user.get_all_users(db)

# get user by id
@router.get('/{id}', response_model=UserDisplay)
def get_user_by_id(id:int, db: Session = Depends(get_db)):
  return db_user.get_user_by_id(db,id)

# Update user

@router.put('/{id}/update')
def get_user_by_id(id:int, request: UserBase,db: Session = Depends(get_db)):
  return db_user.update_user(db,id,request)
  
# Delete user
@router.delete('/{id}/delete')
def delte_user(id:int, db: Session = Depends(get_db)):
  return db_user.delete_user(db,id)
  

