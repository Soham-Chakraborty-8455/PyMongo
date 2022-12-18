import pymongo

connectionString = "mongodb+srv://username:password@cluster0.gbfcu.mongodb.net/test"

# Inserting a Document
def insertDocument():
    studentInfo = {
        "name": "Soham Chakraborty",
        "enrollment": 2,
        "maths_marks": 35,
        "dsa_marks": 79
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(f"Student with id {student_id} has been created")


# Reading a Collection
def readDocuments():
    # Using find function 
    myStudents = collection.find({"enrollment": 1, "name": "Harry"})
    # print(myStudents)
    for student in myStudents:
        print(student)
    # Using findOne function 
    myStudent = collection.find_one({"enrollment": 1})
    print(myStudent) 

# Updating a Collection
def updateDocuments():
    collection.update_one({"enrollment": 1}, {'$inc': {'enrollment': 100}})
    collection.update_many({}, {'$inc': {'enrollment': 100}})

# Deleting a Collection
def deleteDocuments():
    r = collection.delete_one({"enrollment": 101})
    print(r.deleted_count)
    r = collection.delete_many({})
    print(r.deleted_count)
    collection.update_many({})



if __name__ == '__main__':
    client = pymongo.MongoClient(connectionString)
    # Creating a Database for a College
    db = client['IEM_Kolkata'] 

    # Creating a Collection
    collection = db.class1
    
    # CRUD

    #1. Create
    insertDocument()

    # 2. Read
    readDocuments()

    # 3. Update 
    updateDocuments()

    # 4. Delete 
    deleteDocuments()