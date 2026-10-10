import sqlite3
con=sqlite3.connect('employee management system .db')
c=con.cursor()
print("opened database successfully")
c.execute('''create  table if not exists users
       (USERNAME TEXT NOT NULL,
       PASSWORD  TEXT  NOT NULL,
       ROLE TEXT NOT NULL);''')
c.execute('''create  table if not exists employee
      (EMPLOYEEID INT PRIMARY KEY NOT NULL,
       EMPLOYEENAME TEXT NOT NULL,
       JOIN_DATE  INT   NOT NULL,
       DEPARTMENT TEXT NOT NULL,
       DESIGNATION TEXT NOT NULL,
       BANK INT  NOT NULL,
       LEAVE INT NOT NULL,
       SALARY INT  NOT NULL,
       CONTACT INT  NOT NULL);''')
c.execute('''create  table if not exists leave
      (EMPLOYEEID INT  NOT NULL,
       EMPLOYEENAME TEXT NOT NULL,
       DATE  INT  CHAR(10) NOT NULL,
       STATUS TEXT NOT NULL );''')
c.execute('''create  table if not exists salary
      (EMPLOYEEID INT  NOT NULL,
       EMPLOYEENAME TEXT NOT NULL,
       BANK TEXT  NOT NULL,
       PERIOD TEXT NOT NULL,
       BASIC_SALARY INT NOT NULL,
       DA INT  NOT NULL,
       TAX INT  NOT NULL,
       NET INT NOT NULL);''')
con.commit()
con.close()
def signup_admin():
    print("\n=========== Admin/HR ============")
    username = input("Enter Admin/HR Username : ")
    password = input("Enter Admin/HR password : ")
    con=sqlite3.connect('employee management system .db')
    c=con.cursor()
    c.execute("INSERT INTO users(username,password,role)VALUES(?,?,?)",(username,password,"Admin/HR"))
    con.commit()
    con.close()
    print(f"Admin/HR acount created successfully")
def signup_Employee():
    print("\n=========== EMPLOYEE ============")
    username = input("Enter Employee Username : ")
    password = input("Enter Employee password : ")
    con=sqlite3.connect('employee management system .db')
    c=con.cursor()
    c.execute("INSERT INTO users(username,password,role)VALUES(?,?,?)",(username,password,"Employee"))
    con.commit()
    con.close()
    print(f"Employee acount created successfully")
