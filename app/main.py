from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from .database import engine
from . import  models
from .routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    conn = psycopg2.connect(host='localhost', dbname='fastapi', user='postgres', password='admin123', cursor_factory=RealDictCursor)
    cur = conn.cursor()
except Exception as e:
    print(e)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

