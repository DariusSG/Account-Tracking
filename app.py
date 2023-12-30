import getpass as secureinput
import hashlib
import os
import time
from pyfiglet import Figlet
#from colorama import init

from lib import authenication 
from lib import database
from bin import cli_helper

condition1 = None
debug = False #DEBUG FLAG
f = Figlet(font='slant')
#init()

while condition1 != True and debug == False:
    os.system("cls")
    print(f.renderText('Secure Banking'))
    print("Welcome To Secure Banking Python")
    print("Please enter your Username and Password")

    condition1 = authenication.authenicate((str(input("Username: "))),(secureinput.getpass("Password: "))) 

os.system("cls")
print("Welcome Back, DariusSG")
cli_helper.CLILoop()
