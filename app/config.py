import os

class Settings:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/products")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
