# Faz consultas no Banco de dados
from database import ConsultaBanco
# Formatar dados em tabelas
from tabulate import tabulate

# Parametros (tabela, valor, minimo, maximo)
db = ConsultaBanco("tb_customer_account", 560, 1500, 2700)

# Parametros para montar lista de usuarios
tb_header = ['ID', 'CPF/CNPJ', 'NOME', 'STATUS', 'VALOR TOTAL R$']
tb_data = db.consultar_tabela()

# Imprime resultado da consulta na tabela
print(tabulate(tb_data, tb_header, tablefmt="psql", numalign="center", stralign="center"))

print(tabulate(db.consultar_media(),
               headers=['MÉDIA DO VALOR TOTAL (R$)'], tablefmt="psql", floatfmt=".2f", numalign="center", stralign="center"))