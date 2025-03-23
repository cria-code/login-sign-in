from pydantic import BaseModel, EmailStr, Field
import ulid
from typing import Optional

class User (BaseModel):
    id: str = Field(default_factory=lambda: str(ulid.new()), description="User ID")
    google_id: str = Field(description="User Google ID")
    name: str = Field(description="User Name")
    given_name: Optional[str] = Field(None, description="User Given Name")
    family_name: Optional[str] = Field(None, description="User Family Name")
    email: EmailStr = Field(description="User Email")
    verified_email: bool = Field(description="Email Verified Status")
    picture: Optional[str] = Field(None, description="User Photo")
    # birthdate: Optional[str] = Field(None, description="User Birthdate")
    # gender: Optional[str] = Field(None, description="User Gender")
    

# from pydantic import BaseModel, EmailStr, Field
# import ulid


# class User(BaseModel):
#     id: str = Field(
#         default_factory=lambda: str(ulid.new()), description="User ID")
#     google_id: str = Field(description="User Google ID")
#     name: str = Field(description="User Name")
#     email: EmailStr = Field(description="User Email")
#     picture: str = Field(description="User Photo")
