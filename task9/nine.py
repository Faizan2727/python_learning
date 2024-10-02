# To access mongodb usning python we need pymongo library. Installing it using "pip install mongodb"

# Documnetation of pymongo-
# https://pymongo.readthedocs.io/en/stable/

# Now to connect the mongodb to python use the following function-

# dbconn = pymongo.MongoClient("mongodb://127.0.0.1:27017")

# pymongo.MongoClient: This is a class from the pymongo library used to create a client to the MongoDB server.
# "mongodb://127.0.0.1:27017": This is the connection string used to connect to the MongoDB server.
# mongodb://: This indicates that the protocol used is MongoDB.
# 127.0.0.1: This is the IP address for localhost, which means the MongoDB server is running on the same machine as the client.
# 27017: This is the default port on which MongoDB listens for connections

# To create Database-
# dbconn = dbconn["mydb"]

# To create a collection-
# dbcollection = dbname["company"]

# But it will show up until we insert an record.

# To insert a record-
# dbcollection.insert_one(
#    {
#       "cname": "IBM"
#       "location": "bang"
#   }
#   )

# To check its created use find_one function -
# dbcollection.find_one()

# Similarly we can insert as many records as we want .
# When we run here find() function to see all records it will give us here address 

# dbcollection.find()

# In every database, data is saved in hard disk . When we run find function it only gives address. We are able to see it in terminal because it is function of terminal. Here address is called cursor.
# To retrieve data here , we will use for loop.

# for i in dbcollection.find():
#           print(i)

# for i in dbcollection.find(): This loop iterates over each document returned by the find() method.
# Each document is assigned to the variable i during each iteration of the loop.
# print(i): This statement prints the current document (i) to the console.

#To insert multiple records use insert_many() function-

# dbcollection.insert_many(
#    {
#       "cname": "IBM"
#       "location": "bang"
#   },
#   {
#       "cname": "Redhat"
#       "location": "pune"
#   },
#   {
#       "cname": "Redhat"
#       "location": "pune"
#   }
#   )

# If we see now multiple records are inserted.
# for i in dbcollection.find():
#       print(i)

# Program That takes input fields form the user.
import pymongo
dbconn = pymongo.MongoClient("mongodb://127.0.0.1:27017")
myname = input("enter your name: ")
mycity = input("enter your name: ")

dbname = dbconn["mydb1"]
dbcollection = dbname["company"]

dbcollection.insert_one(
        {
            "name": myname,
            "location": mycity
        }
        )

