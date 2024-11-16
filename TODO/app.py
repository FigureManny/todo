from tinydb import TinyDB, Query

db = TinyDB('./db.json')
user = Query()

while True:
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    
    userinput = input("enter your command ")
    
    if userinput == '1':
        name = input("name: ")
        age = input("age: ")
        db.insert({'name': name, 'age': age})
        print(f"Inserted: {{'name': '{name}', 'age': {age}}}")
        
    elif userinput == '2':
        read = db.search(user.name == 'manuel')
        print(read)
        
    elif userinput == '3':
        oldname = input("current name?: ")
        newname = input("new name?: ")
        newage = input("new age?")
        db.update({'name': newname}, user.name == oldname)
        print({'name': newname , "age" : newage})
        
    elif userinput == '4':
        delete = input("Enter the name to delete: ")
        db.remove(user.name == delete)
        print(f"Deleted the name'{delete}'")
    else:
        input('invalid synthax, choose again ')
