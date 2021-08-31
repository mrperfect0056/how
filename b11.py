
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
# Time : Mon Feb  1 07:55:44 2021
#---------------------------------------
# -*- coding: utf-8 -*-
import os,sys,time
os.system("clear")

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		

##### LOGO #####
logo='''

\033[1;92m
          __  __           _    _ 
         |  \/  |         | |  (_)
         | \  / |_   _ ___| | ___ 
         | |\/| | | | / __| |/ / |
         | |  | | |_| \__ \   <| |
         |_|  |_|\__,_|___/_|\_\_|
\033[1;90m --------------------------------------------
 \033[1;93m[+] AUTHER     :   MUSKI
 [+] FACEBOOK   :   XTYLISH PATHANI
 [+] WHATSAPP   :   +1541xxxxxxx
 [+] \033[1;92mBE ORIGINAL LETS THE WORLD COPY YOU
\033[1;90m --------------------------------------------
"""

CorrectUsername = "muskan"
CorrectPassword = "muski"

loop = 'true'
while (loop == 'true'):
    print logo  
    print "\033[1;97mFIRST STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    username = raw_input("          \033[1;94mTOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input("          \033[1;93mTOOL PASSWORD: ")
        if (password == CorrectPassword):
            print " FIRST STEP Is Done. Logged in Successfully as " + username
            jalan("\033[1;93m ")
            jalan("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
            time.sleep(1)
            loop = 'false'
        else:
            print " Wrong Password !"
            os.system('xdg-open https://www.youtube.com/mastertrick1')
            os.system("clear")
    else:
        print " Wrong Username !"
        os.system('xdg-open https://www.facebook.com/groups/231747098048450')
        os.system("clear")

os.system("python2 main.py")
