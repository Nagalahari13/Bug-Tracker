from fastapi import FastAPI
from app.database import Base, engine
from app.routes.auth_routes import router as auth_router
from app.routes.project_routes import router as project_router
from app.routes import project
from app.routes import ticket
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from app.routes import comment

app = FastAPI()

Base.metadata.create_all(bind=engine)

security = HTTPBearer()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Bug Tracker API",
        version="1.0",
        description="Jira-like Bug Tracking System",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi



app.include_router(auth_router)
app.include_router(project.router)
app.include_router(ticket.router)
app.include_router(comment.router)

@app.get("/")
def home():
    return {"message": "Bug Tracker API Running"}
