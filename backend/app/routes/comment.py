from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentOut
from app.auth.auth_bearer import get_current_user, JWTBearer

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CommentOut)
def add_comment(
    data: CommentCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    new_comment = Comment(
        content=data.content,
        ticket_id=data.ticket_id,
        user_id=current_user["user_id"]
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/ticket/{ticket_id}")
def get_comments(ticket_id: int, db: Session = Depends(get_db)):
    return db.query(Comment).filter(Comment.ticket_id == ticket_id).all()
