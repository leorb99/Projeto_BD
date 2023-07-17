import app.models
from mysql.connector import Error
from app.controllers import departamentos

class DepartamentoDAO():
    def create(self, cursor, departamento):
        sql = ("""INSERT INTO departamento VALUES(%s, %s);""")
        try:
            insert = (departamento.codigo, departamento.nome)
            cursor.execute(sql, insert)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela departamento: ", ex)

    def update(self, cursor, departamento):
        sql = ("""UPDATE departamento SET nome=%s WHERE codigo=%s;""")
        try:
            update = (departamento.codigo, departamento.nome)
            cursor.execute(sql, update)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao atualizar dados na tabela departamento: ", ex)
    
    def get(self, cursor, codigo):
        sql = "SELECT * FROM departamento WHERE codigo=%s;"
        try:
            cursor.execute(sql, (codigo,))
            result = cursor.fetchone()
            departamento = departamentos.Departamento(*result)
            return departamento
        except Error as ex:
            print("Falha ao localizar dados na tabela departamento: ", ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM departamento;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            departamento = [departamentos.Departamento(*d) for d in result]
            return departamento
        except Error as ex:
            print("Falha ao localizar dados na tabela departamento: ", ex) 
    