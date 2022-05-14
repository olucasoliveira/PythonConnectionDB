import mysql.connector

#Abrir conexão

conexao = mysql.connector.connect(host='localhost',
                                  database='cadastro',
                                  user= 'root',
                                  password='lucas2003@',
                                  autocommit=True)

#Criar um cursor


cursor = conexao.cursor()

#inserção
try:
    cursor.execute("UPDATE tbl_produtos SET nomeProduto ='Celular' where nomeProduto = 'Lucas' ")

except Exception as e:
    print(f"erro:{e}")


conexao.close()