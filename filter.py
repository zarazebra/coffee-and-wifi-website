from flask import request


class Filter:
    def __init__(self):
        self.calls = None
        self.sockets = None
        self.wifi = None
        self.toilet = None
        self.coffee_price_less_2 = None
        self.coffee_price_less_2_50 = None
        self.coffee_price_more_2_50 = None
        self.seats_0_10 = None
        self.seats_10_20 = None
        self.seats_20_30 = None
        self.seats_30_40 = None
        self.seats_40_50 = None
        self.seats_50_plus = None
        self.get_filters()

    def get_filters(self):
        self.calls = request.form.get("calls")
        self.sockets = request.form.get("sockets")
        self.wifi = request.form.get("wifi")
        self.toilet = request.form.get("toilet")
        self.seats_0_10 = request.form.get("seats_0-10")
        self.seats_10_20 = request.form.get("seats_10-20")
        self.seats_20_30 = request.form.get("seats_20-30")
        self.seats_30_40 = request.form.get("seats_30-40")
        self.seats_40_50 = request.form.get("seats_40-50")
        self.seats_50_plus = request.form.get("seats_50+")
        self.coffee_price_less_2 = request.form.get("price-less-2")
        self.coffee_price_less_2_50 = request.form.get("price-less-2.50")
        self.coffee_price_more_2_50 = request.form.get("price-more-2.50")
