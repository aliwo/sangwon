from pydantic import BaseModel


class CommentResponse(BaseModel):
    id: str
    author: str
    body: str


class ArticleAndCommentsResponse(BaseModel):
    id: str
    author: str
    title: str
    body: str
    comments: tuple[CommentResponse, ...]
