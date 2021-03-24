
from os import system,startfile
from datetime import datetime,timedelta
from time import sleep
import sqlite3 as sql
import re
import argparse


connector = sql.connect("ContestData.db")
cur = connector.cursor()


# Creating Table To store Data of every week
Main_querry =   """
                    CREATE TABLE Contest_Data(
                            Week INT UNIQUE,
                            Duty CHAR ,
                            Days CHAR ,
                            Contest_date CHAR ,
                            Upsolving_date CHAR ,
                            Contest_time CHAR ,
                            Upsolving_time CHAR
                    );
                """
# Pass_Crea_q = " CREATE TABLE PASSWORD(Password Char);"
# Password_q = " INSERT INTO PASSWORD(Password) VALUES ('Deepak@1')"

Team_q = """
            CREATE TABLE TEAM(
            Person1 CHAR,
            Person2 CHAR
            );
         """


try:
    cur.execute(Main_querry)
    # cur.execute(Pass_Crea_q)
    # cur.execute(Password_q)
    cur.execute(Team_q)
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('ANKIT','RIYA')")    
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('SHUBHAM','RETIKA')")
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('CHIRANJEEV','DEEPAK')")
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('CHIRAG','RAMANDEEP')")
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('HARSHR','KANCHI')")
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('CHANCHAL','ABHISHEK')")
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('TANUSHREE','ASHISH')")
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('ABHAY','SUKHMANJOT')")
    cur.execute("INSERT INTO TEAM(Person1,Person2) VALUES ('ARNAV','LALIT')")
    connector.commit()
except sql.OperationalError:
    print("Already Done")
    sleep(1)
except Exception:
    print("There is some Issue!")
    sleep(1)
else:
    print("Created")
    sleep(1)


# it ends 

Main_list = ["Week", "Team", "Days(Sat-Fri)", "Contest Date", "Upsolving Date"]
week10 = ["10", ("Ankit", "Riya"), "27/02-05/03", "01-03-2021", "05-03-21"]
week10_start_d = f"{week10[2][:5]}/{week10[3][6:]}"

#For Coloring text
CLR = {
    "RED": "\u001b[31m",
    "GREEN" : "\u001b[32m",
    "YELLOW" : "\u001b[33m",
    "BLUE" : "\u001b[34m",
    "Magenta" : "\u001b[35m",
    "CYAN" : "\u001b[36m",
    "RESET" : "\u001b[0m"
}

system("color")
# for Some Validation part using regex

# Time_regex = re.compile('[0-24]\d+:[0-60]\d+')
Ze_time_regex = re.compile("[012]\d:[0123456]\d")
Name_regex = re.compile("[A-Za-z]+")
Ze_date_regex = re.compile("\d{2}\/\d{2}\/\d{4}")

# Validation ends here 

# function for print for particular week


def Return_week(week):
    if week < 10:
        print(CLR["RED"],"\t\t\tPlease fill week after 10 week!",CLR["RESET"])
        return
    Fetch_querry = "SELECT Duty,Days,Contest_date,Upsolving_date FROM Contest_Data where Week=(?)"
    cur.execute(Fetch_querry,(week,))
    Fetch_tuple = cur.fetchone()
    if Fetch_tuple:
        week_list = [week,tuple(Fetch_tuple[0].split()),
                    Fetch_tuple[1], Fetch_tuple[2],
                    Fetch_tuple[3]
                    ]
    else:
        fetch_team = "SELECT * FROM TEAM;"
        cur.execute(fetch_team)
        team_list = cur.fetchall()
        len_tam_list = len(team_list)
        days_between = (week - 10)*7
        week_strtDate = (datetime.strptime(week10_start_d,"%d/%m/%Y")+timedelta(days_between)).date()
        week_endDate = week_strtDate+timedelta(days=6)
        week_contDate = week_strtDate+timedelta(days=2)
        week_upsolvingDate = week_endDate
        week_duty = team_list[(week-10)%len_tam_list]

        
        #string formatting

        week_strtDate = str(week_strtDate)
        week_endDate = str(week_endDate)
        week_contDate = str(week_contDate)
        week_upsolvingDate = str(week_upsolvingDate)
        week_days = f"{week_strtDate[8:]}/{week_strtDate[5:7]}-{week_endDate[8:]}/{week_endDate[5:7]}"
        week_contDate = f"{week_contDate[8:]}-{week_contDate[5:7]}-{week_contDate[:4]}"
        week_upsolvingDate = f"{week_upsolvingDate[8:]}-{week_upsolvingDate[5:7]}-{week_upsolvingDate[:4]}"
        week_list = [week,week_duty,
                     week_days,
                     week_contDate,
                     week_upsolvingDate
                    ]
    return week_list



# print for particular week ends here



# print N weeks

