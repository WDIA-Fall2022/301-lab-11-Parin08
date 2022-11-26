from mysql.connector import MySQLConnection, Error

from mySqlDbConfig import readDbConfig


def queryFetchone():
    try:
        dbconfig = readDbConfig()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Grades limit 20")
        row = cursor.fetchone()
        print("<table border='1'>")
        while row is not None:
            print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row[0],row[1],row[2],row[3]))
            row = cursor.fetchone()
        print("</table>")

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def  insertGrade(lastName,firstName,province,grade):
  try:
    dbconfig = readDbConfig()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Grades(FName,LName,Province,Grade) VALUES (%s, %s, %s, %s)",(firstName, lastName, province, grade))
    conn.commit()

  except Error as e:
        print(e)
        conn.rollback()

  finally:
    cursor.close()
    conn.close()

def deleteGrade(lastName,firstName,province,grade):
  try:
    dbconfig = readDbConfig()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM grades WHERE FName=%s AND  LName=%s AND Province=%s AND Grade=%s",(lastName, firstName, province, grade))
    conn.commit()

  except Error as e:
        print(e)
        conn.rollback()

  finally:
    cursor.close()
    conn.close()

def displayGrade(lastName,firstName,province):
  try:
    dbconfig = readDbConfig()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grades WHERE FName LIKE '%" + firstName + "%' AND LName LIKE '%" + lastName + "%' AND province LIKE '%" + province + "%'")
    rows = cursor.fetchall()

    print("<table border='1'>")
    for row in rows:
        print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(row[0], row[1], row[2], row[3]))
    print("</table>")

  except Error as e:
        print(e)

  finally:
    cursor.close()
    conn.close()



def displayMenu():
    finish = 1
    while finish == 1:
        try:
           print("1. Enter a grade.")
           print("2. Display records")
           print("3. Delete record")
           print("0. Exit")
           option = int(input("Select any of the option."))

           if(option==1):
               lname = input("Please enter last name.")
               fname = input("Please enter first name.")
               province = input("Please enter province.")
               grade = input("Please enter grade.")
               insertGrade(lname, fname, province, grade)
           elif(option==2):
               lname = input("Please enter last name.")
               fname = input("Please enter first name.")
               province = input("Please enter province.")
               displayGrade(lname, fname, province)
           elif(option==3):
               lname = input("Please enter last name.")
               fname = input("Please enter first name.")
               province = input("Please enter province.")
               grade = input("Please enter grade.")
               deleteGrade(lname, fname, province, grade)
           else:
               finish = 0

        except:
            finish = 1
            print("Error")

displayMenu()
