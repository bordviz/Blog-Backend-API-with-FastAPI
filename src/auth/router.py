from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from mail.sender import send_email_report_dashboard
from .models import User, Verify
from .auth import current_user
from .schemas import VerifySend
from database import AsyncSession, get_async_session
from random import randint
from sqlalchemy import delete, insert, select, update

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.get('/send-verify-mail')
async def send_vefify_mail(
    background_tasks: BackgroundTasks,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    code = randint(100000, 999999)
    delete_code = delete(Verify).where(Verify.user_id == user.id)
    await session.execute(delete_code)
    await session.commit()
    verify = {
        'user_id': user.id,
        'code': code
    }
    query = insert(Verify).values(verify)
    await session.execute(query)
    await session.commit()
    background_tasks.add_task(send_email_report_dashboard, user.username, user.email, code)
    return {
        'status': 'success',
        'message': 'Email has been sent to you'
    }

@router.post('/send-verify-code')
async def send_verify_code(
    body: VerifySend,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    try:
        if user.is_verified == True:
            return {
                "status": "error",
                "message": 'You have allready been verified'
            }
        query = select(Verify).where(Verify.user_id == user.id)
        result = await session.execute(query)
        code = result.scalar().code
        if code == body.code:
            verify = update(User).where(User.id == user.id).values(is_verified=True)
            await session.execute(verify)
            await session.commit()
            return {
                "status": "success",
                "message": 'You have successfully verified'
            }
        else:
            return {
                "status": "error",
                "message": 'The code is incorrect'
            }
    except AttributeError:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "details": 'You do not have an active verification code'
        })