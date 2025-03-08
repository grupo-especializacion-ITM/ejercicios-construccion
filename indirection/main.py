from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CardPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing card payment of ${amount}")

class PayPalPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class OrderService:
    def __init__(self, payment_processor: IPaymentProcessor):
        self.payment_processor = payment_processor  

    def place_order(self, amount):
        print("Order placed!")
        self.payment_processor.process_payment(amount)  

# Uso del sistema
order_service1 = OrderService(CardPaymentProcessor())
order_service1.place_order(100)

order_service2 = OrderService(PayPalPaymentProcessor())
order_service2.place_order(200)
