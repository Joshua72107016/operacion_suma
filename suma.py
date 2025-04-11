class Suma:
    def __init__(self, operando1, operando2):  # <- CORRECTO
        self.operando1 = self._validar_operando(operando1)
        self.operando2 = self._validar_operando(operando2)

    def _validar_operando(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError(f"El valor '{valor}' no es un número válido (int o float).")
        return valor

    def calcularSuma(self):
        return self.operando1 + self.operando2
