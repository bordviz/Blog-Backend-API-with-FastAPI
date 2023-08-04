from pydantic import BaseModel

class AddPermission(BaseModel):
    user_id: int
    role_id_for_user: int