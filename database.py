import sqlitedict
dictionarydb = sqlitedict.SqliteDict("DBS2.db",autocommit=True)
Database=dictionarydb.get('Data',[])

username = "zandlex"
password = "admin"
name = "Erickson Dela Soledad"
age = "19"
sex = "Male"
loc = "Marikina City, Metro Manila, Philippines"
email ="Qzkmcruz@tip.edu.ph"
started = "November 26, 2000"
favloc = "REGION V"
contact = "09560594126"
for x in dictionarydb["Data"]:
    print(x)