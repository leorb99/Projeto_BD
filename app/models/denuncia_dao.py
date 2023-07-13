import app.models
from mysql.connector import Error
from app.controllers import denuncias

class DenunciaDAO():
    def create(self, cursor, denuncia):
        sql = (f"""INSERT INTO denuncia VALUES('NÃO AVALIADA', "{denuncia['motivo']}", "{denuncia['fk_matricula']}", "{denuncia['fk_idAvaliacao']}");""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela denúncia: ", ex)

    def update(self, cursor, denuncia):
        sql = (f"""UPDATE denuncia SET avaliado="{denuncia['avaliado']}" WHERE idDenuncia="{denuncia['idDenuncia']}";""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao atualizar dados na tabela denúncia: ", ex)
    
    def delete(self, cursor, idDenuncia):
        sql = ("DELETE FROM denuncia WHERE idDenuncia=%s;")
        try:
            cursor.execute(sql, (idDenuncia,))
            app.models.con.commit()
        except Error as ex:
            print("Falha ao deletar dados na tabela denuncia: ", ex)
    
    def get(self, cursor, idAvaliacao):
        sql = "SELECT * FROM denuncia WHERE idAvaliacao=%s;"
        try:
            cursor.execute(sql, (idAvaliacao,))
            result = cursor.fetchone()
            denuncia = denuncias.Denuncia(*result)
            return denuncia
        except Error as ex:
            print("Falha ao localizar dados na tabela denúncia: ", ex)

    def getNaoAvaliado(self, cursor, avaliado):
        sql = "SELECT * FROM denuncia WHERE avaliado='NÃO AVALIADA';"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            denuncia = denuncias.Denuncia(*result)
            return denuncia
        except Error as ex:
            print("Falha ao localizar dados na tabela denúncia: ", ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM denuncia;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            denuncia = [denuncias.Denuncia(*d) for d in result]
            return denuncia
        except Error as ex:
            print("Falha ao localizar dados na tabela denúncia: ", ex) 
    