import pymongo


try:
	conn = pymongo.MongoClient()
	print("Connected successfully")
except pymongo.errors.ConnectionFailure as e:
	print("Could not connect to MongoDB: %s" % e)
db = conn.mydb
# print(db)
collection = db.my_collection
# print(collection)

doc = [{"name":"Miko","surname":"Koko","twitter":"@gorgeousAmbrella"},
 {"name":"Mikola","surname":"Koko","twitter":"@simpleambrella"}, 
 {"name":"Marisha","surname":"Zubka","twitter":"@zubkazubyn"}]

obj_id = collection.insert(doc)
# print(obj_id)
# print(conn.database_names())
# print(db.collection_names())

# one = collection.find_one()
# print(one)

# find_by_name = collection.find_one({"name":"Miko"})
# print("We've found: ", find_by_name)

# find_by_id = collection.find_one({"_id": obj_id.decode("utf-8")})

# print("We've found by id:", find_by_id)

find_all = collection.find()
print("find all type:",type(find_all))
find_all_count = find_all.count()
print("found:",find_all_count)

for i,a in enumerate(find_all):
	print(i,a)

all_miko = collection.find({"name":"Miko"})
all_miko_count = all_miko.count()
print("all miko count:", all_miko_count)
for i,a in enumerate(all_miko):
	print(i,a)

