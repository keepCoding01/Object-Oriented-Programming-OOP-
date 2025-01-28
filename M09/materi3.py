"""A separate class for Item"""
class Item:
    """Constructor function wth price and discount"""
    def __init__(self, price, discount_strategy = None):
        """take price and discount strategy"""

        self.price = price
        self.discount_strategy = discount_strategy

    """A separate function for price after discount"""

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount
    
    def __repr__(self):
        statement = "price : {}, price after discount"
        return statement.format(self.price, self.price_after_discount())
    
    """function dedicated to On Sale Discount"""
    def on_sale_discount(order):
        return order.price * 0.25 + 20
    
    """function dedicated to 20% discount"""
    def twenty_percent_discount(order):
        return order.price * 0.20
    