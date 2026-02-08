from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    content: str
    ticket_id: int

class CommentOut(BaseModel):
    id: int
    content: str
    ticket_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
