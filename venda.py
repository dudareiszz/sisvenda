
        from datetime import datetime
from item_venda import Item_Venda
from produto import Produto
from pagamento import Pagamento

class Venda:
    _total_vendas = 0                                

    def __init__(self, pagamento: Pagamento, data_venda: datetime = datetime.now()):
        self._valor_total = 0.0
        self._data_venda = data_venda
        self._itens: list[Item_Venda] = []
        self._pagamento = pagamento
        Venda._total_vendas += 1                     


    @property
    def itens(self):
        return self._itens
    
    def adicionar_item(self, produto: Produto, quantidade: int):
        if produto.decrementar_estoque(quantidade):
            novo_item = Item_Venda(produto, quantidade)
            self._itens.append(novo_item)
            self._valor_total += novo_item.valor
            return True
        else:
            return False

    def remover_item(self, produto: Produto):
        for item in self._itens:
            if item.produto == produto:
                self._itens.remove(item)
                self._valor_total -= item.valor
                produto.incrementar_estoque(item.quantidade)
                return True
        return False

    def calcular_valor_total(self):
        # calculo total não é mais necessário aqui
        #self._valor_total = sum(item.valor for item in self._itens)
        return self._valor_total

    @property
    def pagamento(self):
        return self._pagamento

    @pagamento.setter
    def pagamento(self, pagamento: Pagamento):
        self._pagamento = pagamento

    def finalizar_venda(self):
        total = self.calcular_valor_total()
        valor_final = self._pagamento.calcular_valor_final(total)
        print(f"Forma de pagamento: {type(self._pagamento).__name__}")
        print(f"Total dos itens: R$ {total:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")
        return valor_final

    @staticmethod                                   
    def get_total_vendas():                          
        return Venda._total_vendas

