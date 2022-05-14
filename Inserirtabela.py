import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',  database='cadastro', user= 'root', password='lucas2003@')

    criar_tabela_SQL="""CREATE TABLE tbl_produtos (
                         IdProduto int(11) NOT NULL,
                         NomeProduto VARCHAR(70) NOT NULL,
                         Preco FLOAT NOT NULL,
                         Quantidade TINYint NOT NULL,
                         PRIMARY KEY (IdProduto)) """
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de Produtos criada com sucesso")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no MYSQL: {}" .format(erro))

finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão o MYSQL foi encerrada")
 
