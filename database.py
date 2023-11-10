from sqlalchemy import create_engine, Column, Integer, select, String, Boolean, Float
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
    can_take_calls = Column(Boolean, nullable=False)
    seats = Column(String, nullable=False)
    coffee_price = Column(String)
    float_coffee_price = Column(Float)


Base.metadata.create_all(engine)


class CafeDatabase:
    def __init__(self):
        self.session = Session(engine)
        self.convert_price_to_float()

    def get_all_cafes(self):
        result = self.session.execute(select(Cafe))
        all_cafes = result.scalars().all()
        return all_cafes

    def select_cafe(self, cafe_id):
        result = self.session.execute(select(Cafe).where(Cafe.id == cafe_id))
        cafe = result.scalar()
        return cafe

    def add_cafe(self, cafe):
        self.session.add(cafe)
        self.session.commit()

    def convert_price_to_float(self):
        cafes = self.session.execute(select(Cafe)).scalars().all()
        for cafe in cafes:
            try:
                split_price = cafe.coffee_price.split("£")
            except ValueError:
                pass
            else:
                float_price = float(split_price[1])
                cafe.float_coffee_price = float_price
                self.session.commit()
