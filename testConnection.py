import mysql.connector
import test
from mysql.connector import errorcode

#connet to db
mydb = mysql.connector.connect(
    host="34.76.65.33",
    user="root",
    passwd="@Polko123",
    port="3306",
    database="ciuszek"
)

#create cursor
cursor = mydb.cursor(dictionary=True)
try:
    cursor.execute("select ID from gender where gender like \"kobiety\";")
except mysql.connector.Error as err:
    print("error " + err)
    exit(1)
x = cursor.fetchall()

for elem in x:
    print(x)