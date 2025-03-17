from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: str = Field(description="User Google ID")
    email: EmailStr = Field(description="User Email")
    verified_email: bool = Field(description="Email Verified Status")
    name: str = Field(description="User Name")
    given_name: str = Field(description="User Given Name")
    family_name: str = Field(description="User Family Name")
    picture: str = Field(description="User Photo")
