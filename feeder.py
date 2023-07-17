import mysql.connector
from mysql.connector import Error
import os
import csv
import time
import pickle

init = time.time()
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'login.txt')

with open(filename, "r") as f:
    user, password = f.readline().split()

dep = {}
disc = {}
profs = {}
turmas_dict = {}
profs_disc = {}
deps_prof = {}
path_dep = here + "/data/dep.pk1"
path_disc = here + "/data/disc.pk1"
path_profs = here + "/data/profs.pk1"
path_turmas_dict = here + "/data/turmas.pk1"
path_profs_disc = here + "/data/profs_disc.pk1"
path_deps_prof = here + "/data/deps_prof.pk1"


try:
    con = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database="AvaliaUnB"
        )
    
    if con.is_connected():
        cursor = con.cursor()

        with open(path_dep, "rb") as pf:
            dep = pickle.load(pf)
        with open(path_disc, "rb") as pf:
            disc = pickle.load(pf)
        with open(path_profs, "rb") as pf:
            profs = pickle.load(pf)
        with open(path_deps_prof, "rb") as pf:
            deps_prof = pickle.load(pf)
        with open(path_profs_disc, "rb") as pf:
            profs_disc = pickle.load(pf)
        with open(path_turmas_dict, "rb") as pf:
            turmas_dict = pickle.load(pf)
        
        # with open("dep.pk1", "wb") as pf:
        #     pickle.dump(dep, pf)
        # with open("disc.pk1", "wb") as pf:
        #     pickle.dump(disc, pf)
        # with open("profs.pk1", "wb") as pf:
        #     pickle.dump(profs, pf)
        # with open("deps_prof.pk1", "wb") as pf:
        #     pickle.dump(deps_prof, pf)
        # with open("profs_disc.pk1", "wb") as pf:
        #     pickle.dump(profs_disc, pf)
        # with open("turmas.pk1", "wb") as pf:
        #     pickle.dump(turmas_dict, pf)
        
        print("Inserindo dados na tabela departamento")
        for d in dep.items():
            insert = f"""INSERT INTO departamento VALUES ("{d[0]}", "{d[1]}");"""
            cursor.execute(insert)
            con.commit()
        
        print("Inserindo dados na tabela disciplina")
        for d in disc.items():
            insert = f"""INSERT INTO disciplina VALUES ("{d[0]}", "{d[1][0]}", "{d[1][1]}");"""
            cursor.execute(insert)
            con.commit()
            
        print("Inserindo dados na tabela professor")
        for p in profs.items():
            insert = f"""INSERT INTO professor VALUES ({p[0]}, "{p[1]}");"""
            cursor.execute(insert)
            con.commit()

        print("Inserindo dados na tabela professor_disciplina")
        for pd in profs_disc.keys():
            insert = f"""INSERT INTO professor_disciplina VALUES ("{pd[0]}", {pd[1]});"""
            cursor.execute(insert)
            con.commit()
            
        print("Inserindo dados na tabela departamento_professor")
        for dp in deps_prof.keys():
            insert = f"""INSERT INTO departamento_professor VALUES ("{dp[0]}", {dp[1]});"""
            cursor.execute(insert)
            con.commit()

        print("Inserindo dados na tabela turma")
        for t in turmas_dict.items():
            insert = f"""INSERT INTO turma VALUES ("{t[0][0]}", "{t[0][1]}", "{t[0][2]}", "{t[1][0]}", {t[1][1]}, {t[1][2]}, {t[0][3]}, "{t[1][3]}");"""
            cursor.execute(insert)
            con.commit()

        cursor.close()
        con.close()
    print("SUCESSO")
    print(f"{int((time.time()-init)/60)}:{int((time.time()-init)%60):02d}")

except Error as erro:
    cursor.execute("DROP DATABASE AvaliaUnB;")
    print(erro)
    print(f"{int((time.time()-init)/60)}:{int((time.time()-init)%60):02d}")
    con.commit()
    cursor.close()
    con.close()