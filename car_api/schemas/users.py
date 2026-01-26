from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    passwdord: str

class UserBasePublic(BaseModel):
    id: int
    username: str
    email: EmailStr

class userSchema(BaseModel):
    username: UserBase
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

class updateUserSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    
class UserListPublicSchema(BaseModel):
    users: List[UserPublicSchema]