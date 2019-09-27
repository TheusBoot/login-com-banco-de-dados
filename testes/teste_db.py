import pymysql

conexão = pymysql.connect(
    host='localhost',
    user='root',
    passwd=''
)
cursor = conexão.cursor()
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)
   
    
"""
     Ao executar esse teste, deve voltar essa resposta, esse teste faz a connect
     direito com o banco de dados e realizade uma chamada para ver todos os
     elemento aparecerem;
     
('information_schema',)
('mysql',)
('performance_schema',)
('phpmyadmin',)
('test',)

"""