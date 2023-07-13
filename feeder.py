import mysql.connector
from mysql.connector import Error
import os
import csv

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'login.txt')

with open(filename, "r") as f:
    user, password = f.readline().split()
row_count = 0
try:
    con = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database="AvaliaUnB"
        )
    if con.is_connected():
        departamentos = here + "/data/2023.1/departamentos_2023-1.csv"
        disciplinas = here + "/data/2023.1/disciplinas_2023-1.csv"
        turmas = here + "/data/2023.1/turmas_2023-1.csv"
        cursor = con.cursor()

        with open(departamentos, "r") as f_dptos:
            dptos = csv.reader(f_dptos)
            next(dptos)
            for line in dptos:
                codigo, nome = line[0], line[1]
                row_count += 1
                insert = f"""INSERT INTO departamento VALUES ("{codigo}", "{nome}");"""
                # print(insert)
                cursor.execute(insert)
                con.commit()
    
    
        with open(disciplinas, "r") as f_disciplinas:
            disciplinas = csv.reader(f_disciplinas)
            next(disciplinas)
            for line in disciplinas:
                row_count += 1
                codigo, nome, cod_dpto = line[0], line[1], line[2]
                insert = f"""INSERT INTO disciplina VALUES ("{codigo}", "{nome}", "{cod_dpto}")"""
                # print(insert)
                cursor.execute(insert)
                con.commit()

        # with open(turmas, "r") as f_turmas:
        #     turmas = csv.reader(f_turmas)
        #     next(turmas)
        #     professor = {}
        #     for line in turmas:
        #         professor[line[2]] = line[8]
        # with open(turmas, "r") as f_turmas:
        #     turmas = csv.reader(f_turmas)
        #     next(turmas)
        #     for line in turmas:
        #         numero, periodo, professor, horario = line[0], line[1], line[2], line[3]
        #         vagas_ocupadas, total_vagas, local = line[4], line[5], line[6]
        #         cod_disciplinas, cod_dpto = line[7], line[8]
        #         insert_professor = f"""INSERT INTO professor VALUES ()"""
        #         insert_turma = f"""INSERT INTO turma
        #                      VALUES ("{periodo}", "{horario}", "{local}", {numero}, {vagas_ocupadas}, {total_vagas}, {id_professor}, "{cod_disciplinas}")"""
        #         cursor.execute(insert)
        #         con.commit()

        cursor.close()
        con.close()
except Error as erro:
    cursor.execute("DROP DATABASE AvaliaUnB;")
    con.commit()
    cursor.close()
    con.close()