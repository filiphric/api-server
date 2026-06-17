from pydantic import BaseModel


class UserResponse(BaseModel):
    user_id: int
    user_name: str
    email: str
    is_active: bool
