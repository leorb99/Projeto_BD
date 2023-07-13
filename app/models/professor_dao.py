import app.models
from mysql.connector import Error
from app.controllers import professores

class ProfessorDAO():
    def create(self, cursor, professor):
        sql = (f"""INSERT INTO professor VALUES("{professor['nome']}", "{professor['fk_codDpto']}");""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela professor: ", ex)

    def get(self, cursor, codigo):
        sql = "SELECT * FROM professor WHERE idProfessor=%s;"
        try:
            cursor.execute(sql, (codigo,))
            result = cursor.fetchone()
            professor = professores.Professor(*result)
            return professor
        except Error as ex:
            print("Falha ao localizar dados na tabela professor: ", ex)
    
    def getNomeProf(self, cursor, nome):
        sql = "SELECT * FROM professor WHERE nome=%s;"
        try:
            cursor.execute(sql, (nome,))
            result = cursor.fetchone()
            professor = professores.Professor(*result)
            return professor
        except Error as ex:
            print("Falha ao localizar dados na tabela professor: ", ex)
    
    def getAll(self, cursor):
        sql = "SELECT * FROM professor;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            professor = [professores.Professor(*p) for p in result]
            return professor
        except Error as ex:
            print("Falha ao localizar dados na tabela professor: ", ex) 
    