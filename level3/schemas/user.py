from pydantic import BaseModel, Field, EmailStr

class CreateUser(BaseModel):
    name : str = Field(min_length=3)
    email : EmailStr
    age : int = Field(gt=0,lt=20)