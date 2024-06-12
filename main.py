from fastapi import FastAPI
from routes.activities.controller import routes_activities

app = FastAPI()
app.include_router(routes_activities, prefix="/activities")