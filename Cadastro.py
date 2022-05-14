import mysql.connector
import pandas as pd

conexao = mysql.connector.connect(host='localhost',
                                  database='cadastro',
                                  user='root',
                                  password='senha',
                                  autocommit=True)
cursor = conexao.cursor()

print(" ===================== CADASTRO  =========================")

ask = int(input("""
        ESCOLHA UMA OPÇÃO:
        [1] CADASTRAR NOVOS USUARIOS
        [2] CONSULTAR USUARIOS CADASTRADOS
        
        A opção escolhida é: """))

while ask == 1 or 2:
    if ask == 1:
        try:
            nome = str(input("NOME:"))
            idade = int(input("IDADE SOMENTE NUMERO: "))
            sexo = str(input("SEXO (H/M):  "))
            peso = float(input("PESO: "))
            altura = float(input("ALTURA: "))
            nacionalidade = str(input("NACIONALIDADE: "))
            print("=" * 60)
            print(f"""
            OS DADOS INFORMADOS SÃO:
            NOME:{nome}
            IDADE:{idade}
            SEXO: {sexo}
            PESO: {peso}
            ALTURA: {altura}
            NACIONALIDADE:{nacionalidade}""")
            confirmation = int(input("""
            DESEJA CONFIRMAR O CADASTRO ?"
            [1] SIM
            [2] NÃO
            A OPÇÃO ESCOLHIDA É : """))
            if confirmation == 1:
                # INSERINDO AS VARIAVEIS NO BANCO DE DADOS

                sql = """INSERT INTO pessoas (nome, idade, peso, sexo, altura, nacionalidade)  
                        VALUES (%s, %s, %s, %s, %s, %s)"""
                sql_data = (nome, idade, peso, sexo, altura, nacionalidade)
                cursor.execute(sql, sql_data)

                print("=" * 60)
                print("            USUARIO CADASTRADO COM SUCESSO             ")
                print("=" * 60)

                ask = int(input("""
                    ESCOLHA OUTRA OPÇÃO:
                    [1] CADASTRAR NOVOS USUARIOS
                    [2] CONSULTAR CADASTRO
                    [3] SAIR

                    A opção escolhida é: """))
            else:
                print("=" * 60)
                ask = int(input("""

                    ESCOLHA OUTRA OPÇÃO:
                    [1] CADASTRAR NOVOS USUARIOS
                    [2] CONSULTAR CADASTRO
                    [3] SAIR

                    A opção escolhida é: """))
        except:
            print("=" * 60)
            print("""    
        ESSA INSERÇÃO DE DADOS NÃO É ACEITA NO CAMPO
        TENTE NOVAMENTE
        """)
            print("=" * 60)
            ask=1


    elif ask == 2:

#SCRIPT PARA EXIBIR OS REGISTROS DA TABELA

        cursor.execute("select * from pessoas")
        view= cursor.fetchall()
        table= pd.DataFrame(view)
        print(table)
        print("="*60)
        ask = int(input("""
        ESCOLHA OUTRA OPÇÃO:
        [1] CADASTRAR NOVOS USUARIOS
        [2} CONSULTAR USUARIOS NOVAMENTE
        [3] SAIR
        
        A opção escolhida é: """))

    elif ask==3:
        break

    elif ask != 1 or 2 or 3:
        ask = int(input("""Opção invalida !
                    
        ESCOLHA UMA OPÇÃO:
        [1] CADASTRAR NOVOS USUARIOS
        [2] CONSULTAR CADASTRO
        [3] SAIR
        
        A opção escolhida é: """))


print("="*60)
print("PROGRAMA ENCERRADO")
cursor.close()
