from fastapi import APIRouter
from models.user import UserResponse

router = APIRouter()


@router.get(
    "/api/users/{user_id}",
    response_model=UserResponse,
    response_model_by_alias=False,
)
async def get_user(user_id: int):
    return UserResponse(
        user_id=user_id,
        user_name="jane_doe",
        email="jane@example.com",
        is_active=True,
    )
