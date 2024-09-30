from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

from app.models.base_model import BaseModel


class Article(BaseModel, Model):
    author = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)
    body = fields.TextField()

    class Meta:
        table = "articles"

    @classmethod
    async def get_one_by_id(cls, id: str) -> Article:
        return await cls.get(id=id)
