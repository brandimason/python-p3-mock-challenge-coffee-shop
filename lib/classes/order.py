
class Order:
    all= []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        
        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)

    '''getter/setter for price'''
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, int) and 1 <= value <= 10:
            self._price = value
        else:
            raise Exception("404 inside order setter")
        
    
    '''getter/setter for customer'''
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from classes.customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("404 inside customer Order setter")
        return self._customer


    '''getter/setter for coffee'''
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from classes.coffee import Coffee
        if isinstance(value, Coffee):
            from classes.coffee import Coffee
            self._coffee = value
        else:
            raise Exception("404 inside customer Order setter")
        return self._coffee