#Alteração de tabela.

import pymysql

conexao = pymysql.connect(
    host='',
    user='root',
    passwd='',
    databse='loginmysql'
)
'''
    Cursor de colocação de alteração de dados
'''
cursor = conexao.cursor()

cursor.execute(
    "ALTER TABLE cliente ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
               )
