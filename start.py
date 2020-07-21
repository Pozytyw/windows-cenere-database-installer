import base
import scrapper
import msvcrt as m

base.clear()

print("First step")
print("Create connection to database")
print("Make sure u have mysql database, user with have privileges to it and he using plugin mysql_native_password")
print("")
base.raw_print("Any key to continue ")
m.getch()

database = base.connect()

if base.create_schema(database):
    print("Operation end successfully")
    print("")
    print("Start webscraping")
    
    xx = "https://www.zalando.pl/odziez-damska"
    xy = "https://www.zalando.pl/odziez-meska/"

    scrapper.scrap(xx, "kobiety", database)
    scrapper.scrap(xy, "mezczyzni", database)
    
    
else:
    print("Error occur during creating schema")

