import mysql.connector
# GLOBAL VARIABLE DECLARATION
myConnection =""
cursor=""
username=""
password =""
roomrent =0
total amount=0
cid=""
#FUNCTION TO CHECK MY SQL CONNECTIVITY
def MYSQLconnectionCheck():
    global myConnection
    global username
    global password
    username = input("\n ENTER MYSQL SERVER'S USERNAME: ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD: ")
    myConnection=mysql.connector.connect(host="localhost", user=userName,passwd=password, auth_plugin='mysql_native_password' )
    if myConnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED!")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD!")

#FUNCTION TO ESTABLISH MYSQL CONNECTION
def MYSQLconnection():
    global username
    global password
    global myConnection
    global cid
    myConnection=mysql.connector.connect(host="localhost",user=username,passwd=password,
    database="HMS" , auth_plugin='mysql_native_password' )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MY SQL CONNECTION!")
        myConnection.close()
                                
