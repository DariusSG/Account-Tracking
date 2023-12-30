import os
import time

from lib import apsw



#First-Time Setup
def InitalSetup():
    '''
    First Time Setup
    '''
    db = apsw.Connection('database.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS savings
    (
        TransactID INTEGER PRIMARY KEY NOT NULL, 
        Time text, 
        Description STRING(50) NOT NULL, 
        Amount DECIMAL NOT NULL,
        Total DECIMAL NOT NULL
    )''')
    cursor.execute('''INSERT INTO {account} (Time,Description,Amount,Total) VALUES(datetime('now', 'localtime'),'{Description}',{Amount},{Total})'''.format(account = "savings",Description = 'FirstTimeSetup',Amount = '0',Total = '0'))
    db.close()

#Transaction Jouranal
def AddTransactionEntry(accountname,description,amount,total):
    db = apsw.Connection('database.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO {account} (Time,Description,Amount,Total) VALUES(datetime('now', 'localtime'),'{Description1}',{Amount1},{Total1})'''.format(account = accountname,Description1 = description,Amount1 = amount,Total1 = total))
    db.close()

#Account Stuff
def AddAccount(accountname):
    '''
    Add a Account
    '''
    db = apsw.Connection('database.db')
    cursor = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS "+accountname+" (TransactID INTEGER PRIMARY KEY NOT NULL,Time text,Description STRING(50) NOT NULL,Amount DECIMAL NOT NULL,Total DECIMAL NOT NULL)"
    cursor.execute(command)
    cursor.execute('''INSERT INTO {account} (Time,Description,Amount,Total) VALUES(datetime('now', 'localtime'),'{Description}',{Amount},{Total})'''.format(account = accountname,Description = 'FirstTimeSetup',Amount = '0',Total = '0'))
    db.close()

#Viewing Accounts&Transactions
def GetTransactionEntries(accountname):
    journal = list()
    db = apsw.Connection('database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM {account}'''.format(account=accountname))
    for rows in cursor:
        journal.append(rows)
    db.close()
    return journal

def GetAccountList():
    AccountList = list()
    db = apsw.Connection('database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';''')
    for rows in cursor:
        AccountList.append(rows)
    db.close()
    return AccountList

def FilterTransactionEntry(accountname,filter_variable):
    journal = list()
    db = apsw.Connection('database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM {account} WHERE Description="{variable}"'''.format(account=accountname,variable=filter_variable))
    for rows in cursor:
        journal.append(rows)
    db.close()
    return journal

def GetTotal_utils(accountname):
    journal = list()
    db = apsw.Connection('database.db')
    cursor = db.cursor()
    cursor.execute('''SELECT TOTAL FROM {account} ORDER BY TransactID DESC LIMIT 1'''.format(account=accountname))
    for r in cursor:
        journal.append(r)
    db.close()
    lst1 = journal[0]
    return lst1[0]

#Extra Utils
def ICleaner():
    '''
    ICleaner for DataBases
    Run Only if needed
    '''
    db = apsw.Connection('database.db')
    cursor=db.cursor()
    cursor.execute('VACUUM')
    db.close()


def checkapsw():
    '''
    Check the version of apsw and sqlite
    '''

    print ("      Using APSW file",apsw.__file__)                # ASPW File location
    print ("         APSW version",apsw.apswversion())           # ASPW Verison
    print ("   SQLite lib version",apsw.sqlitelibversion())      # SQLite Library Version
    print ("SQLite header version",apsw.SQLITE_VERSION_NUMBER)   # SQLite Header Verison
