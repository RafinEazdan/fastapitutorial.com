from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("Users", back_populates="blogs") #two way relation ship between two models or tables; here author and blogs can be found both way through user.blog or blog.user
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
