# Death class
class Death:
    def __init__(self, death):
        self.age = death
    
    def __str__(self):
        return 'Death: %s' % (self.age)