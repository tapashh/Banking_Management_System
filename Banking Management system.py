import mysql.connector
import pickle

mydb = mysql.connector.connect(
    user='root', passwd='ROOT', host='localhost', database='BankDB'")
mycursor = mydb.cursor(buffered=True)

# Created Database BankDB
# mycursor.execute('create database BankDB')

def Menu():
    print("*" * 209)
    print("MAIN MENU".center(140))
    print("1. Insert Record/Records".center(140))
    print("2. Display Records as per Account Number".center(140))
    print(" a. Sorted as per Account Number".center(140))
    print(" b. Sorted as per Customer Name".center(140))
    print(" c. Sorted as per Customer Balance".center(140))
    print("3. Search Record Details as per the account number".center(140))
    print("4. Update Record".center(140))
    print("5. Delete Record".center(140))
    print("6. Transactions".center(140))
    print(" a. Debit/Withdraw from the account".center(140))
    print(" b. Credit into the account".center(140))
    print("7. Exit".center(140))
    print("*" * 209)

def MenuSort():
    print(" a. Sorted as per Account Number".center(140))
    print(" b. Sorted as per Customer Name".center(140))
    print(" c. Sorted as per Customer Balance".center(140))
    print(" d. Back".center(140))

def MenuTransaction():
    print(" a. Debit/Withdraw from the account".center(140))
    print(" b. Credit into the account".center(140))
    print(" c. Back".center(140))

def Create():
    try:
        mycursor.execute('''CREATE TABLE bank(
            ACCNO VARCHAR(10),
            NAME VARCHAR(20),
            MOBILE VARCHAR(10),
            EMAIL VARCHAR(30),
            ADDRESS VARCHAR(20),
            CITY VARCHAR(10),
            COUNTRY VARCHAR(20),
            BALANCE INTEGER(15))''')
        print("Table Created")
    except:
        print("Table Exists")
    Insert()

def Insert():
    while True:
        Acc = input("Enter account no: ")
        Name = input("Enter Name: ")
        Mob = input("Enter Mobile: ")
        email = input("Enter Email: ")
        Add = input("Enter Address: ")
        City = input("Enter City: ")
        Country = input("Enter Country: ")
        Bal = float(input("Enter Balance: "))
        Rec = [Acc, Name.upper(), Mob, email.upper(), Add.upper(), City.upper(), Country.upper(), Bal]
        Cmd = "INSERT INTO BANK VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(Cmd, Rec)
        mydb.commit()
        ch = input("Do you want to enter more records (Y/N): ")
        if ch.lower() == 'n':
            break

def DispSortAcc():
    try:
        cmd = "SELECT * FROM BANK ORDER BY ACCNO"
        mycursor.execute(cmd)
        S = mycursor.fetchall()
        F = "%15s %15s %15s %15s %15s %15s %15s %15s"
        print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print("=" * 130)
        for i in S:
            print(" ".join(f"{j:14}" for j in i))
        print("=" * 130)
    except:
        print("Table doesn't exist")

def DispSearchAcc():
    try:
        cmd = "SELECT * FROM BANK"
        mycursor.execute(cmd)
        S = mycursor.fetchall()
        ch = input("Enter the account number to be searched: ")
        for i in S:
            if i[0] == ch:
                F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
                print("=" * 130)
                print(" ".join(f"{j:14}" for j in i))
                print("=" * 130)
                break
        else:
            print("Record Not found")
    except:
        print("Table doesn't exist")

def Delete():
    try:
        cmd = "SELECT * FROM BANK"
        mycursor.execute(cmd)
        S = mycursor.fetchall()
        A = input("Enter the account number whose details to be deleted: ")
        for i in S:
            if i[0] == A:
                cmd = "DELETE FROM BANK WHERE ACCNO=%s"
                mycursor.execute(cmd, (i[0],))
                mydb.commit()
                print("Account Deleted")
                break
        else:
            print("Record not found")
    except:
        print("No such table")

while True:
    Menu()
    ch = input("Enter your Choice: ")
    if ch == "1":
        Create()
    elif ch == "2":
        while True:
            MenuSort()
            ch1 = input("Enter choice a/b/c/d: ")
            if ch1.lower() == 'a':
                DispSortAcc()
            elif ch1.lower() == 'b':
                DispSortName()
            elif ch1.lower() == 'c':
                DispSortBal()
            elif ch1.lower() == 'd':
                print("Back to the main menu")
                break
            else:
                print("Invalid choice")
    elif ch == "3":
        DispSearchAcc()
    elif ch == "5":
        Delete()
    elif ch == "7":
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered")



