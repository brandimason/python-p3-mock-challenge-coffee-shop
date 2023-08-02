#!/usr/bin/env python3
# import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    newOrder = Order(price=12)
    brandi = Customer("brandi")
    americano = Coffee(111)

    print(newOrder.price)

    # ipdb.set_trace()
