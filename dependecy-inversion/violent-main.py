class PayPalPayment:
    def pay(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")


class OrderProcessor:
    def __init__(self):
        self.payment = PayPalPayment()  # Violación de DIP: dependencia directa

    def process_order(self, amount: float):
        self.payment.pay(amount)


# Uso del sistema
order = OrderProcessor()
order.process_order(100.0)  # Solo puede procesar pagos con PayPal
