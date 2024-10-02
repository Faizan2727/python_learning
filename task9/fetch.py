import pymongo
dbconn = pymongo.MongoClient("mongodb://127.0.0.1:27017")

dbname = dbconn["mydb1"]
dbcollection = dbname["company"]

for i in dbcollection.find():
    print(i)

#https://www.w3schools.com/mongodb/mongodb_query_operators.php
