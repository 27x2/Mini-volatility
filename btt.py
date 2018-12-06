import volatility
import commands
import sys
import os

#show info of raw
def showInfo(file):
	info=commands.getstatusoutput('volatility imageinfo -f '+file)
	if "The requested file doesn't exist" in info[1]:
		print "\nWrong location of raw file"
	else:
		print info[1][122:]

#show processing
def showProcess(file,profile):
	proc=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' pslist')
	if "The requested file doesn't exist" in proc[1]:
		print "\nWrong location of raw file"
	else:
		print proc[1][46:]

#show processing + hidden
def showProcessHi(file,profile):
	prochi=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' psscan')
	if "The requested file doesn't exist" in prochi[1]:
		print "\nWrong location of raw file"
	else:
		print prochi[1][46:]

#dump process
def dumpProc(file,profile,pid):
	dump=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' procdump -p'+str(pid)+' -D .')
	if "The requested file doesn't exist" in dump[1]:
		print "\nWrong location of raw file"
	elif "Cannot find PID" in dump[1]:
		print "\nWrong pid please use option 3 to check again"
	else:
		print dump[1][46:]

#show connection
def showCon(file,profile):
	if "WinXP" in profile:
		con=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' connscan')
	else:
		con=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' netscan')
	if "The requested file doesn't exist" in con[1]:
		print "\nWrong location of raw file"
	else:
		print con[1][46:]

def findFile(file,profile,namefile):
	findfile=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' filescan | grep '+namefile)
	if "The requested file doesn't exist" in findfile[1]:
		print "\nWrong location of raw file"
	else:
		print findfile[1][46:]

def dumpFile(file,profile,fid):
	dumpf=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' dumpfiles -Q'+str(fid)+' -D .')
	if "The requested file doesn't exist" in dumpf[1]:
		print "\nWrong location of raw file"
	elif "Invalid PHYSOFFSET Enter" in dumpf[1]:
		print "\nWrong fid please use option 3 to check again"
	else:
		print dumpf[1][46:]

def showDll(file,profile,pid):
	dll=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' dlllist -p '+pid)
	if "The requested file doesn't exist" in dll[1]:
		print "\nWrong location of raw file"
	else:
		print dll[1][46:]
def hiddenDll(file,profile,pid):
	dll=commands.getstatusoutput('volatility -f '+file+' --profile='+profile+' ldrmodules -p '+pid)
	if "The requested file doesn't exist" in dll[1]:
		print "\nWrong location of raw file"
	else:
		print dll[1][46:]

def options(file):
	profile = ""
	while 1:
		menu()
		choice = input("Your choice: \n")
		if choice == 1:
			showInfo(file)
#===============================================================
		elif choice ==2:
			profile = raw_input("Enter profile: \n")
#===============================================================
		elif choice ==3:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				showProcess(file,profile)
#===============================================================
		elif choice ==4:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				showProcessHi(file,profile)
#===============================================================
		elif choice ==5:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				pid=raw_input("Enter pid to dump: \n")
				#pid=str(pid)
				dumpProc(file,profile,pid)
#===============================================================
		elif choice ==6:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				showCon(file,profile)
#===============================================================
		elif choice ==7:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				namefile=raw_input("Enter name file: \n")
				findFile(file,profile,namefile)
#===============================================================
		elif choice ==8:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				fid=raw_input("Enter file id:")
				dumpFile(file,profile,fid)
		elif choice ==9:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				pid=raw_input("Enter file id:")
				showDll(file,profile,pid)
		elif choice ==10:
			if profile == "":
				print "\nPlease use option 2 to enter profile"
			else:
				pid=raw_input("Enter file id:")
				hiddenDll(file,profile,pid)

def menu():
	print """
		1. Show basic info of raw memory file.
		2. Enter profile
		3. Show processing.
		4. Show all processing include hiden processing.
		5. Dump process
		6. Show connection(s).
		7. Find file.
		8. Dump file.
		9. Show dll.
		10. Hidden dll.
	"""

def showhelp():
	print """
	Usage: python btt.py [OPTIONS]
	[OPTIONS]
	--file   [File location]
	--help 	 [Show help]
	"""

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		showhelp()
		sys.exit()
 	else:
 		if sys.argv[1] == "--file":
  			options(sys.argv[2])
  		elif sys.argv[1] == "--help":
  			showhelp()
  		else:
  			print "Wrong option please try --help"
