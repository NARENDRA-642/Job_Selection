#JOB SELECTION
import csv
rec_fields = ['roll.no', 'name', 'age', 'email','phone', 'qualification_strength']
sms_database = 'students.csv'
def show_menu():
    print ("----------------------------------")
    print ("Welcome to GENIUS WORLD company")
    print ("-"*8+" * "*6+"-"*8)
    print("1. Add New Student")
    print ("2. View Students")
    print ("3. Search Student")
    print ("4. Update Student")
    print ("5. Delete Student")
    print ("6. Quit")
def create_record():
    print("-----------------------")
    print ("Add Student Information")
    print ("----------------------")
    global rec_fields
    global sms_database
    stud_data= []
    for field in rec_fields:
        value = input("Enter " + field + ": ")
        stud_data.append(value)
    with open (sms_database, "a", encoding="utf-8") as f:
        writer = csv.writer (f)
        writer.writerows ([stud_data])
    print("Data saved successfully")
    input("Press any key to continue")
    return
def display_student():
    global rec_fields
    global sms_database
    print("----------Student Records ------------")
    with open (sms_database, "r", encoding="utf-8") as f:
        reader=csv.reader (f)
        for k in rec_fields:
           print (k, end='\t\t')
        print ("\n--------------------------")
        for row in reader:
            for item in row:
                print (item, end='\t\t')
            print ("\n--------------------------------")
        input ("Press any key to continue")

def search_record():
    global rec_fields
    global sms_database
    print ("------Search Student -----")
    roll = input ("Enter roll no. to search: ")
    with open (sms_database, "r", encoding="utf-8") as f:
        reader = csv.reader (f)
        for row in reader:
            if len(row) > 0 :
                if roll== row[0]:
                    print("----Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age:", row[2])
                    print("Email:" ,row [3])
                    print("Phone: ", row[4])
                    break
            else:
                print ("Roll No. not found in our database")
        input ("Press any key to continue")

def update_record():

    global rec_fields
    global sms_database

    print ("------Update Student-------")
    roll=input ("Enter roll no. to update: ")
    idx_student = None
    updated_rec = []
    with open (sms_database, "r", encoding="utf-8") as f:
        reader = csv.reader (f)
        counter = 0
        for row in reader:
            if len (row) > 0 :
                if roll== row[0]:
                    idx_student = counter
                    print("Student Found: at index ",idx_student)
                    stud_data =[]
                    for field in rec_fields:
                        value = input("Enter "+ field + ": ")
                        stud_data.append(value)
                    updated_rec.append(stud_data)
                else:
                    updated_rec.append(row)
                counter += 1
    if idx_student is not None:
            with open (sms_database, "w", encoding="utf-8") as f:
                    writer = csv.writer (f)
                    writer.writerows (updated_rec)
    else:
        print("Roll No. not found in our database")
    input ("Press any key to continue")

def delete_record():

    global rec_fields
    global sms_database

    print("---------Delete Student---------")
    roll=input("Enter roll no. to delete: ")
    stud_locate = False
    updated_rec =[]
    with open (sms_database, "r", encoding="utf-8") as f:
        reader = csv.reader (f)
        counter = 0
        for row in reader:
            if len (row) > 0 :
                if roll != row[0]:
                    updated_rec.append(row)
                    counter += 1
                else:
                    stud_locate = True
        if stud_locate is True:
            with open (sms_database, "w", encoding="utf-8") as f:
                writer = csv.writer (f)
                writer.writerows (updated_rec)
            print ("Roll no. ", roll, "deleted successfully")
        else:
            print ("Roll No. not found in our database")
        input ("Press any key to continue")
while True:

        show_menu()

        option=input ("Enter your option: ")
        if option=='1':
            create_record()
        elif option=='2':
            display_student ()
        elif option == '3':
            search_record()
        elif option == '4':
            update_record()
        elif option == '5':
            delete_record()
        else:
            break

print ("----------------------------")

print ("-------DATA COLLECTION OF STUDENTS COMPLETED---------")
import time
roll_no=input("Enter ROLL.NO:  ")
name=input("Enter NAME: ")

print("CONGRATULATIONS!......YOU PROFILE IS SELECTED FOR INTERVIEW....")
print("U have 2 rounds in interview")
print("ROUND 1:APTITUDE QUIZ\n ROUND 2:PERSONAL INTERVIEW")
print("Welcome APTITUDE QUIZ ROUND!")
print("roll.no",roll_no)
print("name",name)


chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)


score = 0

#question number 1
question_1 = print("1) What could be the value of tan80° tan10° + sin270° + sin20° is  tan80° tan10° + sin270° + sin20°?\n(a) 0\n(b) 1\n(c) 2\n(d) 3\n\n ")
answer_1 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question number 2
question_2 = print("2) What is the compound interest on Rs. 2500 for 2 years at rate of interest 4% per annum?\n(a) 180\n(b) 560\n(c) 120\n(d) 204\n\n ")
answer_2 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3) If January 1, 1996, was Monday, what day of the week was January 1, 1997?\n(a) MONDAY\n(b) WEDNESDAY\n(c) FRIDAY\n(d) SUNDAY\n\n ")
answer_3 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)


    

#print the score
while score >= 2:
    print("Well done! Your score was", score)
    print("YOU ARE SELECTED FOR ROUND 2")
    break

while score < 1:
    print("Better luck next time! Your score was", score)
    print("YOU ARE NOT SELECTED FOR ROUND 2")
    break

print("ROUND 2! BEGINS.....for ROUND 1 QUALIFIED STUDENTS")
print("-----------------PERSONAL INTERVIEW----------------------")
name=input ("Introduce yourself : ")
interest=input ("IN WHICH FIELD YOU ARE INTERESTED ")
print("................THANK YOU............")
