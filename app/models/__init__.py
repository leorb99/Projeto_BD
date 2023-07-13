import mysql.connector
import os

path_login = os.path.dirname(os.path.abspath(__file__)) + "/../../"
filename = os.path.join(path_login, 'login.txt')

with open(filename, "r") as f:
    user, password = f.readline().split()

con = mysql.connector.connect(host="localhost", user=user, password=password, database="AvaliaUnB")
cursor = con.cursor()
