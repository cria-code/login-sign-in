from pydantic import BaseModel, EmailStr, Field
import ulid

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(ulid.new()), description="User ID")
    google_id: str = Field(description="User Google ID")
    name: str = Field(description="User Name")
    given_name: str = Field(None, description="User Given Name")
    family_name: str = Field(None, description="User Family Name")
    email: EmailStr = Field(description="User Email")
    verified_email: bool = Field(description="Email Verified Status")
    picture: str = Field(None, description="User Photo")
    
