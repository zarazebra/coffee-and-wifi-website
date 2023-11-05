from sqlalchemy import create_engine, Column, Integer, select, String, Boolean
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

engine = create_engine('sqlite:///cafes.db', echo=True)


class Base(DeclarativeBase):
    pass


class Cafe(Base):
    __tablename__ = "cafe"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    map_url = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    location = Column(String, nullable=False)
    has_sockets = Column(Boolean, nullable=False)
    has_toilet = Column(Boolean, nullable=False)
    has_wifi = Column(Boolean, nullable=False)
    can_take_calls = Column(Integer, nullable=False)
    seats = Column(String)
    coffee_price = Column(String)


Base.metadata.create_all(engine)


class CafeDatabase:
    def __init__(self):
        self.session = Session(engine)

    def get_all_cafes(self):
        result = self.session.execute(select(Cafe))
        all_cafes = result.scalars().all()
        return all_cafes

#    def add_new_cafe(self, cafe):
#        new_cafe = CafeDatabase(cafe)
#        self.session.add(new_cafe)
#        self.session.commit()
