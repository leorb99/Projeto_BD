import app.models
from mysql.connector import Error
from app.controllers import usuarios

class UsuarioDAO():
    def create(self, cursor, usuario, foto):
        sql = (f"""INSERT INTO usuario VALUES("{usuario['matricula']}", "{usuario['nome']}", "{usuario['email']}", "{usuario['senha']}", "{usuario['curso']}", "{usuario['privilegio']}", "{usuario['dataNascimento']}", NULL, {foto});""")
        try:
            cursor.execute(sql)
            app.models.con.commit()
        except Exception as ex:
            print("Falha ao inserir dados na tabela usuários: ", ex)

    def update(self, cursor, usuario):
        sql = (f"""UPDATE usuario SET nome="{usuario['nome']}", email="{usuario['email']}", senha="{usuario['senha']}", curso="{usuario['curso']}" """
               f"""WHERE matricula="{usuario['matricula']}";""")
        try:
            cursor.execute(sql)
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

    def getAll(self, cursor):
        sql = "SELECT * FROM usuario;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            usuario = [usuarios.Usuario(*u) for u in result]
            return usuario
        except Error as ex:
            print("Falha ao localizar dados na tabela usuários: ", ex) 
    
    def get_pass(self, cursor, matricula):
        sql = "SELECT senha FROM usuario WHERE matricula=%s;"
        try:
            cursor.execute(sql, (matricula,))
            result = cursor.fetchone()
            return result
        except Error as ex:
            print("Falha ao localizar dados na tabela usuários: ", ex)
        