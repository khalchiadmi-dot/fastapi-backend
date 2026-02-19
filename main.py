from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/message")
def get_message():
    return {"msg": "Bienvenue sur lâ€™API !"}

@app.get("/countries")
def get_countries():
    return [
        {"name": "France", "flag": "í·«í··"},
        {"name": "USA", "flag": "í·ºí·¸"},
        {"name": "Japan", "flag": "í·¯í·µ"}
    ]
