
# Decompiled by HTR-TECH | TAHMID RAYAT
# Github : https://github.com/htr-tech
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
# Time : Mon Feb  1 07:55:44 2021
#---------------------------------------
# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhotnine
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhotnine")
    time.sleep(1)
    os.system('python2 .main.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;92m
          __  __           _    _ 
         |  \/  |         | |  (_)
         | \  / |_   _ ___| | ___ 
         | |\/| | | | / __| |/ / |
         | |  | | |_| \__ \   <| |
         |_|  |_|\__,_|___/_|\_\_|
\033[1;90m --------------------------------------------
 \033[1;93m[+] AUTHER     :   Dark
 [+] FACEBOOK   :   xxxxxxx
 [+] WHATSAPP   :   +xxxx-xxxx
 [+] \033[1;92mBE ORIGINAL LETS THE WORLD COPY YOU
\033[1;90m --------------------------------------------
"""

cusr = "xtylish"
cpwd = "pathani"
def u():
    os.system("clear")
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    usr=raw_input("          \033[1;94mTOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print "\033[1;97mSECOND STEP OF LOGIN"
        print "\033[1;97m--------------------"
        print "\033[1;97m "
        print("          \033[1;94mTOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/mastertrick1')
        u()
def p():
    os.system("clear")
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    print("          \033[1;92mTOOL USERNAME : Muski Tools (correct)")
    pwd=raw_input("          \033[1;93mTOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print "\033[1;97mSECOND STEP OF LOGIN"
        print "\033[1;97m--------------------"
        print "\033[1;97m "
        print("          \033[1;92mTOOL USERNAME : Muski Tools (correct)")
        print("          \033[1;92mTOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/groups/231747098048450')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    print("          \033[1;92mTOOL USERNAME : Muski Tools (correct)")
    print("          \033[1;92mTOOL PASSWORD : Muski Tools (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
  
    time.sleep(1)
    os.system("python2 muski.txt")
if __name__=="__main__":
    u()



