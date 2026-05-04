from pydantic import BaseModel, Field, EmailStr, model_validator
# from typing import Optional
class CreateUser(BaseModel):
    name : str = Field(min_length=3)
    email : EmailStr
    age : int = Field(gt=0,lt=20)

class UpdateUser(BaseModel):
    name : str | None = Field(default=None, min_length=3) 
    email : EmailStr | None = None
    age : int | None = Field(default=None,gt=0,lt=20) 
    @model_validator(mode="after")
    def check_not_empty(self):
        if not any([self.name, self.email, self.age]):
            raise ValueError("At least one field must be provided")
        return self

    # Core principle (real-world REST APIs)

    # Reject invalid request structure first, then validate existence and business rules.
    Why first?

# Because:

# This is a request format problem
# You don’t even need to touch storage/file/db
# It saves unnecessary I/O