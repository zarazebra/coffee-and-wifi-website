from sqlalchemy import create_engine, Column, Integer, select, String, Boolean, Float, or_
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

    def show_filtered_cafes(self, filtering):
        query = (select(Cafe)
                 .filter(or_(filtering.calls is None, Cafe.can_take_calls == filtering.calls))
                 .filter(or_(filtering.sockets is None, Cafe.has_sockets == filtering.sockets))
                 .filter(or_(filtering.wifi is None, Cafe.has_wifi == filtering.wifi))
                 .filter(or_(filtering.toilet is None, Cafe.has_toilet == filtering.toilet))
                 .filter(or_(filtering.coffee_price_less_2 is None, Cafe.float_coffee_price < filtering.coffee_price_less_2))
                 .filter(or_(filtering.coffee_price_less_2_50 is None, Cafe.float_coffee_price < filtering.coffee_price_less_2_50)
                 .filter(or_(filtering.coffee_price_more_2_50 is None, Cafe.float_coffee_price > filtering.coffee_price_more_2_50)
                 .filter(or_(filtering.seats_0_10 is None, Cafe.seats == filtering.seats_0_10))
                 .filter(or_(filtering.seats_10_20 is None, Cafe.seats == filtering.seats_10_20))
                 .filter(or_(filtering.seats_20_30 is None, Cafe.seats == filtering.seats_20_30))
                 .filter(or_(filtering.seats_30_40 is None, Cafe.seats == filtering.seats_30_40))
                 .filter(or_(filtering.seats_40_50 is None, Cafe.seats == filtering.seats_40_50))
                 .filter(or_(filtering.seats_50_plus is None, Cafe.seats == filtering.seats_50_plus)))))

        filtered_cafes = self.session.execute(query).scalars().all()
        return filtered_cafes
