from produto import Produto
from venda import Venda
from pagamento import PagamentoDebito, PagamentoPix, PagamentoDinheiro, PagamentoCartao

formas = [PagamentoDebito(), PagamentoPix(), PagamentoDinheiro(), PagamentoCartao()]

for forma in formas:
    mouse = Produto(descricao="mouse", preco_unitario=100, estoque=5)
    pendrive = Produto(descricao="pendrive", preco_unitario=50, estoque=5)

    venda = Venda(pagamento=forma)
    venda.adicionar_item(produto=mouse, quantidade=1)
    venda.adicionar_item(produto=pendrive, quantidade=2)

    venda.finalizar_venda()
    print("-" * 30)
    
    print(f"Total de vendas no sistema: {Venda.get_total_vendas()}")
