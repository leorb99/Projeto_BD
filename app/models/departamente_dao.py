import app.models
from mysql.connector import Error
from app.controllers import departamentos

class DepartamentoDAO():
    def create(self, cursor, departamento):
        sql = (f"""INSERT INTO departamento VALUES("{departamento['codigo']}", "{departamento['nome']}");""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela departamento: ", ex)

    def update(self, cursor, departamento):
        sql = (f"""UPDATE departamento SET nome="{departamento['nome']}" WHERE codigo="{departamento['codigo']}";""")
        try:
            cursor.execute(sql)
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
    