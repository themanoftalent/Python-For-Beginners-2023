from pymongo import  MongoClient

client = MongoClient()
db = client.pythontut


#result = db.student.insert([{"id":1, "name":"raunak"}, {"id":2, "name":"saurabh"}, {"id":3, "name":"kaushik"}])


def ret():
    for row in db.student.find({}):
        print(row)


def up():
    db.student.update({"id":3},{"$set":{"name":"mritunjay"}})


def dele():
    db.student.delete_many({})



def sch():
    db.student.drop()



sch()
#dele()
#up()
#ret()
client.close()