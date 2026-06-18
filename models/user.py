from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class UserResponse(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
    )

    user_id: int
    user_name: str
    email: str
    is_active: bool
