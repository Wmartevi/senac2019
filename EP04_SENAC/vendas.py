import faust
import json
from datetime import timedelta
from random import randrange

class ItemVenda(faust.Record, serializer='json'):
    produto: str
    qtd: int
    valor: float

app = faust.App(
    'vendas',
    broker='kafka://kafka:9092'
)

venda_topic = app.topic('vendasE', value_type=ItemVenda)
rs_table = app.Table('rsE', default=int).hopping(60,120, expires=timedelta(minutes=10), key_index=True)
qtd_table = app.Table('qtdE', default=int).tumbling(timedelta(minutes=2),expires=timedelta(hours=1))

@app.agent(venda_topic)
async def contar_rs_qtd_venda(info):
    async for venda in info:
        dados = json.loads(venda)
        rs_table['valor_1min'] += (dados.valor * dados.qtd)
        qtd_table['qtd_2_min'] += dados.qtd

#@app.timer(interval=1.0)
#async def exemplo_venda(app):
#    await contar_rs_qtd_venda.send(
#        value=ItemVenda(produto='LARANJA',qtd=randrange,valor='3.43')
#    )

#@app.timer(2.0, on_leader=True)
#async def vender():
#    valor = ItemVenda(produto='MILHO',qtd=randrange,valor='2.40')
#    await contar_rs_qtd_venda.send(value=valor)

#if __name__ == '__main__':
#    app.main()   

@app.page('/rs_1_min/{page}')
@app.table_route(table=rs_table, match_info='page')
async def get_rs(web, request, page):
    return web.json({
        page: rs_table[page],
    })

@app.page('/qtd_2_min/{page}')
@app.table_route(table=qtd_table, match_info='page')
async def get_qtd(web, request, page):
    return web.json({
        page: qtd_table[page],
    })

