import sys, subprocess, os
result = ("")
dir1 = input ('what is your itch.io folder (I.E. C:\\Users\\user\\itch\\games)')
file1 = open('apps.txt','w')

#scans directory for .exe files
import os
for root, dirs, files in os.walk(dir1):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             #writes the results to a file
             file1.write (result + '\n')
             
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
    print (steamID)
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

#this bit usually asks what the name and paths are but I disabled it for testing purposes

#name = input ("what is the name of the game")
#path = input ("paste the entire path to EXE(I.E. C:\\Users\\user\\games\\game.exe)")
#start = input ("paste directory with exe in it(I.E. C:\\Users\\user\\games)")
#inVRLibrary = input ("if it is a VR game, press 1, otherwise press 0")
#categories = input ("are there and cagetorgies you want the game in(I.E. RTS, FPS, simulation)")

#--------------------------------------------------------------------------------
#steam shortcut maker python script shortcut
shortcut = (os.system('python shortcuts.py'))
#--------------------------------------------------------------------------------

def split_path(path):
  full_path = path
  path_to_exe, game_name = path.rsplit("\\", 1)
  return name, full_path, path_to_exe.split(".")[0]
  path_data = split_path(path)
#splits full path into smaller bits 
#--------------------------------------------------------------------------------

LineToRead = 1
counter = 0
amount = (1)
file = open("apps.txt", 'r')
#while loop ensures that all of the dirs are scanned
while (counter < amount):
#checks if the line is empty and moves the script forward if it is
    if (file.readline(LineToRead) == ""):
            counter += 1
#reads what the line is and splits it
    else:
            file.readline(LineToRead)
            pathedit = (file.read())
            pathsplits = split_path(pathedit)
            extensions = (pathVDF, pathsplits, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary," ", last_playtime, categories)
            os.system(f 'python shortcuts{extensions}')
            LineToRead = LineToRead + 1
file.close()
#reads each line
#-------------------------------------------------------------------------------

extensions = (pathVDF, pathsplits, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary," ", last_playtime, categories)
close = input ("press enter to close")
if (close == ""):
    subprocess.call('cleanup.bat')
