from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    login = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    notes = relationship("Note", backref="user")
    # new_pole = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f"User {self.user_id} ,Login: {self.login}, Notes: {self.notes}"


class Note(Base):
    __tablename__ = "Note"

    note_id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(Text)

    user_id = Column(Integer, ForeignKey("User.user_id"))
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()
    )

    def __repr__(self):
        return f"Note {self.note_id} for {self.user_id}, Title: {self.title}"
