# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:46:31 2019

@author: kunal
"""
from json import dumps, loads


class Product:
    def __init__(self, name, price):
        self.name = name;
        self.price = price;

    def to_dict(self):
        return{'name':self.name, 'price': self.price}

def load_products():
    try:
        products_file = open('products.json', 'r+')
    except IOError:
        return []
    product_json = products_file.read()
    product_data = loads(product_json)

    products = []
    for product in product_data:
        products.append(Product(product['name'], product['price']))
    return products

def add_product(name, price):
    new_product = Product(name,price)
    products.append(new_product)

def list_products(products):
    for p in products:
        print('Product {} Price: ${}'.format(p.name, p.price))

def save_products(products):
    product_save_list = []
    for product in products:
        product_save_list.append(product.to_dict())

    products_file = open('products.json', 'w+')
    products_file.write(dumps(product_save_list))
    products_file.close()

products = load_products()
while True:
    choice = input('Please Enter add, list or quit: ')
    if choice == 'quit':
        print('You have entered quit!')
        save_products(products)
        break
    if choice == 'add':
        product_name = input('Enter product name: ')
        try:
            product_price = float(input('Enter product price: '))
        except ValueError:
            print('Invalid Data!!!')
            continue
        add_product(product_name, product_price)
    if choice == 'list':
        list_products(products)
    else:
        print('Invalid Command! Please again with add, list or quit')
