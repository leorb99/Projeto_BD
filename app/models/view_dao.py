from mysql.connector import Error


class View():
    def view(self, cursor):
        sql = "SELECT * FROM vw_avaliacoesDisciplina"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Error as ex:
            print("Falha ao carregar a view:", ex)