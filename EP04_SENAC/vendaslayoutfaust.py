import faust

class ItemVenda(faust.Record):
    produto: str
    qtd: int