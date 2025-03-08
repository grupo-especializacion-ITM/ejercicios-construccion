class Order:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

    def save_to_file(self):
        with open(f"{self.customer}_order.txt", "w") as f:
            f.write(f"Order for {self.customer}: ${self.total}")
        print("Order saved to file")

# Uso
order = Order("Alice", 250)
order.save_to_file()  
