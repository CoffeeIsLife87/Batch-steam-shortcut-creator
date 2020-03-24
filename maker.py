import sys, subprocess, os
#-------------------------------------------------------------------------------
#functions to define
def split_path(path):
  full_path = path
  start, name = path.rsplit("\\", 1)
  return '"'+name.split(".")[0]+'"'+" "+'"'+path+'"'+" "+'"'+start+'"'

shortcut = ('python shortcuts.py')
#-------------------------------------------------------------------------------
#checks for itch.io directory to scan
itchDIRfile = open('info\\itchDIR.txt', 'r+')
itchDIRcheck = itchDIRfile.readline()
if (itchDIRcheck == ""):
    itchDIR = input("copy and paste itch games directory ")
    itchDIRfile.write(itchDIR)
    itchDIRfile.close
else:
    itchDIR = itchDIRcheck
    print (itchDIR)
#-------------------------------------------------------------------------------
#checks for steam ID or askes for it if it is not detected
steamIDfile = open('info\\steamID.txt', 'r+')
steamIDcheck = steamIDfile.readline()
if (steamIDcheck == ""):
    steamIDpath = "C:\\Program Files (x86)\\Steam\\userdata"
    steamIDpath = os.path.realpath(steamIDpath)
    os.startfile(steamIDpath)
    steamID = str(input("copy and paste the numbers from the folder"))
    steamIDfile.write(steamID)
    steamIDfile.close()
else:
    steamID = steamIDcheck
    print (steamID)
#-------------------------------------------------------------------------------
#stuff to define
pathVDF = ('"'+"C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"'+" ")
name = ""
path = ''
start = ""
hidden = " 0 "
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
inVRLibrary = "0 "
last_playtime = "0 "
categories = ""
#this is a template in case I have to move stuff around
#extensions = (pathVDF+splitresult+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories)
#-------------------------------------------------------------------------------
#scans directory for .exe files
import os
for root, dirs, files in os.walk(itchDIR):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             splitresult = split_path(result)
             #------------------------------------------------------------------
             #from here @this indentation point, I need to have all the variables set
             extensions = (" "+pathVDF+splitresult+" "+'""'+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories)
             os.system(shortcut+extensions)
#--------------------------------------------------------------------------------
print ("thanks for using my tool")
print ("glad I could help you automate some stuff")
close = input ("press enter to close")