def admin():
   while True:
    print("\n================== Admin/HR================")
    print("1. Add new employee")
    print("2. View all employee")
    print("3. Search employee")
    print("4.Update")
    print("5.Leave management")
    print("6.Delete")
    print("7.Add salary")
    print("8.Back")
    choice = input(" Enter your choice : ")
    if choice == "1":
       print("\n============== Add New Employee =============") 
       ids = int(input("Enter id : "))
       name = input("Enter name : ")
       join_date = input(" Joinig date : ")
       department = input(" Department Name : ")
       designation = input("Designation : ")
       bank_account =int(input("Enter Bank Account Number : "))
       salary = float(input("Enter salary amout : ") )
       leave = int(input("Balance leave(days):  ") )
       contact =int(input("Enter contact number : "))
       con = sqlite3.connect('employee management system .db')
       c = con.cursor()
       con.execute("INSERT INTO employee(EMPLOYEEID,EMPLOYEENAME,JOIN_DATE,DEPARTMENT,DESIGNATION,BANK,LEAVE,SALARY,CONTACT)VALUES(?,?,?,?,?,?,?,?,?)",(ids,name,join_date,department,designation,bank_account,leave,salary,contact))
       con.commit()
       con.close()    
       print(" \nCompleted")
    elif choice =="2": 
        print("\n==============  Employee List =============")      
        con=sqlite3.connect("employee management system .db")
        c=con.cursor()
        c.execute("SELECT * FROM employee")
        row = c.fetchall()
        con.close()
        for i in row:
            print("ID = ", i[0])
            print("Name = ", i[1])
            print("Join Date = ", i[2])
            print("Department = ", i[3])
            print("Designation = ", i[4])
            print("Account Number = ", i[5])
            print("Leave(Days) = ", i[6])
            print("Salary = ", i[7])
            print("Contact Number = ", i[8],"\n")
            pass
    elif choice == "3":
         print("\n =============== Search Employee ==========")
         search_id = int(input("Enter employee ID to search : "))
         con = sqlite3.connect('employee management system .db')
         c = con.cursor()
         c.execute("SELECT * FROM employee WHERE EMPLOYEEID = ?",(search_id,))
         row = c.fetchone()
         con.close()
         if row:
            print("\n --------Find it -----------")
            print("ID = ", row[0])
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Department = ", row[3])
            print("Designation = ", row[4])
            print("Account Number = ", row[5])
            print("Leave(Days) = ", row[6])
            print("Salary = ", row[7])
            print("Contact Number = ", row[8],"\n")
         else:
          print("\nEployee not found")
    elif choice == "4":
         print("\n ============= Update Employee ==========")
         update_id = int(input("Enter employee ID to update: "))
         con = sqlite3.connect("employee management system .db")
         c = con.cursor()
         c.execute("SELECT * FROM employee WHERE EMPLOYEEID = ?" , (update_id,))
         row = c.fetchone()
         if row:
             print("\nwhat do you want to update ? ")
             print("1. Name")
             print("2. Join Date")
             print("3. Department")
             print("4. Dsignation")
             print("5.Account number")
             print("6.Leave(Days)")
             print("7. Salary ")
             print("8. Countact Number")
             update_choice = input("Entrer your choice : ")
             if update_choice == "1":
                new_name = input("Enter new name : ")
                c.execute("UPDATE employee SET EMPLOYEENAME = ? WHERE EMPLOYEEID = ?" , (new_name,update_id))
             elif update_choice == "2":
                  new_jion_date = input("Enter new Jion Date : ")
                  c.execute("UPDATE employee SET JOIN_DATE= ? WHERE EMPLOYEEID = ?" , (new_join_date,update_id))
             elif update_choice == "3":
                  new_department = input("Enter new Department : ")
                  c.execute("UPDATE employee SET DEPARTMENT  = ? WHERE EMPLOYEEID = ?" , (new_department,update_id))
             elif update_choice == "4":
                  new_designation = input("Enter new Dsignation : ")
                  c.execute("UPDATE employee SET DSIGNATION = ? WHERE EMPLOYEEID = ?" , (new_designation,update_id))
             elif update_choice == "5":
                  new_account = input("Enter new Account Number : ")
                  c.execute("UPDATE employee SET BANK = ? WHERE EMPLOYEEID = ?" , (new_account,update_id))
             elif update_choice == "6":
                  new_leave = input("Enter new number of leave : ")
                  c.execute("UPDATE employee SET LEAVE = ? WHERE EMPLOYEEID = ?" , (new_leave,update_id))
             elif update_choice == "7":
                new_salary = input("Enter new salary : ")
                c.execute("UPDATE employee SET SALARY = ? WHERE EMPLOYEEID = ?" , (new_salary,update_id))
             elif update_choice == "8":
                  new_contact = input("Enter new contact number : ")
                  c.execute("UPDATE employee SET CONTACT = ? WHERE EMPLOYEEID = ?" , (new_contact,update_id))
             else:
                 print("Invalid choice ! ")
                 con.close()
                 continue
             con.commit()
             con.close()
             print("\nEmployee details updated successfully..")
         else:
            con.close()
            print("\nEmployee ID not found")
    elif choice == "5":
        print("\n ============= Leave Management ==============")
        con = sqlite3.connect("employee management system .db")
        c = con.cursor()
        c.execute("SELECT * FROM leave")
        rows = c.fetchall()
        if rows:
            print("\n----- Leave Applications --------")
            for i in rows:
                     print("ID = ", i[0])
                     print("Name = ", i[1])
                     print("Date = ", i[2])
                     print("Status = ", i[3])
            print("\nDo you want to update leave status")
            choice_yes_no = input("Enter (Y/N) : ")
            if choice_yes_no == "Y":
                id = int(input("Enter Employee ID : "))
                leave_date = input("Enter leave Date : ")
                new_status = input("Enter new status(Approved/Rejected) : ")
                c.execute("""UPDATE leave SET STATUS = ? WHERE EMPLOYEEID = ? AND DATE = ?""", (new_status, id ,leave_date))
                con.commit()
                print("\nLeave status updated successfully")
            elif choice_yes_no == "N":
                print("\nOkay.....")
            else:
                print("\nInvalid choice ! Enter Y or N ")
        con.close()
    elif choice == "6":
        print("\n ========= Delete Employee ========")
        del_id = int(input("Enter employee ID to delete: "))
        con = sqlite3.connect("employee management system .db")
        c = con.cursor()
        c.execute("SELECT * FROM employee WHERE EMPLOYEEID = ?",(del_id,))
        row = c.fetchone()
        if row:
            print(f"\nemoloyee found :{row[1]}")
            confirm = input("Are you sure you want to delet this employee?(Y/N) : ")
            if confirm == "Y":
               c.execute("DELETE FROM employee WHERE EMPLOYEEID = ?",(del_id,))
               con.commit()
               print("\nDeleted successfully")
            else:
                print("\Delection cancelled")
                con.close()
    elif choice == "7":
        print("\n============== Add Employee Salary =============")
        ids = int(input("Enter Employee ID : "))
        name = input("Enter Employee Name : ")
        bank = input("Enter Bank Name/Account : ")
        period = input("Enter Pay Period (e.g., October 2026) : ")
        basic = int(input("Enter Basic Salary : "))
        da = int(input("Enter DA : "))
        tax = int(input("Enter Tax Deduction : "))
        net = (basic + da) - tax 
        
        con = sqlite3.connect('employee management system .db')
        c = con.cursor()
        c.execute("INSERT INTO salary (EMPLOYEEID, EMPLOYEENAME, BANK, PERIOD, BASIC_SALARY, DA, TAX, NET) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                  (ids, name, bank, period, basic, da, tax, net))
        con.commit()
        con.close()
        print("\nSalary record added successfully!")
    elif choice == "8":
         print("\nReturing to main menu....")
         return
    else:
        print("\nInvalid choice ! Please choose between 1 to 8.")

def employee_menu():
    while True:
        print(f"\n============== Employee Menu ===========")
        print("1.view your profile")
        print("2.Apply for Leave")
        print("3.view pay slip")
        print("4. logout")
        choice = input("Enter your choice : ")
        if choice =="1":
            print("\n======= My Profile =========")
            id = int(input("Enter your ID : "))
            con= sqlite3.connect("employee management system .db")
            c = con.cursor()
            c.execute("SELECT * FROM employee WHERE EMPLOYEEID = ?",(id,))
            row = c.fetchone()
            con.close()
            if row:
                print("\n ----------- Profile Details -----------")
                print("ID = ", row[0])
                print("Name = ", row[1])
                print("Join Date = ", row[2])
                print("Department = ", row[3])
                print("Designation = ", row[4])
                print("Account Number = ", row[5])
                print("Leave(Days) = ", row[6])
                print("Salary = ", row[7])
                print("Contact Number = ", row[8],"\n")
            else:
                print("\nEmployee ID not found in records.")
        elif choice == "2":
            print("\n ========= Apply Leave =========")
            id = int(input(" Enter your ID : "))
            con = sqlite3.connect("employee management system .db")
            c = con.cursor()
            c.execute("SELECT DATE, STATUS FROM leave WHERE EMPLOYEEID = ?", (id,))
            leaves = c.fetchall()
            if leaves:
                print("\n---------- Status-------")
                for i in leaves:
                    print(f"Date:{i[0]} status:{i[1]}")
            else:
                    print("\nNO previous leave application found.")
            c.execute("SELECT EMPLOYEENAME FROM employee WHERE EMPLOYEEID = ?", (id,))
            row = c.fetchone()
            
            if row:
                name = row[0]
                print("\n--- Apply for New Leave ---")
                leave_date = input("Enter new leave date : ")
                
                c.execute("INSERT INTO leave (EMPLOYEEID, EMPLOYEENAME, DATE, STATUS) VALUES (?, ?, ?, ?)", 
                          (id, name, leave_date, "Pending"))
                con.commit()
                print("\nNew leave application submitted successfully! Status: Pending")
            else:
                print("\nEmployee ID not found in records! Cannot apply.")
            con.close()
            print("\nLeave application submitted successfully ...")
        elif choice == "3":
            print("\n =========== Pay Slip ==========")
            id = int(input(" Enter your Employee ID : "))
            con = sqlite3.connect("employee management system .db")
            c= con.cursor()
            c.execute("SELECT * FROM salary WHERE EMPLOYEEID = ?",(id,))
            row = c.fetchone()
            con.close()
            if row:
               print("\n-------- Salary Slip ---------")  
               print("Employee ID = ", row[0]) 
               print("Employee Name = ", row[1]) 
               print("Bank Account = ", row[2]) 
               print("pay period = ",row[3])
               print("Basic salary = ",row[4])
               print("DA = ",row[5])
               print("Tax = ",row[6])
               print("Net salary = ",row[7])
            else:
                print("\n No salary record found for this employee ID .")
        elif choice =="4":
            print('\nLogging out....')   
            break


         
             
def signin_admin():
 while True:
    print("\n=========== Admin/HR ============")
    username = input("Enter Admin/HR Username : ")
    password = input("Enter Admin/HR password : ")
    con=sqlite3.connect('employee management system .db')
    c=con.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password =? AND role = 'Admin/HR' ",(username,password))
    user=c.fetchone()
    con.close()
    if user:
        print(f"\nWelcome Admin ! Sign in successfully completed.")
        admin()
        break
    else:
        print("\nInvalid username or password... Try again")

def signin_Employee():
    print("\n=========== Employee ============")
    username = input("Enter Employee Username : ")
    password = input("Enter Employee password : ")
    con=sqlite3.connect('employee management system .db')
    c=con.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password =? AND role = 'Employee' ",(username,password))
    user=c.fetchone()
    con.close()
    if user:
        print(f"\nWelcome Employee ! Sign in successfully completed.")
        employee_menu()
    else:
        print("\nInvalid username or password... Try again")
def main_menu():
 while True:
    print("\n============= MAIN MENU ================")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Exit")

    choice =input("Enter your choice = ")
    if choice=="1":
       print("\n======= Sign Up ========")
       print("1. Admin/HR")
       print("2. Employee")
       role_choice=input("Enter your choice = ")
       if  role_choice =="1":
           signup_admin()
           pass
       elif role_choice =="2":
           signup_Employee()
       else:
           print("Invalid choice. Please choice 1 or 2")
    elif choice=="2":
         print("\n======= Sign In ========")
         print("1. Admin/HR")
         print("2. Employee")
         role_choice=input("Enter your choice = ")
         if  role_choice =="1":
            signin_admin()
         elif role_choice =="2":
             signin_Employee()
         else:
             print("Invalid choice. Please choice 1 or 2")
    elif choice == "3":
        print(" Thank You !")
        break
    else:
       print("Invalid Choice.Please choose 1 ,2 ,or 3")
       break
main_menu()
           