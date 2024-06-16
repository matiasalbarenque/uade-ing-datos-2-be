from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth.auth_controller import router as auth_router
from .users.users_controller import router as users_routes
from .activities.activities_controller import router as activities_routes
from .projects.projects_controller import router as projects_routes
from .tasks.tasks_controller import router as tasks_routes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/auth")
app.include_router(users_routes, prefix="/users")
app.include_router(activities_routes, prefix="/activities")
app.include_router(projects_routes, prefix="/projects")
app.include_router(tasks_routes, prefix="/tasks")