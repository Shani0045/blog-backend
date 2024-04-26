from sqlalchemy import BigInteger, Boolean, Column, Computed, DateTime, Identity, Integer, Numeric, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'blogms'}

    id = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    name = Column(Text)
    created_at = Column(Integer)
