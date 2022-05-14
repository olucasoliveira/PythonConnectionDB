import mysql.connector

#Abrir conexão

conexao = mysql.connector.connect(host='localhost',
                                  database='cadastro',
                                  user= 'root',
                                  password='*******',
                                  autocommit=True)

#Criar um cursor

cursor = conexao.cursor()

#inserção
try:
    cursor.execute("INSERT INTO pessoas (nome) values ('Maria')")

except Exception as e:
    print(f"erro:{e}")


conexao.close()
