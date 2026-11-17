class Pagamento:
    def calcular_valor_final(self, valor: float) -> float:
        raise NotImplementedError("Cada forma de pagamento deve implementar este método")

class PagamentoDebito(Pagamento):
    def calcular_valor_final(self, valor: float) -> float:
        return valor 

class PagamentoPix(Pagamento):
    def calcular_valor_final(self, valor: float) -> float:
        return valor * 0.95  

class PagamentoDinheiro(Pagamento):
    def calcular_valor_final(self, valor: float) -> float:
        return valor * 0.97  

class PagamentoCartao(Pagamento):
    def calcular_valor_final(self, valor: float) -> float:
        return valor * 1.05  