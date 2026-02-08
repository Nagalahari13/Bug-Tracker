from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.project import ProjectCreate, ProjectResponse
from app.models.project import Project
from app.auth.auth_bearer import get_current_user   # your JWT auth function

router = APIRouter(prefix="/projects", tags=["Projects"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProjectResponse)
def create_project(data: ProjectCreate, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    project = Project(name=data.name, description=data.description, owner_id=user["id"])
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    return db.query(Project).filter(Project.owner_id == user["id"]).all()
