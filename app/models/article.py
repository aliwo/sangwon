from __future__ import annotations

from typing import TYPE_CHECKING

from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.models.comment import Comment


class Article(BaseModel, Model):
    author = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)
    body = fields.TextField()

    comments: list[Comment]

    class Meta:
        table = "articles"

    @classmethod
    async def get_one_by_id(cls, id: str) -> Article:
        return await cls.get(id=id)
