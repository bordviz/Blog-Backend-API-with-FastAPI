from fastapi import APIRouter, Depends
from sqlalchemy import select, update
from database import AsyncSession, get_async_session
from auth.models import User
from auth.auth import current_user
from auth.schemas import UserRead
from .schemas import UserUpdate

router = APIRouter(
    prefix='/user',
    tags=["User"]
)

@router.get('/get-user', response_model=UserRead)
async def get_user_by_id(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    query = select(User).where(User.id == user.id)
    result = await session.execute(query)
    return result.scalar()

@router.put('/update-profile')
async def update_profile(
    body: UserUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    query = update(User).where(User.id == user.id).values(username=body.username)
    await session.execute(query)
    await session.commit()
    return {
        'status': 'success',
        'message': f'Username update to {body.username}'
    }