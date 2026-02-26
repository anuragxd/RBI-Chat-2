from dotenv import load_dotenv
load_dotenv()  # This loads your GROQ_API_KEY from the .env file

from fastapi import FastAPI
from backend.app.api.chat import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)