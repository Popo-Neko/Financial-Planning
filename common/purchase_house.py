from func import mortgage


# purchase house class
class Purchase_house:
    def __init__(self, purchase_house, location, area, price, down_payment_ratio, mortgage_ir, renovation, furniture, appliances):
        # age of purchase house
        self.age = purchase_house
        # location of house
        self.location = location
        # area of house
        self.area = area
        # price of house
        self.price = price
        # unit price of house
        self.unit_price = price / area
        # down payment ratio
        self.down_payment = down_payment_ratio
        # down payment
        self.down_payment = price * down_payment_ratio
        # loan
        self.loan = price - self.down_payment
        # interest rate
        self.interest_rate = mortgage_ir
        # renovation
        self.renovation = renovation
        # furniture
        self.furniture = furniture
        # appliances
        self.appliances = appliances
        # monthly mortgage
        self.monthly_mortgage = mortgage(self.loan, self.interest_rate, 30)
        
    def __str__(self):
        return 'Purchase_house: %s' % (self.age)