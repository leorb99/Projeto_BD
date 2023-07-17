import app.models
from mysql.connector import Error
from app.controllers import professor_disciplina

class ProfDisciplinaDAO():
    def create(self, cursor, professor_disc):
        sql = ("""INSERT INTO professor_disciplina VALUES(%s, %s);""")
        try:
            insert = (professor_disc.fk_codDisciplina, professor_disc.fk_idProfessor)
            cursor.execute(sql, insert)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela professor_disciplina: ", ex)

    def get(self, cursor, professor_disc):
        sql = """SELECT * FROM professor_disciplina 
                 WHERE fk_idProfessor=%s AND fk_codDisciplina=%s;"""
        try:
            select = (professor_disc.fk_idProfessor, professor_disc.fk_codDisciplina)
            cursor.execute(sql, select)
            result = cursor.fetchone()
            prof_disciplina = professor_disciplina.ProfDisciplina(*result)
            return prof_disciplina
        except Error as ex:
            print("Falha ao localizar dados na tabela professor_disciplina: ", ex)
    
    def getAll(self, cursor):
        sql = "SELECT * FROM professor_disciplina;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            professor_disciplina = [professor_disciplina.ProfDisciplina(*p) for p in result]
            return professor_disciplina
        except Error as ex:
            print("Falha ao localizar dados na tabela professor_disciplina: ", ex) 
    