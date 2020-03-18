# Modules
import sqlitedict

# Access
tourist_accounts_db = sqlitedict.SqliteDict("giya_accounts_tourist.db", autocommit=True)
tourGuide_accounts_db = sqlitedict.SqliteDict("giya_accounts_tourGuide.db", autocommit=True)
# Functions

def add_record_tourist(): # Insert New Records
    temp_data = {"username": "", "password": ""}
    tourist_data = tourist_accounts_db.get("tourist_data", [])
    print("--------- Insert New Tourist Record ---------")
    temp_data["username"] = input("Enter Username: ")
    temp_data["password"] = input("Enter Password: ")
    tourist_data.append(temp_data)
    tourist_accounts_db["tourist_data"] = tourist_data
    print(" ")

def add_record_tourGuide(): # Insert New Records
    temp_data = {"username": "", "password": ""}
    tourGuide_data = tourGuide_accounts_db.get("tourGuide_data", [])
    print("--------- Insert New Tour Guide Record ---------")
    temp_data["username"] = input("Enter Username: ")
    temp_data["password"] = input("Enter Password: ")
    tourGuide_data.append(temp_data)
    tourGuide_accounts_db["tourGuide_data"] = tourGuide_data
    print(" ")
"""
def delete_record(): # Delete Records based on Student Number
    student_records = student_db.get("records")
    i = 0
    indicator = False

    print("----------- Delete Tourist Record -----------")
    student_number = input("Enter Student Number: ") 
    while i < len(student_records):
        if student_number == student_records[i]["student_number"]:
            delete = i
            print("Successfully Removed")
            break
        else:
            if i+1 == len(student_records):
                indicator = True
            i += 1
    if indicator == True:
        print("No Student Record Found !!!")
    else:
        student_records.pop(delete)
        student_db["records"] = student_records
    print(" ")

def view_records(typeIndicator): # View Records based on Student Number
    student_records = student_db.get("records")
    indicator = False
    i = 0

    if typeIndicator == 0:     
        print("----------- Search Student Record -----------")
        student_number = input("Enter Student Number: ") 
    
        while i < len(student_records):
            if student_number == student_records[i]["student_number"]:
                print("--------------------")
                print("Student Number: ",
                    student_records[i]["student_number"])
                print("Student Name: ",
                    student_records[i]["first_name"] + " " + student_records[i]["last_name"])
                print("Program: ",
                    student_records[i]["program"])
                break
            else:
                if i+1 == len(student_records):
                    indicator = True
                i += 1
        if indicator == True:
            print("No Student Record Found !!!")
            i = -1
        print(" ")
        return i
    
    elif typeIndicator == 1:
        print("-------------| Student Records |-------------")
        print(" ")
        for i in range(len(student_records)):
            if i < 10:
                print("-------------------- 00{} --------------------".format(i+1))
            elif i > 10 and i < 100:
                print("-------------------- 0{} --------------------".format(i+1))    
            else:
                print("-------------------- {} --------------------".format(i+1))        
            print("Student Number: ",
                student_records[i]["student_number"])
            print("Student Name: ",
                student_records[i]["first_name"] + " " + student_records[i]["last_name"])
            print("Program: ",
                student_records[i]["program"])
        print(" ")

def modify_records(list_number): # Modify Records 
    student_records = student_db.get("records")
    value = 1/2

    if list_number == -1:
        return None
    else:
        while value < 5 and value > 0:
            print("----------- Modify Student Record -----------")
            print("  | 1. Student Number   4. Program      |")
            print("  | 2. First Name       5. Back         |")
            print("  | 3. Last Name                        |")
            chosen = int(input("Choose What to Modify: "))
            if chosen == 1:
                print("Current Student Number: ", student_records[list_number]["student_number"])
                student_records[list_number]["student_number"] = input("Enter New Student Number: ")
            elif chosen == 2:
                print("Current First Name: ", student_records[list_number]["first_name"])
                student_records[list_number]["first_name"] = input("Enter New First Name: ")
            elif chosen == 3:
                print("Current Last Name: ", student_records[list_number]["last_name"])
                student_records[list_number]["last_name"] = input("Enter New Last Name: ")
            elif chosen == 4:
                print("Current Program: ", student_records[list_number]["program"])
                student_records[list_number]["program"] = input("Enter New Program: ")
            elif chosen == 5:
                value = 5
            else:
                print("Please Enter Approriate Value !!!")
            print(" ")
            student_db["records"] = student_records
"""

tourist_data = tourist_accounts_db.get("tourist_data", [])
print(len(tourist_data))
tourGuide_data = tourGuide_accounts_db.get("tourGuide_data", [])
print(len(tourGuide_data))

print(tourist_data[0]["username"])
print(tourist_data[0]["password"])
print(tourGuide_data[0]["username"])
print(tourGuide_data[0]["password"])

print(len(tourist_data))
print(len(tourGuide_data))