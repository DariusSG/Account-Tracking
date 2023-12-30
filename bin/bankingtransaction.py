from lib import database
from lib.rapidtable import format_table, FORMAT_GENERATOR_COLS
from lib.termcolor import colored

def transferfunds(args):
    if len(args) == 3:
        print("Transfering {funds} From Account {froacc} to Account {toacc}".format(funds=args[0],froacc=args[1],toacc=args[2]))
        yesorno = input("Is this Correct? ")
        if yesorno.lower() == "y" or yesorno.lower() == "yes":
            remaintotal = database.GetTotal_utils(args[1])
            remaintotal1 = database.GetTotal_utils(args[2])
            if (remaintotal-float(args[0])) >= 0 and float(args[0]) < 10000.00:
                    database.AddTransactionEntry(args[1],"FUNDSTRANSFER",(str(float(args[0])*-1)),(remaintotal-float(args[0])))
                    database.AddTransactionEntry(args[2],"FUNDSTRANSFER",args[0],(remaintotal1+float(args[0])))
                    print("Transfer Completed")
            else:
                print("Insufficient Funds or Amount too large") 
        else:
            print("Transaction Cancelled")
    else:
        print("Invaild Arguments \nUsage:transferfunds Amount [From Account] [To Account]")

def withdraw(arg):
    if len(arg) == 2:
        print("Withdrawing ${amount} from {account}".format(amount=arg[1],account=arg[0]))
        yesorno = input("Confirm? ")
        if yesorno.lower() == "y" or yesorno.lower() == "yes":
            print("Please Wait...")
            remaintotal = database.GetTotal_utils(arg[0])
            if (remaintotal-float(arg[1])) >= 0 and float(arg[1]) < 10000.00:
                database.AddTransactionEntry(arg[0],"WITHDRAW",(str(float(arg[1])*-1)),(remaintotal-float(arg[1])))
                print("Withdraw Completed")
            else:
                print("Insufficient Funds or Amount too large")
        else:
            print("Transaction Cancelled")
    else:
        print("Invaild Argument \nUsage:withdraw Account Amount")

def deposit(arg):
    if len(arg) == 2:
        print("Depositing ${amount} to {account}".format(amount=arg[1],account=arg[0]))
        yesorno = input("Confirm? ")
        if yesorno.lower() == "y" or yesorno.lower() == "yes":
            print("Please Wait...")
            remaintotal = database.GetTotal_utils(arg[0])
            if float(arg[1]) < 10000.00:
                database.AddTransactionEntry(arg[0],"DEPOSIT",arg[1],(remaintotal+float(arg[1])))
                print("Deposit Completed")
            else:
                print("Amount too large")
        else:
            print("Transaction Cancelled")
    else:
        print("Invaild Argument \nUsage:deposit Account Amount")

def deleteaccount(arg):
    if len(arg) == 2:
        pass
    elif len(arg) == 1:
        pass
    else:
        pass

