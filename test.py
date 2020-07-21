import mysql.connector
from mysql.connector import errorcode

#type test
def typeExist(cursor, type, gender_id):
    try:
        cursor.execute("select ID from type where type like \""+type+"\" and gender_id = "+str(gender_id)+";")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        exit(1)
    x = cursor.fetchall()
    if cursor.rowcount == 0:
        return -1
    else:
        return x[0]['ID']
#brand test
def getBrandID(cursor, brand):
    brand.replace("'", "\\'")
    try:
        cursor.execute("select ID from brands where name like \""+brand+"\";")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        exit(1)
    x = cursor.fetchall() 
    if cursor.rowcount == 0:
        return -1
    else:
        return x[0]['ID']
#gender test
def getGenderID(cursor, gender):
    try:
        cursor.execute("select ID from gender where gender like \""+gender+"\";")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        exit(1)
    x = cursor.fetchall();
    if cursor.rowcount == -1:
        exit(1)
    else:
        return x[0]['ID']
#cloth exist
def clothExist(cursor, img_src):
    try:
        cursor.execute("select name from clothes where img_src like '"+img_src+"';")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        exit(1)
    x = cursor.fetchall()
    if cursor.rowcount == 0:
        return False
    return True