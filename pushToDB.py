import mysql.connector
import test
from mysql.connector import errorcode

def addBrand(cursor, name):
    name.replace("'", "\\'")
    try:
        cursor.execute("insert into brands values(default, \""+name+"\");")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        cursor.close()
        exit(1)

def addCloth(cursor, name, price, gender_id, type_id, brand_id, img_src):
    name.replace("'", "\\'")
    if "'" in img_src or '"' in name:
        return;
    if not test.clothExist(cursor, name):
        try:
            cursor.execute("insert into clothes(name, price, gender_id, type_id, brand_id, img_src) values('"+name+"',"+str(price)+","+str(gender_id)+","+str(type_id)+"," + str(brand_id) + ",'" +img_src+"');")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            cursor.close()
            exit(1)
    else:
        print("skip " + name + " already exist")
        
def addType(cursor, type, gender_id):
    try:
        cursor.execute("insert into type values(default, \""+type+"\""+","+str(gender_id)+");")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        cursor.close()
        exit(1)
        
def push(type, gender, jsonList, mydb):
    #create cursor
    cursor = mydb.cursor(dictionary=True)
    
    #set gender id
    gender_id = test.getGenderID(cursor, gender)
    
    #check, if type isn't exist
    typeID = test.typeExist(cursor, type, gender_id)
    if typeID == -1:
        #add if isn't
        addType(cursor, type, gender_id)
        typeID = test.typeExist(cursor, type, gender_id)
        
    #get object list
    objectList = jsonList
    for elem in objectList:
        #set type for new cloth
        type_id = typeID
        #set name
        name = elem['name']
        name.replace("'","\\'")
        #set price
        price = elem['price']
        #set img src
        img_src = elem['img']   
        img_src.replace("'","\\'")
        
        elem['brand'] = elem['brand'].replace("'","\\'")
        #set brand id
        brand_id = test.getBrandID(cursor, elem['brand'])
        if brand_id == -1:
            #add to brands table, if doesn't contain brand
            addBrand(cursor, elem['brand'])
            print("Add new brand to database: " + elem['brand'])
            mydb.commit()
        brand_id = test.getBrandID(cursor, elem['brand'])
        addCloth(cursor, name, price, gender_id, type_id, brand_id, img_src)
            
    print("Add all for type: " + type)
    mydb.commit()
    cursor.close()