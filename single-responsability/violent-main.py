class CalculadoraArea:
    def calcularArea(self, figura):
        if figura["tipo"] == "circulo":
            return 3.14 * figura["radio"] ** 2
        elif figura["tipo"] == "rectangulo":
            return figura["ancho"] * figura["alto"]