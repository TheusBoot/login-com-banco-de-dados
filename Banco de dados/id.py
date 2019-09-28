import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='loginmysql'
)

cursor = conexao.cursor()

cursor.execute(
    "CREATE TABLE cliente(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255))"
               )

