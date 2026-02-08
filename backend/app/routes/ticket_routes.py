from fastapi import APIRouter, Depends
from app.schemas.ticket import TicketCreate, TicketOut
from app.models.ticket import Ticket
from app.auth.deps import get_current_user
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=TicketOut)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        project_id=ticket.project_id,
        created_by=user.id
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket
