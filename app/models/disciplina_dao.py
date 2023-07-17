import app.models
from mysql.connector import Error
from app.controllers import disciplinas

class DisciplinaDAO():
    def create(self, cursor, disciplina):
        sql = ("""INSERT INTO disciplina VALUES(%s, %s, %s);""")
        try:
            insert = (disciplina.codigo, disciplina.nome, disciplina.codDpto)
            cursor.execute(sql, insert)
            app.models.con.commit()
        except Error as ex:
            print("Falha ao inserir dados na tabela disciplina: ", ex)

    def update(self, cursor, disciplina):
        sql = ("""UPDATE disciplina SET nome=%s"
                  WHERE codigo=%s;""")
        try:
            update = (disciplina.nome, disciplina.codigo)
            cursor.execute(sql, update)
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
    
    def getNome(self, cursor, codigo):
        sql = "SELECT nome FROM disciplina WHERE codigo=%s;"
        try:
            cursor.execute(sql, codigo)
            result = cursor.fetchone()
            return result
        except Error as ex:
            print("Falha ao localizar dados na tabela disciplina: ", ex)