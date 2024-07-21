class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        return self.price * self.quantity
    
# Example usage:
if __name__ == "__main__":
    # Creating instances of Product
    product1 = Product("Egg", 15, 100)
    product2 = Product("Milk", 50, 400)
    product3 = Product("Water", 15, 300)
    
    # Calculate total value for each product
    total_value1 = product1.total_value()
    total_value2 = product2.total_value()
    total_value3 = product3.total_value()
    
    # Print out the details
    print(f'{product1.name}: Total value = {total_value1}')
    print(f'{product2.name}: Total value = {total_value2}')
    print(f'{product3.name}: Total value = {total_value3}')
