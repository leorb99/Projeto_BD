import app.models
from mysql.connector import Error
from app.controllers import usuarios

class UsuarioDAO():
    def create(self, cursor, usuario, foto):
        sql = """INSERT INTO usuario 
                (matricula, nome, email, senha, curso, privilegio, dataNascimento, foto) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"""
        try:
            insert = (usuario.matricula, usuario.nome, usuario.email, usuario.senha, 
                      usuario.curso, usuario.privilegio, usuario.dataNascimento, foto)
            cursor.execute(sql, insert)
            app.models.con.commit()
        except Exception as ex:
            print("Falha ao inserir dados na tabela usuários: ", ex)

    def update(self, cursor, usuario, foto):
        sql = ("""UPDATE usuario SET nome=%s, email=%s, senha=%s, curso=%s, foto=%s
               WHERE matricula=%s;""")
        try:
            update = (usuario.nome, usuario.email, usuario.senha, usuario.curso, 
                      foto, usuario.matricula)
            cursor.execute(sql, update)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao atualizar dados na tabela usuários: ", ex)

    def delete(self, cursor, matricula):
        sql = ("DELETE FROM usuario WHERE matricula=%s;")
        try:
            cursor.execute(sql, (matricula,))
            app.models.con.commit()
        except Error as ex:
            print("Falha ao deletar dados na tabela usuários: ", ex)
    
    def get(self, cursor, matricula):
        sql = "SELECT * FROM usuario WHERE matricula=%s;"
        try:
            cursor.execute(sql, (matricula,))
            result = cursor.fetchone()
            if result != None:
                usuario = usuarios.Usuario(*result)
                return usuario
            usuario = None
            return usuario
        except Error as ex:
            print("Falha ao localizar dados na tabela usuários: ", ex)
    
    def get_email(self, cursor, email):
        sql = "SELECT * FROM usuario WHERE email=%s;"
        try:
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if result != None:
                usuario = usuarios.Usuario(*result)
                return usuario
            usuario = None
            return usuario
        except Error as ex:
            print("Falha ao localizar dados na tabela usuários: ", ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM usuario;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            usuario = [usuarios.Usuario(*u) for u in result]
            return usuario
        except Error as ex:
            print("Falha ao localizar dados na tabela usuários: ", ex) 
    
    def getPassword(self, cursor, matricula):
        sql = "SELECT senha FROM usuario WHERE matricula=%s;"
        try:
            cursor.execute(sql, (matricula,))
            result = cursor.fetchone()
            return result
        except Error as ex:
            print("Falha ao localizar dados na tabela usuários: ", ex)
        