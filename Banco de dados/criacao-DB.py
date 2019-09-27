import pymysql

#Criando a conexão com o serv

conexao = pymysql.connect(
    host= "localhost",
    user = 'root',
    passwd = ''
)

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE loginmysql")
