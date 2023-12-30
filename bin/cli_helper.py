import cmd
import sys
import time
from lib import database
from bin import core
from bin import bankingtransaction

class InteractiveTerminal(cmd.Cmd):
    intro = "Type help or ? to list commands.\n"
    prompt = "[DariusSG]>>>"
    file = None

    #---------- Commands ----------
    def do_icleaner(self, arg):
        'Do maintenance on database'
        print("Please Wait ...")
        database.ICleaner()
        time.sleep(5)
        print("Completed")
    
    def do_view(self, arg):
        'View Something \nUsage:view [transaction\\accounts] {AccountName [filter\\all] FilterVariable}(transaction)'
        arguments = parse(arg)
        core.command_view(arguments)

    def do_add(self, arg):
        'Add Something \nadd [transaction\\account] {AccountName Description Amount}(transaction)\n**DO NOT USE**'
        arguments = parse(arg)
        core.command_add(arguments)

    def do_transferfunds(self, arg):
        'Transfer money to another account \nUsage:transferfunds Amount [From Account] [To Account]'
        arguments = parse(arg)
        bankingtransaction.transferfunds(arguments)

    def do_withdraw(self, arg):
        'Withdraw Funds From an Account \nUsage:withdraw Account Amount'
        arguments = parse(arg)
        bankingtransaction.withdraw(arguments)

    def do_deposit(self, arg):
        'Deposit Funds Into an Account \nUsage:deposit Account Amount'
        arguments = parse(arg)
        bankingtransaction.deposit(arguments)

    def do_exit(self, arg):
        'Exit'
        print("Logging out ...")
        time.sleep(3)
        print("Thanking For Banking with us")
        time.sleep(1)
        return True

    def do_setup(self, arg):
        database.InitalSetup()

def parse(arg):
    return arg.split()

def CLILoop():
    '''CLI Loop'''
    InteractiveTerminal().cmdloop()
