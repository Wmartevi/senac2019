# EP04_SENAC
EP04 - Stream de Dados


1.Subir os containers

	docker-compose up -d

2.Iniciar o serviço de stream

	docker-compose run processor bash

3.O processor possui métodos para enviar informação para a stream utilizando valores randomicos que está comentado no vendas.py

3.1.Realizar os seguintes comandos para Envio de informações para a stream:

	faust -A venda send vendasA '{"produto":"LARANJA","qtd":"3","valor":"3.43"}'

	faust -A venda send vendasA '{"produto":"MILHO","qtd":"2","valor":"2.40"}'


4.Endereços para visualizar as informações da stream em rotas

4.1.Realiza a contagem de vendas em R$ do último 1 minuto (sliding)

	localhost:6066/rs_1_min/valor_1min


4.2.rRealiza a Contagem de vendas em quantidade de cada 2 minutos (tumbling)

	localhost:6066/qtd_2_min/qtd_2_min
