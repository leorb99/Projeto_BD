import app.models
from mysql.connector import Error
from app.controllers import disciplinas

class DisciplinaDAO():
    def create(self, cursor, disciplina):
        sql = (f"""INSERT INTO disciplina VALUES("{disciplina['codigo']}", "{disciplina['nome']}", "{disciplina['fk_codDpto']}");""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela disciplina: ", ex)

    def update(self, cursor, disciplina):
        sql = (f"""UPDATE disciplina SET nome="{disciplina['nome']}" """
               """WHERE codigo="{disciplina['codigo']}";""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao atualizar dados na tabela disciplina: ", ex)
    
    def get(self, cursor, codigo):
        sql = "SELECT * FROM disciplina WHERE codigo=%s;"
        try:
            cursor.execute(sql, (codigo,))
            result = cursor.fetchone()
            disciplina = disciplinas.Disciplina(*result)
            return disciplina
        except Error as ex:
            print("Falha ao localizar dados na tabela disciplina: ", ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM disciplina;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            disciplina = [disciplinas.Disciplina(*d) for d in result]
            return disciplina
        except Error as ex:
            print("Falha ao localizar dados na tabela disciplina: ", ex) 
    