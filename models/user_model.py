from pydantic import BaseModel, EmailStr, Field
import ulid


class User(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ulid.new()), description="User ID")
    google_id: str = Field(description="User Google ID")
    name: str = Field(description="User Name")
    email: EmailStr = Field(description="User Email")
    picture: str = Field(description="User Photo")
