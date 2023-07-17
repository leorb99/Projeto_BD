import app.models
from mysql.connector import Error
from app.controllers import departamento_professor

class DepartamentoProfessorDAO():
    def create(self, cursor, dep_professor):
        sql = ("""INSERT INTO departamento_professor VALUES(%s, %s);""")
        try:
            insert = (dep_professor.fk_codDpto, dep_professor.fk_idProfessor)
            cursor.execute(sql, insert)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela departamento_professor: ", ex)

    def get(self, cursor, dep_professor):
        sql = """SELECT * FROM departamento_professor 
        WHERE fk_idProfessor=%s AND fk_codDpto=%s;"""
        try:
            select = (dep_professor.fk_codDpto, dep_professor.fk_idProfessor)
            cursor.execute(sql, select)
            result = cursor.fetchone()
            departamento_professor = departamento_professor.DepartamentoProfessor(*result)
            return departamento_professor
        except Error as ex:
            print("Falha ao localizar dados na tabela departamento_professor: ", ex)
    
    def getAll(self, cursor):
        sql = "SELECT * FROM departamento_professor;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            departamento_professor = [departamento_professor.DepartamentoProfessor(*dp) for dp in result]
            return departamento_professor
        except Error as ex:
            print("Falha ao localizar dados na tabela departamento_professor: ", ex) 
    