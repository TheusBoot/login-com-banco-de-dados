import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='loginmysql'
)
cursor = conexao.cursor()
cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)

#conexão Criada com Sucesso, a verificação foi bem Feita!

