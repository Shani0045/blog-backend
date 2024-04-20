from sqlalchemy import BigInteger, Boolean, Column, Computed, DateTime, Identity, Integer, Numeric, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Blogs(Base):
    __tablename__ = 'blogs'
    __table_args__ = {'schema': 'blogms'}

    id = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    title = Column(Text)
    content = Column(Text)
    author_id = Column(Integer)
    category_id = Column(Integer)
    created_at = Column(Integer)
    updated_at = Column(Integer)

