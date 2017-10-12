import mysql.connector


class ConsultaBanco(object):

    def __init__(self, tabela, valor, minimo, maximo):
        self.cnx = mysql.connector.connect(user="root", password="1234", host="localhost", database="teste_back")
        self.valor = valor
        self.minimo = minimo
        self.maximo = maximo
        self.tabela = tabela

    # Consulta valor média do campo vl_total seguindo as condições:
    # vl_total > que valor
    # id_customer entre min e max

    def consultar_media(self):
        cursor = self.cnx.cursor()
        query = ("SELECT AVG(vl_total) FROM {} WHERE vl_total > {} AND id_customer "
                 "BETWEEN {} AND {};".format(self.tabela, self.valor, self.minimo, self.maximo))
        cursor.execute(query)
        resultado = cursor
        self.cnx.close()
        return resultado

    # Filtra e gera lista conforme condições abaixo:
    # vl_total > que valor
    # id_customer entre min e max
    def consultar_tabela(self):
        cursor = self.cnx.cursor()
        query = (
            "SELECT * FROM {} WHERE vl_total > {} AND id_customer BETWEEN {} AND "
            "{} ORDER BY vl_total asc;".format(self.tabela, self.valor, self.minimo, self.maximo))
        cursor.execute(query)
        resultado = cursor
        self.cnx.close()
        return resultado
