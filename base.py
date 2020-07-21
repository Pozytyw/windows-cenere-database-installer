import mysql.connector
import msvcrt as m
import os
from mysql.connector import errorcode

def clear():
    os.system('cls')

def create_schema(database):
    #create cursor
    cursor = database.cursor(dictionary=True)
    try:
        print("Creating schema in database")
        #users table
        userQuerry = "CREATE TABLE `users` (`id` int NOT NULL AUTO_INCREMENT, `email` varchar(255) DEFAULT NULL, `password` varchar(255) DEFAULT NULL, `gender_id` int NOT NULL, PRIMARY KEY (`id`))"
        cursor.execute(userQuerry)
        #wallets table
        walletsQuerry = "CREATE TABLE `wallets` (`id` int NOT NULL AUTO_INCREMENT, `balance` decimal(10,2) DEFAULT NULL, `user_id` int NOT NULL, PRIMARY KEY (`id`))"
        cursor.execute(walletsQuerry)   
       #brands table
        brandsQuerry = "CREATE TABLE `brands` (`id` int NOT NULL AUTO_INCREMENT, `name` varchar(255) DEFAULT NULL, PRIMARY KEY (`id`))"
        cursor.execute(brandsQuerry)  
        #clothes table
        clothesQuerry = "CREATE TABLE `clothes` (`id` int NOT NULL AUTO_INCREMENT, `name` varchar(255) DEFAULT NULL, `img_src` varchar(255) DEFAULT NULL, `price` decimal(10,2) DEFAULT NULL, `gender_id` int NOT NULL, `type_id` int NOT NULL, `brand_id` int NOT NULL, PRIMARY KEY (`id`))"
        cursor.execute(clothesQuerry)  
        #gender table
        genderQuerry = "CREATE TABLE `gender` (`id` int NOT NULL AUTO_INCREMENT, `gender` varchar(50) DEFAULT NULL, PRIMARY KEY (`id`))"
        cursor.execute(genderQuerry) 
        genderQuerry = "INSERT INTO gender(gender) values ('kobiety'),('mezczyzni')"
        cursor.execute(genderQuerry) 
        #order_clothes table
        order_clothesQuerry = "CREATE TABLE `order_clothes` (`cloth_id` int NOT NULL, `user_id` int NOT NULL, `size` char(10) NOT NULL, `amount` int NOT NULL, `order_id` int NOT NULL)"
        cursor.execute(order_clothesQuerry) 
        #orders table
        ordersQuerry = "CREATE TABLE `orders` (`id` int NOT NULL AUTO_INCREMENT, `user_id` int NOT NULL, `total_price` decimal(10,2) NOT NULL, `paid` tinyint(1) DEFAULT NULL, PRIMARY KEY (`id`))"
        cursor.execute(ordersQuerry) 
        #type table
        typeQuerry = " CREATE TABLE `type` (`id` int NOT NULL AUTO_INCREMENT, `type` varchar(255) DEFAULT NULL, `gender_id` int NOT NULL, PRIMARY KEY (`id`))"
        cursor.execute(typeQuerry)
        return True
    except mysql.connector.Error as err:
        return False

def connect():
    #placeholders, default values
    host = "127.0.0.1"
    port = "3306"
    user = "root"
    password = "root"
    database = "cenere"
    
    #get values from users
    host = input_placeholder("host",host)
    port = input_placeholder("port",port)
    user = input_placeholder("user",user)
    password = input_placeholder("password",password)
    database = input_placeholder("database",database)
    
    #try to connect
    try:
        #clear console and print success
        clear()
        print("Try connect to database " + host + ":" + port + ", database: " + database + ", user: " + user)
        database = mysql.connector.connect(
            host = host,
            user = user,
            passwd = password,
            port = port,
            database = database
        )
        print("Connection successful")
        
        return database
    except mysql.connector.Error as err:
    #if user press enter, repet try connection 
        print("Press enter to repet, or any key to exit")
        key = m.getch()
        if key[0] == 13:
            return connect()
    return None

#print string before prompt
def raw_print(string):
    for char in string:
        m.putwch(char)

def input_placeholder(variableName, placeholder):
    clear()
    #print string before prompt and w8 for key
    raw_print(variableName + " : " + placeholder)  
    key = m.getch()
    
    #if key is enter
    if key[0] == 13:
        return placeholder
    #else clear connsole and use standard input for user value
    else:
        clear()
        input(variableName + " : ")