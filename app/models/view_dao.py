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
        
    def view_pages(self, cursor, page, per_page):
        offset = (page - 1) * per_page
        sql = "SELECT * FROM view_turmas_avaliadas LIMIT %s OFFSET %s"
        try:
            cursor.execute(sql, (per_page, offset))
            result = cursor.fetchall()
            cursor.execute("SELECT COUNT(*) FROM view_turmas_avaliadas")
            total_results = cursor.fetchone()[0]
            return result, total_results
        except Error as ex:
            print("Falha ao carregar a view:", ex)