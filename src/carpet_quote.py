from math import ceil


class CarpetQuote(object):
    def __init__(self, length, width, price_per_sqr_mtr, round_up):
        self.round_up = round_up
        self.price_per_sqr_mtr = price_per_sqr_mtr
        self.width = width
        self.length = length

    def quote(self):
        area = self.length * self.width
        if self.round_up:
            area = ceil(area)
        return area * self.price_per_sqr_mtr