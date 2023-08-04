from fastapi import APIRouter, Depends
from auth.auth import current_user
from database import get_async_session, AsyncSession
from auth.models import User
from admin.schemas import AddPermission
from sqlalchemy import update


router = APIRouter(
    prefix='/admin',
    tags=['Admin']
)

@router.put('/add-permission')
async def add_permision(
    body: AddPermission,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    if user.role_id != 2:
        return {
            'status': 'error',
            'message': 'You don\'t have permission to do this'
        }
    query = update(User).where(User.id == body.user_id).values(role_id=body.role_id_for_user)
    await session.execute(query)
    await session.commit()
    return {
        'status': 'success',
        'message': f'User {body.user_id} had a new role_id: {body.role_id_for_user}'
    }
