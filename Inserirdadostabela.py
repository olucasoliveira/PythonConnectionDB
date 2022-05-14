import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',  database='cadastro', user= 'root', password='******')

    inserir_produtos =""" Insert into tbl_produtos
                            (IdProduto, NomeProduto, Preco, Quantidade)
                            VALUES
                            (1, 'camera', 850.00, 5),
                            (2, 'Monitor', 630.00, 7),
                            (3, 'Relogio', 575.00, 10)"""
    
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
 
