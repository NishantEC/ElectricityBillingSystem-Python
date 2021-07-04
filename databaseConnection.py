# Creating table into database!!!
import sqlite3

# Connect to sqlite database


def getsqliteconnection():
    conn = sqlite3.connect('ebsDatabase.sqlite')
    print("Connected to SQLite")
    # cursorObject = conn.cursor()
    # createTable1 = "CREATE TABLE operatorinfo(operatorID TEXT PRIMARY KEY ,fullname TEXT, mobile INTEGER, password TEXT);"
    # createTable2 = "CREATE TABLE consumerDetails(meterNo INTEGER PRIMARY KEY AUTOINCREMENT, consumerFullname TEXT, consumerMobileNO INTEGER, consumerEmail TEXT, consumerAddress TEXT);"
    # createTable3 = "CREATE TABLE bills(billNo INTEGER PRIMARY KEY AUTOINCREMENT,meterNo INTEGER NOT NULL REFERENCES consumerDetails(meterNo), unitConsumed REAl, billAmount REAL, creationDate DATE);"
    # cursorObject.execute(createTable1)
    # cursorObject.execute(createTable2)
    # cursorObject.execute(createTable3)


    return conn

# getsqliteconnection()
