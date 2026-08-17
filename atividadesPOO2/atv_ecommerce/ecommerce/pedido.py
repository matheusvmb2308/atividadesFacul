from ecommerce.item_pedido import ItemPedido


class Pedido:

    def __init__(self) -> None:
        self._itens: list[ItemPedido] = []
        self._status = "criado"

    @property
    def itens(self) -> list[ItemPedido]:
        return list(self._itens)

    @property
    def status(self) -> str:
        return self._status

    def adicionar_item(self, produto: "Produto", quantidade: int) -> None:
        if self._status != "criado":
            raise ValueError("Não é possível adicionar itens a um pedido já finalizado")
        preco_no_momento = produto.preco
        self._itens.append(ItemPedido(produto, quantidade, preco_no_momento))

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self._itens)

    def quantidade_itens(self) -> int:
        return len(self._itens)