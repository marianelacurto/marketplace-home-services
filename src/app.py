import os

from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from src.api.models import db

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def home():
    return {"message": "Marketplace API running"}