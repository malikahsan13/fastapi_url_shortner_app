from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi.responses import RedirectResponse
import string
import random

DATABASE_URL = "sqlite://urls.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class URL(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    original_url=Column(String, unique=True, nullable=False)
    short_code = Column(String, unique=True, index=True, nullable=False)
    
Base.metadata.create_all(bind=engine)

class URLRequest(BaseModel):
    original_url: HttpUrl
    
class URLResponse(BaseModel):
    original_url: str
    short_code: str
    short_url: str

    class Config:
        orm_mode = True