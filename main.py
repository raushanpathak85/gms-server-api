from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException, RequestValidationError
from pg_db import database
from config import settings
from routers.users import router as users_router
from routers.employees import router as employees_router
from routers.roles import router as roles_router
from routers.projects import router as projects_router
from routers.tasks_monitor import router as tasks_router
from routers.dashboard import router as dashboard_router
from errors import (
    http_error_handler,
    validation_exception_handler,
    unhandled_exception_handler,
)

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

##--------------------------------##
ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:3000",      # React dev server
    "http://127.0.0.1:3000",
    # add your deployed frontend origin(s) here when ready
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    ##allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,                   # keep False if you don't use cookies
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], # allow all HTTP methods
    allow_headers=["*"],                        # add others if you send them
)
##---------------------------------##

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("🚀 App starting...")
    yield
    # Shutdown logic
    print("🛑 App shutting down...")

# ✅ Connect on startup
@app.on_event("startup")
async def startup():
    await database.connect()

# ✅ Disconnect on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

## ---------------- USER ENDPOINTS ----------------

app.include_router(users_router, prefix="/api")
    
## ---------------- EMPLOYEE ENDPOINTS ----------------

app.include_router(employees_router, prefix="/api")

## ------------------------------------Roles Endpoints-----------------------------

app.include_router(roles_router, prefix="/api")

## ------------------------------------Projects Endpoints-----------------------------

app.include_router(projects_router, prefix="/api")

## ------------------------------------Task Monitors Endpoints-----------------------------

app.include_router(tasks_router, prefix="/api")

## ------------------------------------Dashboard Endpoints-----------------------------

app.include_router(dashboard_router, prefix="/api")
