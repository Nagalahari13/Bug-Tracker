from pydantic import BaseModel

class TicketCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str = "medium"
    project_id: int
    assignee_id: int | None = None

class TicketOut(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    project_id: int
    assignee_id: int | None

    class Config:
        orm_mode = True
