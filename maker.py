import sys, subprocess, os
#-------------------------------------------------------------------------------
#functions to define
def split_path(path):
  full_path = path
  path_to_exe, name = path.rsplit("\\", 1)
  return name, full_path, path_to_exe.split(".")[0]

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
#pathVDF = ("C:\\Program Files (x86)\\Steam\\userdata\\", steamID, "\\config\\shortcuts.vdf ")
name = ""
path = ''
start = ""
hidden = "0 "
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
inVRLibrary = ""
last_playtime = "0 "
categories = ""
#extensions = (pathVDF, splitpath, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary, last_playtime, categories)
#-------------------------------------------------------------------------------
#scans directory for .exe files
import os
for root, dirs, files in os.walk(itchDIR):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             splitresult = split_path(result)
             print (splitresult)

#--------------------------------------------------------------------------------
close = input ("press enter to close")