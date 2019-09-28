import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='loginmysql'
)

cursor = conexao.cursor()


element_sql = "INSERT INTO cliente(nome,email) VALUES(%s,%s)"

valor = ('Matheus','Matheus@hotmail.com')

cursor.execute(element_sql, valor)

conexao.commit()

print(cursor.rowcount,"Inserida com sucesso")
