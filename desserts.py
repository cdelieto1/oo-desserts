"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'


    def __init__ (self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        #add the cupcake's name to the ditc as a key 
        self.cache[name] = self
    

    def add_stock(self, amount):

        self.qty = self.qty + amount


    def sell(self, amount):

        if self.qty == 0:
            print("Sorry, these cupcakes are sold out")
            return

        #stops it at zero    
        if self.qty < amount:
            self.qty = 0
            return        
         
        self.qty = self.qty - amount

    @staticmethod
    def scale_recipe(ingredients,amount):

        list_of_ingredients =[]
        
        for ingredients, qty in ingredients:
            list_of_ingredients.append((ingredients,qty*amount))

        return list_of_ingredients

    @classmethod
    def get(cls,name):
        if name not in cls.cache:
            print("Sorry, that cupcake doesn\'t exist")
            return
        else:
            return cls.cache[name]

class Brownie(Cupcake):
    """The bakery is finally ready to accept delivery orders for their delicious brownies! 

    They’ll need you to write a Brownie class. The specifications for Brownie are the almost 

    the same as the ones for Cupcake. The difference is that brownies come in one flavor (chocolate).

    Add a Brownie class to desserts.py. Hint: inheritance will make this task a lot easier!"""


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
