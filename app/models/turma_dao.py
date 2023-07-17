import app.models
from mysql.connector import Error
from app.controllers import turmas

class TurmaDAO():
    def create(self, cursor, turma):
        sql = ("""INSERT INTO turma
               VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""")
        try:
            insert = (turma.periodo, turma.horario, turma.local, turma.numero,
                      turma.vagasOcupadas, turma.totalVagas, turma.fk_idProfessor, 
                      turma.fk_codDisciplina,)
            cursor.execute(sql, insert)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela turmas: ", ex)

    def update(self, cursor, turma):
        sql = ("""UPDATE turma SET vagasOcupadas=%s, totalVagas=%s
               WHERE periodo=%s AND horario=%s AND local=%s AND fk_idProfessor=%s;""")
        try:
            update = (turma.vagasOcupadas, turma.totalVagas, turma.periodo, turma.horario, turma.local, turma.fk_idProfessor)
            cursor.execute(sql, update)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao atualizar dados na tabela turmas: ", ex)

    def delete(self, cursor, turma):
        sql = ("""DELETE FROM turma
               WHERE periodo=%s AND horario=%s AND local=%s AND fk_idProfessor=%s;""")
        try:
            delete = (turma.periodo, turma.horario, turma.local, turma.fk_idProfessor)
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao deletar dados na tabela turmas: ", ex)
    
    def get(self, cursor, turma):
        sql = """SELECT * FROM turma WHERE periodo=%s AND horario=%s AND local=%s AND fk_idProfessor=%s;"""
        try:
            select = (turma.periodo, turma.horario, turma.local, turma.fk_idProfessor)
            cursor.execute(sql, select)
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
    
    def getTurmas(self, cursor, codDisciplina):
        sql = """SELECT * FROM turma WHERE fk_codDisciplina=%s;"""
        try:
            cursor.execute(sql, (codDisciplina,))
            result = cursor.fetchall()
            turma = [turmas.Turma(*t) for t in result]
            return turma
        except Error as ex:
            print("Falha ao localizar dados na tabela turmas: ", ex) 
    
    def getDisciplina(self, cursor, idProfessor, horario, local, periodo):
        sql = """SELECT fk_codDisciplina FROM turma
                 WHERE periodo=%s AND horario=%s AND local=%s AND fk_idProfessor=%s"""
        try:
            consulta = (periodo, horario, local, idProfessor)
            cursor.execute(sql, consulta)
            result = cursor.fetchone()
            return result
        except Error as ex:
            print("Falha ao localizar dados na tabela turmas: ", ex) 