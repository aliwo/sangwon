from tortoise import fields


class BaseModel:
    id = fields.BigIntField(pk=True, max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
