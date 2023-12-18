# Marriage class
class Marriage:
    def __init__(self, marriage, location, tables, unit_price, ceremony, accommodation, wine, honeymoon, jewelry):
        # age of marriage
        self.age = marriage
        # location of wedding
        self.location = location
        # number of tables
        self.tables = tables
        # unit price of table
        self.unit_price = unit_price
        # ceremony
        self.ceremony = ceremony
        # accommodation
        self.accommodation = accommodation
        # wine
        self.wine = wine
        # honeymoon
        self.honeymoon = honeymoon
        # jewelry
        self.jewelry = jewelry
        self.sum = self.ceremony + self.accommodation + self.wine + self.honeymoon + self.jewelry + self.tables * self.unit_price

    def __str__(self):
        return 'Marriage: %s' % (self.age)

    def __dict__(self):
        return {'Marriage': self.age}

    def __getitem__(self, key):
        return getattr(self, key)