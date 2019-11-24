# EP03_SENAC
# Executar os comandos para a execução do EP03.
docker-compose build
docker-compose up -d
docker exec -it hadoop bash

cd volume

hdfs dfs -mkdir ep03

hdfs dfs -mkdir ep03/input

hdfs dfs -mkdir ep03/output

# A planilha yellow_tripdata.csv criada uma quantidade menor de registro para não ultrapassar a limite da Maquina Virtual
hdfs dfs -put yellow_tripdata.csv ep03/input

# Somar total de cobranças por dia
python Ep03_01.py -r hadoop

# Tempo médio de corrida por dia em minutos
python Ep03_02.py -r hadoop

# Valor médio de corrida a cada 15 minutos
python Ep03_03.py -r hadoop
