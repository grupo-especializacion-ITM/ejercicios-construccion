from abc import ABC, abstractmethod


# Interfaz que define el contrato de los métodos de pago
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


# Implementación de PayPal
class PayPalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")


# Otra implementación: Pago con tarjeta de crédito
class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Processing credit card payment of ${amount:.2f}")


# OrderProcessor ahora depende de la abstracción, no de una implementación concreta
class OrderProcessor:
    def __init__(self, payment_method: PaymentMethod):  # ✅ Aplicación de DIP
        self.payment = payment_method

    def process_order(self, amount: float):
        self.payment.pay(amount)


# Uso del sistema
paypal_payment = PayPalPayment()
credit_card_payment = CreditCardPayment()

order1 = OrderProcessor(paypal_payment)  # Usando PayPal
order1.process_order(100.0)

order2 = OrderProcessor(credit_card_payment)  # Usando Tarjeta de Crédito
order2.process_order(50.0)
