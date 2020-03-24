import sys, subprocess, os
#-------------------------------------------------------------------------------
#functions to define
def split_path(path):
  full_path = path
  path_to_exe, name = path.rsplit("\\", 1)
  return name, full_path, path_to_exe.split(".")[0]
#-------------------------------------------------------------------------------
#checking bits
check1 = 0
itchDIRfile = open("info\\itchDIR.txt", 'r+')
while (check1 < 1):
    if (itchDIRfile.readline(1) == " "):
        itchDIR = input("copy and paste itch games directory ")
        itchDIRfile.write(itchDIR)
        check1 = 1
    else:
        itchDIR = itchDIRfile.readline()
        check1 = 1
#-------------------------------------------------------------------------------
#checks for steam ID or askes for it if it is not detected
steamIDfile = open('info\\steamID.txt', 'r+')
check2 = 0
while (check2 < 1):
    if (steamIDfile.readline(1) == ""):
        steamIDpath = "C:\\Program Files (x86)\\Steam\\userdata"
        steamIDpath1 = os.path.realpath(steamIDpath)
        os.startfile(steamIDpath)
        steamID = str(input("copy and paste the numbers from the folder"))
        steamIDfile.write(steamID)
        steamIDfile.close()
        check2 = 1
    else:
        steamID = steamIDfile.read()
        check2 = 1
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#scans directory for .exe files
import os
for root, dirs, files in os.walk(itchDIR):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             splitresult = split_path(result)
             print (splitresult)

#------------------------------------------------------------------------------

pathVDF = ("C:\\Program Files (x86)\\Steam\\userdata\\", steamID, "\\config\\shortcuts.vdf ")
name = ""
path = ''
start = ""
hidden = "0 "
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
inVRLibrary = ""
last_playtime = "0 "
categories = ""

#--------------------------------------------------------------------------------
#steam shortcut maker python script shortcut
shortcut = ('python shortcuts.py')
#--------------------------------------------------------------------------------
#extensions = (pathVDF, splitpath, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary, last_playtime, categories)
close = input ("press enter to close")
if (close == ""):
    os.system("python cleanup.py")
