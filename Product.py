class Product:
    def __init__(self,product_name, price):
        '''
        make a constructor for Profuct class which includes
        :param product_name:
        :param price:will be overrode later in the main program
        '''
        self.product_name = product_name
        self.price = price


    def __str__(self):
        '''
        Implement method made to improve user experience with shopping
         by giving both name and price
        :return:
        '''
        return f"{self.product_name}'s price is ${self.price}"

