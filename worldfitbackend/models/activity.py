from sqlalchemy import Column, Text, Integer, DateTime, ForeignKey

from worldfitbackend.models import Base

class Activity(Base):
    __tablename__ = 'activities'

    TYPES = ["steps", ]

    id = Column(Integer, primary_key=True, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    activity_type = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    value = Column(Integer, nullable=False)