def Caller_print_weeks():
    system("cls")
    print(CLR["Magenta"],"\n\n\n\t\t\t\tFill to see weeks list",CLR["RESET"])
    print()
    print(CLR["BLUE"],"\t\t\tEnter starting Week: ",CLR["RESET"],end = "")
    start = int(input())
    print(CLR["BLUE"],"\t\t\tEnds starting Week: ",CLR["RESET"],end = "")
    ends = int(input())
    if start <= ends and start >=10 :
        Print_weeks(start, ends)
        sleep(1)
        print(CLR["GREEN"],"\t\t\tDo you want to continue to print(y/n)?",CLR["RESET"],end="")
        ans = input().upper()
        if ans == "Y" or ans == "YES":
            sleep(2)
            Caller_print_weeks()
        else:
            return
    else:
        print(CLR["RED"]+"\t\t\tPlease fill starting week less than equal to ending week and\n\t\t\tStart week should be greater than equal to 10",CLR["RESET"])
        print()
        print(CLR["GREEN"],"\t\t\tDo you want to continue to print(y/n)?",CLR["RESET"],end="")
        ans = input().upper()
        if ans == "Y" or ans == "YES":
            sleep(2)
            Caller_print_weeks()
        else:
            return


def Print_weeks(start, ends):
    if start<=ends and start>=10:
        system("cls")
        print(CLR["BLUE"],"\n\n")
        print("\t\t __________________________________________________________________________________________")
        print("\t\t|          |                              |                  |              |              |") 
        print("\t\t|"+CLR["CYAN"]+"Week".center(10)+CLR["BLUE"]+"|"+
                      CLR["CYAN"]+"DUTY".center(30)+CLR["BLUE"]+"|"+
                      CLR["CYAN"]+"Days (Sat-Fri)".center(18)+CLR["BLUE"]+"|"+
                      CLR["CYAN"]+"Contest Date".center(14)+CLR["BLUE"]+"|"+
                      CLR["CYAN"]+"Upsolving Date".center(14)+CLR["BLUE"]+"|"
            )
        print("\t\t|__________|______________________________|__________________|______________|______________|",CLR["RESET"]) 
        for i in range(start,ends+1):
            Fetch_data_querry = "SELECT Duty,Days,Contest_date,Upsolving_date FROM Contest_Data WHERE Week=(?);"
            cur.execute(Fetch_data_querry,(i,))
            fetch_list = cur.fetchone()
            if fetch_list:
                print(CLR["BLUE"]+"\t\t|"+CLR["RESET"]+f"week {i}".center(10)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{fetch_list[0]}".ljust(30)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{fetch_list[1]}".center(18)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{fetch_list[2]}".rjust(14)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{fetch_list[3]}".rjust(14)+CLR["BLUE"]+"|"
                    )
                print(CLR["BLUE"]+"\t\t|----------|------------------------------|------------------|--------------|--------------|")
                continue
            out_list = Return_week(i)
            print(CLR["BLUE"]+"\t\t|"+CLR["RESET"]+f"week {i}".center(10)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{out_list[1][0]} {out_list[1][1]}".ljust(30)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{out_list[2]}".center(18)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{out_list[3]}".rjust(14)+CLR["BLUE"]+"|"+
                              CLR["YELLOW"]+f"{out_list[4]}".rjust(14)+CLR["BLUE"]+"|"
                )
            print(CLR["BLUE"]+"\t\t|----------|------------------------------|------------------|--------------|--------------|")
    print(CLR["RESET"])
    return
    print(CLR["GREEN"],"\t\t\tDo you want to continue to print(y/n)? ",CLR["RESET"],end="")
    ans = input().upper()
    if ans == "Y" or ans == "YES":
        Caller_print_weeks()
    else:
        return



# print N weeks ends here


# Details of previous one

