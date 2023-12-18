from common.marriage import Marriage
from common.purchase_house import Purchase_house
from common.childbearing import Childbearing
from common.retirement import Retirement
from common.death import Death


# life events of a person
class life_events:
    def __init__(self, marriage: Marriage, purchase_house: Purchase_house, childbearing: Childbearing, retirement: Retirement, death: Death):
        '''
        marriage: Marriage Class
        purchase_house: Purchase_house
        childbearing: Childbearing
        retirement: Retirement
        death: Death
        '''
        self.marriage = marriage
        self.purchase_house = purchase_house
        self.childbearing = childbearing
        self.retirement = retirement
        self.death = death
        assert self.marriage.age >= 22, 'Marriage age should be greater than 22.'
        assert self.childbearing.age >= 22, 'Childbearing age should be greater than 22.'
        assert self.retirement.age >= 55, 'Retirement age should be greater than 55.'
        # retirement age should be greater than marriage age and childbearing age and greater than purchase_house age and less than death age
        assert self.retirement.age > self.marriage.age, 'Retirement age should be greater than marriage age.'
        assert self.retirement.age > self.childbearing.age, 'Retirement age should be greater than childbearing age.'
        assert self.retirement.age > self.purchase_house.age, 'Retirement age should be greater than purchase_house age.'
        assert self.retirement.age < self.death.age, 'Retirement age should be less than death age.'
        
    def __str__(self):
        return 'Marriage: %s, Purchase_house: %s, Childbearing: %s, Retirement: %s' % (self.marriage, self.purchase_house, self.childbearing, self.retirement)

    def __dict__(self):
        return {'Marriage': self.marriage, 'Purchase_house': self.purchase_house, 'Childbearing': self.childbearing, 'Retirement': self.retirement}
    
    def __getitem__(self, key):
        return getattr(self, key)
