from fastapi import APIRouter

from app.dtos.article_and_comments_response import ArticleAndCommentsResponse
from app.services.article_service import service_get_article_and_comments

router = APIRouter(prefix="/v1/articles", tags=["Article"], redirect_slashes=False)


@router.get("/{article_id}", response_model=ArticleAndCommentsResponse)
async def router_get_article_and_comments(article_id: str) -> ArticleAndCommentsResponse:
    return await service_get_article_and_comments(article_id)
