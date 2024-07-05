import mysql.connector as connector;

con = connector.connect(host='localhost',
        port='3306',
        user='root',
        password='Root123#',
        database='project1');
print('connection established');