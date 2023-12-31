import app.models
from mysql.connector import Error
from app.controllers import avaliacoes

class AvaliacaoDAO():
    def create(self, cursor, avaliacao):
        sql = ("""INSERT INTO avaliacao 
               (comentario,nota,dificuldade,fk_matricula,fk_idProfessor,fk_periodo,fk_local,fk_horario)
               VALUES(%s, %s, %s, %s, %s, %s, %s, %s);""")
        try:
            insert = (avaliacao.comentario, avaliacao.nota, avaliacao.dificuldade, avaliacao.fk_matricula,
                      avaliacao.fk_idProfessor, avaliacao.fk_periodo, avaliacao.fk_local, avaliacao.fk_horario)
            cursor.execute(sql, insert)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela avaliação: ", ex)

    def update(self, cursor, avaliacao):
        sql = ("""UPDATE avaliacao SET comentario=%s, nota=%s, dificuldade=%s
               WHERE idAvaliacao=%s;""")
        try:
            update = (avaliacao.comentario, avaliacao.nota, avaliacao.dificuldade, avaliacao.id)
            cursor.execute(sql, update)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao atualizar dados na tabela avaliação: ", ex)

    def delete(self, cursor, idAvaliacao):
        sql = ("DELETE FROM avaliacao WHERE idAvaliacao=%s;")
        try:
            cursor.execute(sql, (idAvaliacao,))
            app.models.con.commit()
        except Error as ex:
            print("Falha ao deletar dados na tabela avaliação: ", ex)
    
    def get(self, cursor, idAvaliacao):
        sql = "SELECT * FROM avaliacao WHERE idAvaliacao=%s;"
        try:
            cursor.execute(sql, (idAvaliacao,))
            result = cursor.fetchone()
            avaliacao = avaliacoes.Avaliacao(*result)
            return avaliacao
        except Error as ex:
            print("Falha ao localizar dados na tabela avaliação: ", ex)

    def getProf(self, cursor, fk_idProfessor):
        sql = "SELECT * FROM avaliacao WHERE fk_idProfessor=%s;"
        try:
            cursor.execute(sql, (fk_idProfessor,))
            result = cursor.fetchone()
            avaliacao = avaliacoes.Avaliacao(*result)
            return avaliacao
        except Error as ex:
            print("Falha ao localizar dados na tabela avaliação: ", ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM avaliacao;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            avaliacao = [avaliacoes.Avaliacao(*a) for a in result]
            return avaliacao
        except Error as ex:
            print("Falha ao localizar dados na tabela avaliação: ", ex) 
    
    def getTurmas(self, cursor, avaliacao):
        sql = """SELECT * FROM avaliacao
                 WHERE fk_idProfessor=%s AND fk_periodo=%s AND fk_local=%s AND fk_horario=%s;"""
        try:
            insert = (avaliacao.fk_idProfessor, avaliacao.fk_periodo,
                      avaliacao.fk_local, avaliacao.fk_horario)
            cursor.execute(sql, insert)
            result = cursor.fetchall()
            avalia = [avaliacoes.Avaliacao(*a) for a in result]
            return avalia
        except Error as ex:
            print("Falha ao localizar dados na tabela avaliação: ", ex) 

    def getMy(self, cursor, fk_matricula):
        sql = "SELECT * FROM avaliacao WHERE fk_matricula=%s;"
        try:
            cursor.execute(sql, (fk_matricula,))
            result = cursor.fetchall()
            avaliacao = [avaliacoes.Avaliacao(*a) for a in result]
            return avaliacao
        except Error as ex:
            print("Falha ao localizar dados na tabela avaliação: ", ex) 