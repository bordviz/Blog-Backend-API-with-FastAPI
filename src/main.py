from fastapi import FastAPI
from auth.auth import fastapi_users, auth_backend
from auth.schemas import UserCreate, UserRead
from article.router import router as article_router
from admin.router import router as admin_router
from user.router import router as user_router
from auth.router import router as auth_router

app = FastAPI(
    title='BLOG API'
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(auth_router)
app.include_router(article_router)
app.include_router(admin_router)
app.include_router(user_router)
