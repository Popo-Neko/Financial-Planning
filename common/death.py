# Death classw
class Death:
    def __init__(self, death):
        self.age = death
    
    def __str__(self):
        return 'Death: %s' % (self.age)
    
    # describe all attributes
    def describe(self):
        print('Death: %s' % (self.age))