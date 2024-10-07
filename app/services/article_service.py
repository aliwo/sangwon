from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.dtos.article_and_comments_response import (
    ArticleAndCommentsResponse,
    CommentResponse,
)
from app.models.article import Article


async def service_get_article_and_comments(article_id: str) -> ArticleAndCommentsResponse:
    article = await Article.filter(id=article_id).prefetch_related("comments").get_or_none()

    if not article:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"article {article_id} not found")

    return ArticleAndCommentsResponse(
        id=article.id,
        author=article.author,
        title=article.title,
        body=article.body,
        comments=tuple(
            CommentResponse(id=comment.id, author=comment.author, body=comment.body) for comment in article.comments
        ),
    )
