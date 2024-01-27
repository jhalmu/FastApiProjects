import uvicorn
from fastapi import FastAPI

from core.user.routes import user_router

# from database import Base, engine

app = FastAPI()

app.include_router(user_router, prefix="/user")

# Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=True)
