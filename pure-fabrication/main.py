class Order:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

class OrderPersistence:
    @staticmethod
    def save_to_file(order: Order):
        with open(f"{order.customer}_order.txt", "w") as f:
            f.write(f"Order for {order.customer}: ${order.total}")
        print("Order saved to file")

# Uso
order = Order("Alice", 250)
OrderPersistence.save_to_file(order)  # ✅ Ahora la persistencia está separada