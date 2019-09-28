import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='loginmysql'
)
cursor = conexao.cursor()
cursor.execute("CREATE TABLE cliente_final(id INT(11) PRIMARY KEY AUTO_INCREMENT)")



