import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv
import os



app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")