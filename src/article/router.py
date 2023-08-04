from typing import List
from fastapi import APIRouter, Depends
from database import AsyncSession, get_async_session
from auth.auth import current_user
from auth.models import User
from article.schemas import ArticleCreate, ArticleRead, ArticleReadShort, CommentCreate
from article.models import Article, Comment
from sqlalchemy import insert, select, update

router = APIRouter(
    prefix='/article',
    tags=['Article']
)

class Limit:
    def __init__ (self, limit: int = 10, start:int = 1):
        self.limit = limit
        self.start = start

@router.post('/create')
async def create_article(
    article: ArticleCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    if user.role_id != 2 and user.is_verified == False:
        return {
            'status': 'error',
            'message': 'You don\'t have permission to do this'
        }
    article.author_id = user.id
    query = insert(Article).values(article.model_dump())
    await session.execute(query)
    await session.commit()
    return {
            'status': 'success',
            'message': 'Add new article'
        }

@router.get('/get-article/{article_id}')
async def get_article_by_id(
    article_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    article = select(Article).where(Article.id == article_id)
    response_article = await session.execute(article)
    comments_query = select(Comment).where(Comment.article_id == article_id)
    respone_comments = await session.execute(comments_query)
    result: ArticleRead = response_article.scalar()
    result.comments = respone_comments.scalars().all()
    return result



@router.get('/all-articles', response_model=List[ArticleReadShort])
async def get_articles(
    limit: Limit = Depends(Limit),
    session: AsyncSession = Depends(get_async_session)
) -> List[ArticleReadShort]:
    query = select(Article).where(Article.id >= limit.start).order_by(Article.id.desc()).limit(limit.limit)
    result = await session.execute(query)
    return result.scalars().all()

@router.post('/add-comment')
async def add_comment(
    body: CommentCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    if user.is_verified == False:
        return {
            'status': 'error',
            'message': 'You are not a verified user'
        }
    body.author_id = user.id
    query = insert(Comment).values(**body.model_dump())
    await session.execute(query)
    await session.commit()
    return {
        'status': 'success',
        'comment': body
    }

@router.post('/add-view')
async def add_view(
    article_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    if user.is_verified == False:
        return {
            'status': 'error',
            'message': 'You are not a verified user'
        }
    query = update(Article).where(Article.id == article_id).values(views=Article.views+1)
    await session.execute(query)
    await session.commit()
    return {
        'status': 'success',
        'message': 'Add new view'
    }

@router.post('/add-like')
async def add_like(
    article_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    if user.is_verified == False:
        return {
            'status': 'error',
            'message': 'You are not a verified user'
        }
    query = update(Article).where(Article.id == article_id).values(likes=Article.likes+1)
    await session.execute(query)
    await session.commit()
    return {
        'status': 'success',
        'message': 'Add new like'
    }

@router.post('/add-dislike')
async def add_dislike(
    article_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    if user.is_verified == False:
        return {
            'status': 'error',
            'message': 'You are not a verified user'
        }
    query = update(Article).where(Article.id == article_id).values(dislikes=Article.dislikes+1)
    await session.execute(query)
    await session.commit()
    return {
        'status': 'success',
        'message': 'Add new dislike'
    }

@router.post('/search-article/{value}', response_model=List[ArticleReadShort])
async def search_article(
    value: str,
    session: AsyncSession = Depends(get_async_session)
):
    query = select(Article).where(Article.title.like(f'%{value}%'))
    result = await session.execute(query)
    return result.scalars().all()