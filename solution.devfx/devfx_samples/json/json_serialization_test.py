from dataclasses import dataclass
from typing import List
import datetime
from devfx.json import JsonSerializer
from devfx.json import JsonDeserializer

"""----------------------------------------------------------------
"""
# create classes order and prduct
@dataclass
class Product:
    name: str = None
    price: float = None

@dataclass
class OrderItem:
    product: Product = None
    quantity: int = None

@dataclass
class SpecialOrderItem(OrderItem):
    discount: int = None

@dataclass
class Order:
    date: datetime.date = None
    items: list[OrderItem] = None
    special_items: dict[str, SpecialOrderItem] = None
    list: List[int] = None

"""----------------------------------------------------------------
"""
# create a product
product = Product('Apple', 1.5)

# create an order item
order_item1 = OrderItem(product, None)
order_item2 = OrderItem(product, 5)

# create a special order item
special_order_item1 = SpecialOrderItem(product, 10, 5)
special_order_item2 = SpecialOrderItem(product, 15, 10)

# create a list of orders
order_list = [
    Order(date=datetime.date(2025, 2, 14), 
          items=[order_item1, order_item2], 
          special_items={'special_order_item1': special_order_item1, 'special_order_item2': special_order_item2},
          list=[1, 2, 3, 4, 5]),
    Order(date=datetime.date(2022, 3, 1), 
          items=[order_item1, order_item2], 
          special_items={'special_order_item1': special_order_item1, 'special_order_item2': special_order_item2},
          list=[6, 7, 8, 9, 10]),
]

"""----------------------------------------------------------------
"""
# serialize the order
orders_json = JsonSerializer.serialize(order_list)
print(orders_json)

orders = JsonDeserializer.deserialize(List[Order], orders_json)    
print(orders)
    
