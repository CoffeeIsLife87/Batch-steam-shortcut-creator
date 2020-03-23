import sys, subprocess, os
result = ("")
#says where to scan
dir1 = input ('what is your itch.io folder (I.E. C:\\Users\\user\\itch\\games)')
#says where the results are written to
file1 = open('apps.txt','w')
#-------------------------------------------------------------------------------
#scans directory for .exe files
import os
for root, dirs, files in os.walk(dir1):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             #writes the results to a file
             file1.write (result+'\n')
             
file1.close()
#-------------------------------------------------------------------------------
#checks for steam ID or askes for it if it is not detected
steamIDfile = open('steamID.txt', 'r+')
if (steamIDfile.readline(1) == ""):
    steamIDpath = "C:\\Program Files (x86)\\Steam\\userdata"
    steamIDpath1 = os.path.realpath(steamIDpath)
    os.startfile(steamIDpath)
    steamID = str(input("copy and paste the numbers from the folder"))
    steamIDfile.write(steamID)
    steamIDfile.close()
else:
    steamID = steamIDfile.read()
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

def split_path(path):
  full_path = path
  path_to_exe, game_name = path.rsplit("\\", 1)
  return name, full_path, path_to_exe.split(".")[0]
  path_data = split_path(path)
#splits full path into smaller bits 
#--------------------------------------------------------------------------------
counter = 0
amount = 1
file = open("apps.txt", 'r')
Efile = open("Exec.txt", 'w+')

while (counter < amount):
    if (file.readline() == ""):   #checks if the line is empty and moves the script forward if it is
            counter += 1
#reads what the line is and splits it
    else:
            pathtoedit = file.readline()
            splitpath = split_path(pathtoedit)
            print (splitpath)
            extensions = (pathVDF, splitpath, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary, last_playtime, categories)
            supercmd = str((shortcut, extensions))
            Efile.write(supercmd)
file.close()
#reads each line
#--------------------------------------------------------------------------------
close = input ("press enter to close")
if (close == ""):
    os.system("python cleanup.py")