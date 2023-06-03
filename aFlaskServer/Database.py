from pymongo import MongoClient
from DataSchema import makeSchema
def MongoP(received_array):
    
    myclient = MongoClient("mongodb+srv://Pixel:Pixel7788@cluster0.3dpfxx3.mongodb.net/mydb?retryWrites=true&w=majority")
    db_name = myclient["DB01"]
    Collection = db_name["Queries_added"]
    document=received_array
    # Insert the document into MongoDB
    print(document)
    Collection.insert_one(document)
    print("Pushed in mongo")
    myclient.close()
    

def MongoP1(received_array):
    
    myclient = MongoClient("mongodb+srv://Pixel:Pixel7788@cluster0.3dpfxx3.mongodb.net/mydb?retryWrites=true&w=majority")
    db_name = myclient["DB02"]
    Collection = db_name["Quoted_info"]
    
    document=makeSchema(received_array)
    
    # Insert the document into MongoDB
    print(document)
    Collection.insert_one(document)
    print("Pushed in mongo")
    myclient.close()