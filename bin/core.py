from lib import database
from lib.rapidtable import format_table, FORMAT_GENERATOR_COLS
from lib.termcolor import colored

def command_view(arg):
    if len(arg) == 0:
        print("Invaild Arguments \nUsage:view [transaction\\accounts] {AccountName [filter\\all] FilterVariable}(transaction)")
    elif arg[0] == "transaction":
        if len(arg) == 2:
            print("Invaild Arguments \nUsage:view [transaction\\accounts] {AccountName [filter\\all] FilterVariable}(transaction)")
        elif arg[2] == 'filter':
            if len(arg) == 3:
                print("Invaild Arguments \nUsage:view [transaction\\accounts] {AccountName [filter\\all] FilterVariable}(transaction)")
            else:
                result = database.FilterTransactionEntry(arg[1],arg[3:])
                if len(result) == 0:
                    print("No Transactions with this Description was found.")
                else:
                    print_table(orderedict(result))
        elif arg[2] == 'all':
            result = database.GetTransactionEntries(arg[1])
            print_table(orderedict(result))
        else:
            print("Invaild Arguments \nUsage:view [transaction\\accounts] {AccountName [filter\\all] FilterVariable}(transaction)")
    elif arg[0] == "accounts":
        result = database.GetAccountList()
        print_table2(orderedict2(result))
    else:
        print("Invaild Arguments \nUsage:view [transaction\\accounts] {AccountName [filter\\all] FilterVariable}(transaction)")

def command_add(arg):
    if len(arg) == 0:
        print("Invaild Arguments \nUsage:add [transaction\\account] {AccountName Description Amount}(transaction)")
    elif arg[0] == "transaction":
        if len(arg) != 4:
            print("Invaild Arguments \nUsage:add [transaction\\account] {AccountName Description Amount}(transaction)")
        else:
            print("Creating a Transaction...")
            print("Transcation\nAccount:{account} Description:{description} Amount:{amount}".format(account=arg[1],description=arg[2],amount=currencyformatting(arg[3])))
            yesorno=input("Is This Correct? Type Yes or No ")
            if yesorno.lower() == "y" or yesorno.lower() == "yes":
                print("Please Wait ... ")
                remaintotal = database.GetTotal_utils(arg[1])
                if (remaintotal+float(arg[3])) >= 0 and float(arg[3]) < 10000.00:
                    database.AddTransactionEntry(arg[1],arg[2],arg[3],(remaintotal+float(arg[3])))
                    print("Transaction Completed")
                else:
                    print("Insufficient Funds or Amount too large")
            else:
                print("Transaction Cancelled")
    elif arg[0] == "account":
        print("Creating Account ...")
        accname = input("What is the new Account Name \nIt CANNOT start with numbers and can only contain alphanumeric characters. \n :>>")
        database.AddAccount(str(accname))
        print("Account Created")
    else:
        pass

def orderedict(x):
    dct_data = {
        'TransactID':None,
        'Time':None,
        'Description':None,
        'Amount':None,
        'Remaining Total':None
    }
    data = []
    for lst in x:
        dct_data['TransactID']= lst[0]
        dct_data['Time']= lst[1]
        dct_data['Description']= lst[2]
        dct_data['Amount']= currencyformatting(lst[3])
        dct_data['Remaining Total']= currencyformatting(lst[4])
        data.append(dct_data)
        dct_data = {
        'TransactID':None,
        'Time':None,
        'Description':None,
        'Amount':None,
        'Remaining Total':None
    } 
    return data

def print_table(y):
    header, rows = format_table(y, fmt=FORMAT_GENERATOR_COLS)
    spacer = '  '
    print(colored(spacer.join(header), color='blue'))
    print(colored('-' * sum([(len(x) + 2) for x in header]), color='magenta'))
    for r in rows:
        print(colored(r[0], color='white') + spacer, end='')
        print(colored(r[1], color='yellow') + spacer, end='')
        print(colored(r[2], color='cyan') + spacer, end='')
        print(colored(r[3], color='red') + spacer, end='')
        print(colored(r[4], color='green'))

def orderedict2(x):
    dct_data = {
        'No.':None,
        'Name':None
    }
    data = []
    counter = 1
    for i in x:
        dct_data['No.'] = counter
        dct_data['Name'] = i[0]
        data.append(dct_data)
        dct_data = {
        'No.':None,
        'Name':None
    }
        counter += 1
    return data

def print_table2(y):
    header, rows = format_table(y, fmt=FORMAT_GENERATOR_COLS)
    spacer = '  '
    print(colored(spacer.join(header), color='blue'))
    print(colored('-' * sum([(len(x) + 2) for x in header]), color='magenta'))
    for r in rows:
        print(colored(r[0], color='white') + spacer, end='')
        print(colored(r[1], color='cyan'))

def currencyformatting(x):
    x = float(x)
    return "${:,.2f}".format(x)
