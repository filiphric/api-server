from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class UserResponse(BaseModel):
    # Keep aliases available for input parsing, but don't require/assume
    # Pydantic minor-version-specific config keys for serialization.
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    user_id: int
    user_name: str
    email: str
    is_active: bool
