from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser toutes les origines (pour React)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Données fictives
countries = [
    {"name": "France", "flag": "🇫🇷"},
    {"name": "USA", "flag": "🇺🇸"},
    {"name": "Japan", "flag": "🇯🇵"}
]

@app.get("/message")
def get_message():
    return {"msg": "Bienvenue sur l’API !"}

@app.get("/countries")
def get_countries():
    return countries


