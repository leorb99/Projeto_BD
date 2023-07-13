import app.models
from mysql.connector import Error
from app.controllers import turmas

class TurmaDAO():
    def create(self, cursor, turma):
        sql = (f"""INSERT INTO turma VALUES("{turma['periodo']}", "{turma['horario']}", "{turma['local']}", "{turma['numero']}", "{turma['vagasOcupadas']}", "{turma['totalVagas']}", "{turma['fk_idProfessor']}", {turma['fk_codDisciplina']});""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela turmas: ", ex)

    def update(self, cursor, turma):
        sql = (f"""UPDATE turma SET vagasOcupadas="{turma['vagasOcupadas']}", totalVagas="{turma['totalVagas']}", dificuldade="{turma['dificuldade']}" """
               f"""WHERE periodo="{turma['periodo']}" AND horario="{turma['horario']}" AND local="{turma['local']}" AND fk_idProfessor="{turma['fk_idProfessor']}";""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao atualizar dados na tabela turmas: ", ex)

    def delete(self, cursor, turma):
        sql = (f"""DELETE FROM turma WHERE periodo="{turma['periodo']}" AND horario="{turma['horario']}" AND local="{turma['local']}" AND fk_idProfessor="{turma['fk_idProfessor']}";""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao deletar dados na tabela turmas: ", ex)
    
    def get(self, cursor, turma):
        sql = f"""SELECT * FROM turma WHERE periodo="{turma['periodo']}" AND horario="{turma['horario']}" AND local="{turma['local']}" AND fk_idProfessor="{turma['fk_idProfessor']}";"""
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            turma_ = turmas.Turma(*result)
            return turma_
        except Error as ex:
            print("Falha ao localizar dados na tabela turmas: ", ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM turma;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            turma = [turmas.Turma(*t) for t in result]
            return turma
        except Error as ex:
            print("Falha ao localizar dados na tabela turmas: ", ex) 
    