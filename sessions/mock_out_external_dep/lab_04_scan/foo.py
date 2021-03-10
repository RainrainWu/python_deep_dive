class InnerTicker:
    inner_attr = 0


class Ticker:
    static_attr = 0
    inner_ticker = InnerTicker()

    def __init__(self):
        self.dynamic_attr = 0

    def add_one(self, num):
        self.my_attr = 0
        return num + 1
