import os
import subprocess
import sys

if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
    print '''
You need to supply the application group for the servers you want to ping, i.e.
    dms
    swaps

Followed by the site i.e.
    155
    bromley'''
    sys.exit(0)
else:
    if (len(sys.argv) < 3):
        sys.exit ('\nYou need to supply the app group. Usage : ' + filename + ' followed by the application group i.e. \n \t dms or \n \t swaps \n then the site i.e. \n \t 155 or \n \t bromley')
    appgroup = sys.argv[1]
    site = sys.argv[2]	

    if os.name == "posix":
        myping = "ping -c 2 "
    elif os.name in ("nt", "dos", "ce"):
        myping = "ping -n 2 "		
    if 'dms' in sys.argv:
      appgroup = 'dms'	
    elif 'swaps' in sys.argv:
      appgroup = 'swaps'
    if '155' in sys.argv: 
      site = '155'	
    elif 'bromley' in sys.argv:
      site = 'bromley'	

filename = sys.argv[0]	
logdir = os.getenv("logs")
logfile = 'ping_' + appgroup + '_' + site + '.log'
logfilename = os.path.join(logdir, logfile)	
confdir = os.getenv("my_config")		
conffile = (appgroup + '_servers_' + site + '.txt')
conffilename = os.path.join(confdir, conffile)	
f = open(logfilename, "w")
for server in open(conffilename):
    ret = subprocess.call(myping + server, shell=True, stdout=f, stderr=subprocess.STDOUT)
    if ret == 0:
      f.write (server.strip() + " is alive" + "\n")
    else:
      f.write (server.strip() + " did not respond" + "\n")
print ("\n\tYou can see the results in the logfile : " + logfilename);
