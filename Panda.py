import mysql.connector
import pandas as pd

#CONEXÃO BASICA COM BANCO DE DADOS


conexao = mysql.connector.connect(host='localhost',
                                  database='cadastro',
                                  user='root',
                                  password='lucas2003@',
                                  autocommit=True)
#DEFININDO O CURSOR

cursor = conexao.cursor()

#EXECUTANDO O COMANDO MYSQL
cursor.execute('select * from pessoas')
view = cursor.fetchall()
variavel = pd.DataFrame(view)
print(variavel)


for view in cursor.fetchall():
    print(f"""{view[1]}
              {view[2]}
              {view[3]}
              {view[4]}
              {view[5]}
              
          """)

cursor.close()