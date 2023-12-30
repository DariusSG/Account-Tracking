import hashlib
import time
import binascii

def salt():
    return "eb387a5edbaddb8851e28127671cec2694a817afc327a9c8eb6e90196c21a222"

def authenicate(username,password):
    newpass = username+password
    if (binascii.hexlify(hashlib.pbkdf2_hmac('sha256', newpass.encode('utf-8'), salt().encode("ascii"), 100000, dklen=128)).decode('ascii')) == "62e2f1036707e229a95b3f9db4b090f24308dd89d5248d3a28f9adf0da820ed0cde0b9412594a462d6447419bafc3a0def70f0abac2edd46a558499b1dd40e0ab5b207f18b888f237c431421fac80ba2a2234bb2057f46b521de47524e9aa104a43f42893ef7466487eebc566e6e4942f73884420fdc3509d36cc7fe985deeca":
        return True
    else:
        print("Wrong Password, Try Again")
        time.sleep(3)
        return False
