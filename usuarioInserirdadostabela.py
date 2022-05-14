import mysql.connector
from mysql.connector import Error

print("Rotina para cadastro de produtos no banco de dados")
print("ENTRE COM OS DADOS")

idProd= input("ID do Produto: ")
nomeProd= input("NOme do Produto: ")
precoProd=input("Preço: ")
quantoProd=input("Quantidade: ")

dados = idProd + ',\'' + nomeProd + '\',' + precoProd + ',' + quantoProd + ')'
declaracao= """ Insert into tbl_produtos (IdProduto, NomeProduto, Preco, Quantidade)
VALUES ("""
sql= declaracao + dados
print(sql)
    

try:
    con = mysql.connector.connect(host='localhost',  database='cadastro', user= 'root', password='lucas2003@')

    inserir_produtos = sql
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "Registros inseridos na tabela")
    cursor.close()
except Error as erro:
    print("Falha ao criar tabela no MYSQL: {}" .format(erro))

finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão o MYSQL foi encerrada")
 