def Details_of_previous_week():
    date_today = datetime.now().date()
    date_test = datetime.strptime(week10_start_d,"%d/%m/%Y").date()
    curr_week = (date_today-date_test).days//7 + 10
    curr_week_list = Return_week(curr_week)
    if date_today >= datetime.strptime(curr_week_list[3],"%d-%m-%Y").date():
        Print_weeks(10,curr_week)
    else:
        cur.execute("SELECT * From Contest_Data where Week=(?)",(curr_week,))
        test = cur.fetchone()
        if not test:
            curr_week = curr_week-1
            Print_weeks(10,curr_week)
    print()
    print()
    print(CLR["BLUE"],f"\t\t\tEnter week number to see detail(It should be between 10 and {curr_week}): ",CLR["RESET"],end="")
    week = int(input())
    if 10 <= week <=curr_week:
        cur.execute("SELECT * FROM Contest_Data where Week=(?);",(week,))
        data_list = cur.fetchone()
        if data_list:
            print()
            print(CLR["BLUE"]+"\t\t|"+CLR["RESET"]+"Week".center(10)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+"Duty".center(24)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+"Days(Sat-Fri)".center(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+"Contest Date".center(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+"Upsolving Date".center(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+"Contest Time".center(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+"Upsolving Time".center(16)+CLR["BLUE"]+"|"+CLR["RESET"]
                )
            print(CLR["BLUE"]+"\t\t|"+CLR["RESET"]+f"{data_list[0]}".center(10)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+f"{data_list[1]}".ljust(24)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+f"{data_list[2]}".center(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+f"{data_list[3]}".rjust(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+f"{data_list[4]}".rjust(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+f"{data_list[5]}".center(16)+CLR["BLUE"]+"|"+
                CLR["YELLOW"]+f"{data_list[6]}".center(16)+CLR["BLUE"]+"|"+CLR["RESET"]
                )
        else:
            print(CLR["RED"],f"\t\t\tThere is no record of {week} week.",CLR["RESET"])
    else:
        print(CLR["RED"],f"\t\t\tPlease select in mentioned range!",CLR["RESET"])
    print()
    print(CLR["GREEN"],"\t\t\tDO you want to search more(y/n)? ",CLR["RESET"],end="")
    ans = input().upper()
    if ans == "Y" or ans == "YES":
        Details_of_previous_week()
    else:
        return

# Details of previous week


# print Teams

def PrintTeams():
    system("cls")
    Fetch_querry = "SELECT * FROM TEAM"
    cur.execute(Fetch_querry)
    Fetch_list = cur.fetchall()
    len_list = len(Fetch_list)
    print(CLR["BLUE"],"\n\n")
    print("\t\t\t ________________________________________________________________")
    print("\t\t\t|                                                                |") 
    print("\t\t\t|                           ",CLR["CYAN"],"Team List",CLR["BLUE"],"                        |")
    print("\t\t\t|________________________________________________________________|") 

    for i in range(len_list):
        print("\t\t\t|",CLR["RESET"],f"Team{i+1}".ljust(10),CLR["BLUE"],"|",CLR["YELLOW"],
              (f"{Fetch_list[i][0]}").ljust(20),CLR["BLUE"],
              "|",CLR["YELLOW"],(f"{Fetch_list[i][1]}").ljust(20),CLR["BLUE"],
              "|")
        print("\t\t\t|----------------------------------------------------------------|")
    print(CLR["RESET"])
# print teams ends here

# For Shuffling Two Persons at a time by just giving name


def Shuffle():
    system("cls")
    Fetch_querry = "SELECT * FROM TEAM"
    cur.execute(Fetch_querry)
    Fetch_list = cur.fetchall()
    len_list = len(Fetch_list)
    print(CLR["BLUE"],"\n\n")
    print("\t\t\t ________________________________________________________________")
    print("\t\t\t|                                                                |") 
    print("\t\t\t|                  "+CLR["CYAN"]+"Please Select Names to Shuffle"+CLR["BLUE"]+"                |")
    print("\t\t\t|________________________________________________________________|") 

    for i in range(len_list):
        print("\t\t\t|",CLR["RESET"],f"Team{i+1}".ljust(10),CLR["BLUE"],"|",CLR["YELLOW"],
              (f"{Fetch_list[i][0]}").ljust(20),CLR["BLUE"],
              "|",CLR["YELLOW"],(f"{Fetch_list[i][1]}").ljust(20),CLR["BLUE"],
              "|")
        print("\t\t\t|----------------------------------------------------------------|")
    print(CLR["GREEN"])
    Name1 = input("\t\t\tEnter 1 Name: ").upper()
    Name2 = input("\t\t\tEnter name to suffle with : ").upper()

    if Name1 == Name2:
        while True:
            print(CLR["RED"],"\t\t\tName you entered is matching Please Enter different Names")
            print(CLR["CYAN"],end="")
            Name1 = input("\t\t\t Name 1(Don't use space between): ").upper()
            Name2 = input("\t\t\t Name 2(Don't use space between): ").upper()
            if Name1 != Name2:
                break
            if Name1 == Name2:
                print(CLR["Magenta"],end="")
                print("\t\t\tName you entered still matches\n\t\t\tYou wanna try more to suffle members? (y/n) ",end=" ")
                print(CLR["CYAN"],end="")
                ans = input()
                print(CLR["RESET"])
                if ans == "Y" or ans == "y" or ans == "1":
                    continue
                else:
                    return


    while True:
        print(CLR["RED"])
        if not Name_regex.fullmatch(Name1):
            Name1 = input("\t\t\tPlease Enter First Name again(Entered digit before or used space between): ").upper()
        if not Name_regex.fullmatch(Name2):
            Name2 = input("\t\t\tPlease Enter Name to suffle with again(Entered digit before or used space between): ").upper()
        if Name_regex.fullmatch(Name1) and Name_regex.fullmatch(Name2):
            print(CLR["RESET"])
            break
    name_found_j_1 = -1
    name_found_j_2 = -1
    for i in range(len_list):
        for j in range(2):
            if Fetch_list[i][j] == Name1:
                name_found_j_1 = (j+1)%2
                name_found_i_1 = i
            elif Fetch_list[i][j] == Name2:
                name_found_j_2 = (j+1)%2
                name_found_i_2 = i
    try:
        if name_found_j_1 == -1 or name_found_j_2 == -1:
            raise UnboundLocalError
        if name_found_j_1 == 1:
            cur.execute("UPDATE TEAM set Person1=(?) where Person2=(?) ",(Name2,Fetch_list[name_found_i_1][1],))
            connector.commit()
        if name_found_j_1 == 0:
            cur.execute("UPDATE TEAM set Person2=(?) where Person1=(?) ",(Name2,Fetch_list[name_found_i_1][0],))
            connector.commit()
        if name_found_j_2 == 1:
            cur.execute("UPDATE TEAM set Person1=(?) where Person2=(?) ",(Name1,Fetch_list[name_found_i_2][1],))
            connector.commit()
        if name_found_j_2 == 0:
            cur.execute("UPDATE TEAM set Person2=(?) where Person1=(?) ",(Name1,Fetch_list[name_found_i_2][0],))
            connector.commit()
    except UnboundLocalError:
        print(CLR["RED"],"\t\t\tThe Name you entered is not correct Please check again")
        print(CLR["GREEN"],"\t\t\tYou wanna Shuffle team members more? (y/n)",CLR["RESET"],end=" ")
        print(CLR["CYAN"],end="")
        ans = input()
        print(CLR["RESET"])
        if ans == "Y" or ans == "y" or ans == "1":
            Shuffle()
        else:
            return 
    except Exception as e:
        print(f"\t\t\t{e}")
    else:
        print(CLR["YELLOW"],"\t\t\tDONE!!")
        sleep(2)
        PrintTeams()
        print(CLR["GREEN"],"\t\t\tYou wanna Shuffle team members more? (y/n)",CLR["RESET"],end=" ")
        ans = input()
        print(CLR["RESET"])
        if ans == "Y" or ans == "y" or ans == "1":
            Shuffle()
        else:
            return

    print(CLR["RESET"])


# To Insert New Team 

def Insert_Team():
    system("cls")
    Fetch_querry = "SELECT * FROM TEAM;"
    cur.execute(Fetch_querry)
    Fetch_list = cur.fetchall()
    len_list = len(Fetch_list)
    print(CLR["Magenta"],"\n\n\n\t\t\t    Please fill some detail"+CLR["YELLOW"]+"(All Capital)\n")
    print(CLR["BLUE"],"\t\t\tEnter Team's first person name (Don't use space between first and last Name): ",CLR["CYAN"],end="")
    Name1 = input().upper()
    print(CLR["BLUE"],"\t\t\tEnter Team's second person name (Don't use space between first and last Name): ",CLR["CYAN"],end="")
    Name2 = input().upper()
    print(CLR["RESET"])

    if Name1 == Name2 :
        while True:
            print()
            print(CLR["RED"],"\t\t\tThe names you entered are matching please enter different names!",CLR["BLUE"])
            print("\t\t\t Name 1(e for Exit): ",CLR["CYAN"],end="")
            Name1 = input().upper()
            if Name1 == "e":
                print(CLR["RESET"])
                return
            print(CLR["BLUE"],"\t\t\t Name 2(e for Exit): ",CLR["CYAN"],end="")
            Name2 = input().upper()
            if Name2 == "e":
                print(CLR["RESET"])
                return
            if Name1 == Name2 :
                continue
            else:
                break
        print(CLR["RESET"])

    name_found_1 = -1
    name_found_2 = -1
    while True:
        for i in range(len_list):
            if Fetch_list[i][0] == Name1 or Fetch_list[i][1] == Name1:
                name_found_1 = 1
            if Fetch_list[i][0] == Name2 or Fetch_list[i][1] == Name2:
                name_found_2 = 1
        if name_found_2 == 1 and name_found_1 == 1:
            print(CLR["RED"],"\t\t\tPlease Enter different Name they both exists!",CLR["RESET"])
            sleep(1)
            Insert_Team()
        if name_found_2 == 1:
            print(CLR["RED"],"\t\t\tSecond Name you entered matches from other team members\n\t\t\t Please renter(e for Exit): ",CLR["CYAN"],end="")
            Name2 = input().upper()
            if Name2 == "E" or Name2 == "EXIT":
                print(CLR["RESET"])
                return
            name_found_2 = -1
            continue
        if name_found_1 == 1:
            print(CLR["RED"],"\t\t\tFirst Name you entered matches from other team members\n\t\t\t Please renter(e for Exit): ",CLR["CYAN"],end="")
            Name1 = input().upper()
            if Name1 == "E" or Name1 == "EXIT":
                print(CLR["RESET"])
                return
            name_found_1 = -1
            continue
        if not Name_regex.fullmatch(Name1) and name_found_1 ==-1:
            print(CLR["RED"],"\t\t\tName 1(Please don't Enter digits or spaces in name!): ",CLR["RESET"],end="")
            Name1 = input().upper()
            if Name1 == "E" or Name1 == "EXIT":
                print(CLR["RESET"])
                return
            name_found_1 = -1
            continue

        if not Name_regex.fullmatch(Name2) and name_found_2 ==-1:
            print(CLR["RED"],"\t\t\tName 2(Please don't Enter digits or spaces in name!): ",CLR["RESET"],end="")
            Name2 = input().upper()
            if Name2 == "E" or Name2 == "EXIT":
                print(CLR["RESET"])
                return
            name_found_2 = -1
            continue

        if name_found_1 == -1 and name_found_2 == -1 :
            break
    print(CLR["RESET"])

    try:
        cur.execute("INSERT INTO TEAM VALUES(?,?);",(Name1,Name2,))
        connector.commit()
    except Exception as e:
        print(CLR["RED"],"\t\t\tThere is Some Issue ("+e+")")
        print(CLR["GREEN"],"\t\t\t Please fill again(e for go back)",CLR["RESET"],end="")
        ans = input()
        if ans.upper() == "E":
            return
        sleep(2)
        Insert_Team()
    else:
        print(CLR["YELLOW"],"\t\t\tDone !!")
        sleep(2)
        PrintTeams()
        print(CLR["GREEN"],"\n\t\t\tYou want to add more teams(y/n)?  ",CLR["RESET"],end="")
        ans = input()
        if ans.upper() == "Y" or ans.upper() == "YES":
            print(CLR["RESET"])
            Insert_Team()
        else:
            print(CLR["RESET"])
            return

# Inserting a new team function ends here


# Function to confirm Contest Date and Time

def Confirm_Cont_DT():
    date_today = datetime.now().date()
    date_test = datetime.strptime(week10_start_d,"%d/%m/%Y").date()
    curr_week = (date_today-date_test).days//7 + 10
    week,team,days,cont_date,upsol_date = Return_week(curr_week)
    team = f"{team[0]}  {team[1]}"
    # week = 10
    # team = ("Ankit","Riya")
    # days = "27/02-05/03"
    # cont_date = "28-02-2021"
    # upsol_date = "05-03-2021"

    test_cont_d = list(cont_date.split("-"))
    test_cont_d = f"{test_cont_d[2]}-{test_cont_d[1]}-{test_cont_d[0]}"
    min_test_cont_date = datetime.strptime(cont_date,"%d-%m-%Y") - timedelta(days = 2)
    min_test_cont_date = str(min_test_cont_date.date())
    max_test_cont_date = datetime.strptime(cont_date,"%d-%m-%Y") + timedelta(days = 3)
    max_test_cont_date = str(max_test_cont_date.date())

    string_date_now = str(datetime.now().date())
    if min_test_cont_date <= string_date_now <= test_cont_d:
        system("cls")
        print(CLR["Magenta"],"\n\n\n\t\t\t\tPlease Confirm Date and time for Contest\n",CLR["BLUE"])
        print("\t\t",CLR["YELLOW"],("Week").center(6),CLR["BLUE"],
               "|",CLR["YELLOW"],("Team").center(20),CLR["BLUE"],
               "|",CLR["YELLOW"],("Days").center(15),CLR["BLUE"],
               "|",CLR["YELLOW"],("Contest Date").center(16),CLR["BLUE"],
               "|",CLR["YELLOW"],("Upsolving Date").center(16),CLR["BLUE"],
            )
        print("\t\t",CLR["RESET"],(f"{week}").center(6),CLR["BLUE"],
               "|",CLR["RESET"],(team).center(20),CLR["BLUE"],
               "|",CLR["RESET"],(f"{days}").center(15),CLR["BLUE"],
               "|",CLR["RESET"],(f"{cont_date}").center(16),CLR["BLUE"],
               "|",CLR["RESET"],(f"{upsol_date}").center(16),CLR["RESET"]
            )
        while True:
            print()
            print(CLR["GREEN"],"\t\t\tDo you want to change date(y/n)? ",CLR["RESET"],end="")
            ans = input()
            if ans.upper() == "Y":
                while True:
                    print(CLR["BLUE"],"\t\t\tEnter a valid date"+CLR["YELLOW"]+"(dd/mm/yyyy)",CLR["RESET"],end="")
                    update_cont_date = input()
                    if Ze_date_regex.fullmatch(update_cont_date):
                        try:
                            datetime.strptime(update_cont_date,"%d/%m/%Y")
                        except ValueError:
                            print(CLR["RED"],"\t\t\tEither you have filled wrong format or didn't used '/' between them",CLR["RESET"])
                            print(CLR["GREEN"],"\t\t\tYou want to continue to set Date(y/n)? ",CLR["RESET"],end="")
                            ans = input().upper()
                            if ans == "Y":
                                continue
                            return
                        else:
                            if min_test_cont_date < str((datetime.strptime(update_cont_date,"%d/%m/%Y")).date()) <= max_test_cont_date : 
                                if update_cont_date<=string_date_now:
                                    cont_date = f"{update_cont_date[:2]}-{update_cont_date[3:5]}-{update_cont_date[6:]}"
                                    break
                                else:
                                    print(CLR["RED"],"\t\t\tDon't fill past date!",CLR["RESET"])
                                    print(CLR["GREEN"],"\t\t\tYou want to continue (y/n)? ",CLR["RESET"],end="")
                                    ans = input().upper()
                                    if ans == "Y":
                                        continue
                                    return
                            else:
                                print(CLR["RED"],"\t\t\tPlease select date between -1 or +3 of Contest date!")
                                print(CLR["GREEN"],"\t\t\tYou want to continue (y/n)? ",CLR["RESET"],end="")
                                ans = input().upper()
                                if ans == "Y":
                                    continue
                                return
                    else:
                        print(CLR["RED"],"\t\t\tPlease follow instruction (dd/mm/yyyy)!\n\t\t\tPut zero before if needed!",CLR["RESET"])
                        continue
            break
            

    #       for asking time

        while True:
            print()
            time_n = f"{datetime.now().time()}"[:5]
            print(CLR["BLUE"],"\t\t\tContest Time ( "+CLR["YELLOW"]+"hour:min"+CLR["BLUE"]+" (24 hour format),enter 0 before if hour or time < 10 ): ",CLR["RESET"],end="")
            cont_time = input()
            try:
                datetime.strptime(cont_time,"%H:%M")
            except ValueError:
                print(CLR["RED"],"\t\t\tPlease follow instruction ( valid Time too )",CLR["RESET"])
                continue
            else:
                if Ze_time_regex.fullmatch(cont_time):
                    if datetime.strptime(cont_date,"%d-%m-%Y").date() == datetime.now().date():
                        if time_n<=cont_time :
                            break
                        else:
                            print(CLR["RED"],"\t\t\tDon't select past time!",CLR["RESET"])
                            continue
                    else:
                        break
                else:
                    print(CLR["RED"],"\t\t\tPlease put zero!",CLR["RESET"])
                    continue
                

        #inserting data in main table
        try:
            Insert_querry = "INSERT INTO Contest_Data(Week,Duty,Days,Contest_date,Upsolving_date,Contest_time) VALUES(?,?,?,?,?,?);"
            cur.execute(Insert_querry,(week,team,days,cont_date,upsol_date,cont_time,))
            connector.commit()
        except sql.IntegrityError:
            print()
            print(CLR["RED"],"\t\t\tWeek Already confirmed!")
            print()
            print(CLR["BLUE"],"\t\t\tYou can update it by going back,you wanna go(y/n)?",CLR["RESET"],end="")
            ans = input()
            if ans.upper() == "Y":
                return
            else:
                sleep(1)
                Confirm_Cont_DT()
        except Exception as e:
            print(CLR["RED"],f"\t\t\tThere is some Issue {e} fill it again",CLR["RESET"])
            print(CLR["GREEN"],"\t\t\tYou want to go back to main(y/n)? ",CLR["RESET"],end="")
            ans = input()
            if ans.upper() == "Y":
                return
            sleep(2)
            Confirm_Cont_DT()
        else:
            print()
            print(CLR["YELLOW"],"\t\t\tDone!")
            print(CLR["GREEN"],"\t\t\tYou want to go back to main(y/n)? ",CLR["RESET"],end="")
            ans = input()
            if ans.upper() == "Y":
                return
            Confirm_Cont_DT()
    else:
        print(CLR["RED"],"\t\t\tThere is no Contest in 2 days so you can't confirm!",CLR["RESET"])
        sleep(2)
        return

# Function to confirm Contest Date and Time ends here



# function to update time and Date for Upsolving

def Update_D_and_T_Upsolving():
    system("cls")
    date_today = datetime.now().date()
    date_test = datetime.strptime(week10_start_d,"%d/%m/%Y").date()
    curr_week = (date_today-date_test).days//7 + 10
    curr_week_list = Return_week(curr_week)
    if date_today >= datetime.strptime(curr_week_list[3],"%d-%m-%Y").date():
        Print_weeks(10,curr_week)
    else:
        cur.execute("SELECT * From Contest_Data where Week=(?)",(curr_week,))
        test = cur.fetchone()
        if not test:
            curr_week = curr_week-1
            Print_weeks(10,curr_week)
    print()
    while True:
        print(CLR["BLUE"],f"\t\t\tEnter a week to updateDate and time for upsolving( 10<= week <= {curr_week} ): ",CLR["RESET"],end="")
        week = int(input())
        if 10 <= week <= curr_week:
            print()
            print(CLR["BLUE"],"\t\t\tEnter a valid date"+CLR["YELLOW"]+"(dd/mm/yyyy)",CLR["RESET"],end="")
            Update_upsol_date = input()
            if Ze_date_regex.fullmatch(Update_upsol_date):
                try:
                    datetime.strptime(Update_upsol_date,"%d/%m/%Y")
                except ValueError:
                    print(CLR["RED"],"\t\t\tEither you have filled wrong format or didn't used '/' between them",CLR["RESET"])
                    print(CLR["GREEN"],"\t\t\tYou want to continue to set Date(y/n)? ",CLR["RESET"],end="")
                    ans = input().upper()
                    if ans == "Y":
                        continue
                    return
                else:
                    if datetime.now().date() <= (datetime.strptime(Update_upsol_date,"%d/%m/%Y")).date(): 
                        
                        upsol_date = f"{Update_upsol_date[:2]}-{Update_upsol_date[3:5]}-{Update_upsol_date[6:]}"
                        break
                    else:
                        print(CLR["RED"],"\t\t\tDon't fill past date!",CLR["RESET"])
                        print(CLR["GREEN"],"\t\t\tYou want to continue (y/n)? ",CLR["RESET"],end="")
                        ans = input().upper()
                        if ans == "Y":
                            continue
                        return
                    
            else:
                print(CLR["RED"],"\t\t\tPlease put zero or you have not followed instruction!",CLR["RESET"])
            continue

        else:
            print(CLR["RED"],"\t\t\tPlease enter a week in the mentioned range!",CLR["RESET"])
            print()
            print(CLR["GREEN"],"\t\t\tDo you want to continue to update(y/n)? ",CLR["RESET"],end="")
            ans = input().upper()
            if ans == "Y" or ans == "YES":
                continue
            else:
                sleep(1)
                return

    while True:
        print()
        time_n = f"{datetime.now().time()}"[:5]
        print(CLR["BLUE"],"\t\t\tContest Time ( "+CLR["YELLOW"]+"hour:min"+CLR["BLUE"]+" (24 hour format),enter 0 before if hour or min < 10 ): ",CLR["RESET"],end="")
        upsol_time = input()
        try:
            datetime.strptime(upsol_time,"%H:%M")
        except ValueError:
            print(CLR["RED"],"\t\t\tPlease follow instruction ( valid Time too )",CLR["RESET"])
            continue
        else:
            if Ze_time_regex.fullmatch(upsol_time):
                if datetime.strptime(upsol_date,"%d-%m-%Y").date() == datetime.now().date():
                    if time_n<=upsol_time :
                        break
                    else:
                        print(CLR["RED"],"\t\t\tDon't select past time!",CLR["RESET"])
                        continue
                else:
                    break
            else:
                print(CLR["RED"],"\t\t\tPlease put zero!",CLR["RESET"])
                continue

    print(upsol_date, upsol_time)

    try:
        cur.execute("UPDATE Contest_Data set Upsolving_date=(?), Upsolving_time=(?) where Week=(?)",(upsol_date,upsol_time,week))
        connector.commit()
    except Exception as e:
        print(CLR["RED"],f"\t\t\tSome issue {e}",CLR["RESET"])
    else:
        print(CLR["YELLOW"],"\t\t\tDone!!",CLR["RESET"])

# function to update time and Date for upsolving ends here

# Update Function for week

def Update():
    pass


# update Function for week ends here

# Function to suffle team for some time

def Shuffle_Team_for_sometime():
    system("cls")
    date_today = datetime.now().date()
    date_test = datetime.strptime(week10_start_d,"%d/%m/%Y").date()
    curr_week = (date_today-date_test).days//7 + 10
    end_week = curr_week+15
    #function to print 15    
    Print_weeks(curr_week,end_week)
     
    print(CLR["Magenta"],"\n\n\t\t\t\tFill detail\n",CLR["RESET"])
    print(CLR["BLUE"],"\t\t\tEnter week number: ",CLR["RESET"],end="")
    week1 = int(input())
    print(CLR["BLUE"],"\t\t\tEnter week number to suffle with: ",CLR["RESET"],end="")
    week2 = int(input())
    week1 = Return_week(week1)
    week2 = Return_week(week2)
    if date_today <= datetime.strptime(week1[3],"%d-%m-%Y").date() and date_today <= datetime.strptime(week2[3],"%d-%m-%Y").date():
        week1[1],week2[1] = week2[1],week1[1]
        Insert_querry = "INSERT INTO Contest_Data(Week,Duty,Days,Contest_date,Upsolving_date) VALUES(?,?,?,?,?);"
        try:
            cur.execute(Insert_querry,(week1[0],f"{week1[1][0]}  {week1[1][1]}",week1[2],week1[3],week1[4],))
            connector.commit()
        except sql.IntegrityError:
            try:
                cur.execute("UPDATE Contest_Data set Duty=(?) where week=(?);",(f"{week1[1][0]}  {week1[1][1]}",week1[0],))
                connector.commit()
            except Exception as e:
                print(CLR["RED"],f"\t\t\tThere is Some issue {e}",CLR["RESET"])
            else:
                print(CLR["CYAN"],f"\t\t\tDone for week {week1[0]}",CLR["RESET"])
        else :
            print(CLR["CYAN"],f"\t\t\tDone for week {week1[0]}",CLR["RESET"])
        try:
            cur.execute(Insert_querry,(week2[0],f"{week2[1][0]}  {week2[1][1]}",week2[2],week2[3],week2[4],))
            connector.commit()
        except sql.IntegrityError:
            try:
                cur.execute("UPDATE Contest_Data set Duty=(?) where week=(?);",(f"{week2[1][0]}  {week2[1][1]}",week2[0],))
                connector.commit()
            except Exception as e:
                print(CLR["RED"],f"\t\t\tThere is Some issue {e}",CLR["RESET"])
            else:
                print(CLR["CYAN"],f"\t\t\tDone for week {week2[0]}",CLR["RESET"])
        else:
            print(CLR["CYAN"],f"\t\t\tDone for week {week2[0]}",CLR["RESET"])
    else:
        print(CLR["RED"],"\t\t\tPlease Select a week which is not passed!",CLR["RESET"])
    print(CLR["GREEN"],"\t\t\tDo you want to continue to change duty(y/n)? ",CLR["RESET"],end="")
    ans = input().upper()
    if ans == "Y" or ans == "YES":
        Shuffle_Team_for_sometime()
    else:
        return

# Function suffle team ends here


# Generate A csv File and show
def Csv_file(start, end):
    import csv

    with open("Contest Roaster.csv","w",newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(Main_list) 

        for i in range(start,end+1):
            week_list = Return_week(i)
            week_list[1] = f"{week_list[1][0]}    {week_list[1][1]}"
            csvwriter.writerow(week_list)

    print(CLR["YELLOW"],"\t\t\tDone",CLR["RESET"])
    startfile("Contest Roaster.csv")

# Generate a csv file functions ends here


# Main function for terminal


def Main_Window():
    while True:
        system("cls")
        print(CLR["BLUE"],"\n\n\n\n\t\t\t\t ________________________________________________")
        print("\t\t\t\t|                                                |")
        print("\t\t\t\t|                  "+CLR["YELLOW"]+"CONTEST ROASTER"+CLR["BLUE"]+"               |")
        print("\t\t\t\t|________________________________________________|",CLR["RESET"])
        print()
        print(CLR["Magenta"],"\t\t\t\t1.  Print Teams",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t2.  Print Weeks",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t3.  Insert Team",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t4.  Permanently change Team members",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t5.  Alter Team for some time",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t6.  Confirm Date and Time for Contest",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t7.  Update Date and Time for Upsolving",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t8.  Detail of any Previous week",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t9.  Update Week Details( Coming Soon)",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t10. CSV File( Coming Soon)",CLR["RESET"])
        print(CLR["Magenta"],"\t\t\t\t11. For Exit",CLR["RESET"])
        print()
        print(CLR["GREEN"],"\t\t\tChoose your option: ",CLR["RESET"],end="")
        ans = int(input())
        if ans == 1:
            PrintTeams()
            input()
        elif ans == 2:
            Caller_print_weeks()
        elif ans == 3:
            Insert_Team()
        elif ans == 4:
            Shuffle()
        elif ans == 5:
            Shuffle_Team_for_sometime()
        elif ans == 6:
            Confirm_Cont_DT()
        elif ans == 7:
            Update_D_and_T_Upsolving()
        elif ans == 8:
            Details_of_previous_week()
        elif ans == 9:
            Update()
        elif ans ==10:
            pass
        elif ans == 11:
            break
        else:
            print(CLR["RED"],"\t\t\tPlease Enter valid option!",CLR["RESET"])
            sleep(2)


# Main function for terminal ends here

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--start",type=int,help="Where to start printing")
    parser.add_argument("--end",type=int,help="Where to end printing")

    args = parser.parse_args()

    if args.start != None and args.end != None :
        Csv_file(args.start, args.end)
    elif args.start == None and args.end != None:
       Csv_file(10, args.end)
    elif args.start != None and args.end == None:
        Print_weeks(args.start,args.start)
    else:
        Main_Window()
        






connector.close()