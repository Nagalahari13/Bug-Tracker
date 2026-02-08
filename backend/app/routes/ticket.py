from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.ticket import TicketCreate, TicketOut
from app.models.ticket import Ticket
from app.auth.auth_bearer import get_current_user

router = APIRouter(prefix="/tickets", tags=["Tickets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- CREATE TICKET -----------------------
@router.post("/", response_model=TicketOut)
def create_ticket(
    data: TicketCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    new_ticket = Ticket(
        title=data.title,
        description=data.description,
        priority=data.priority,
        project_id=data.project_id,
        assignee_id=data.assignee_id
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


# ------------------- GET ALL TICKETS ---------------------
@router.get("/")
def get_tickets(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return db.query(Ticket).all()


# ------------------- UPDATE TICKET STATUS ----------------
@router.put("/{ticket_id}/status")
def update_status(
    ticket_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        return {"error": "Ticket not found"}

    ticket.status = status
    db.commit()
    db.refresh(ticket)
    return {"message": "Status updated", "ticket": ticket}
