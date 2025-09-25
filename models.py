from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String)
    age = Column(Integer, nullable=True)
    recommendations = Column(String)
    zip = Column(String, nullable=True)