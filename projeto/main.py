from fastapi import FastAPI
from projeto.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)
