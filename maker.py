import sys
result = ("")
dir1 = input ('what is your itch.io folder (I.E. C:\\Users\\user\\itch\\games)')
file1 = open('apps.txt','w')

import os
for root, dirs, files in os.walk(dir1):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             file1.write(result)
             
file1.close()

pathVDF = ("C:\\Program Files (x86)\\Steam\\userdata\\UserID\\config\\shortcuts.vdf ")
name = ""
path = ''
start = ""
hidden = "0 "
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
inVRLibrary = ""
last_playtime = "0 "
catagories = ""

name = input ("what is the name of the game")
path = input ("paste the entire path to EXE(I.E. C:\\Users\\user\\games\\game.exe)")
start = input ("paste directory with exe in it(I.E. C:\\Users\\user\\games)")
inVRLibrary = input ("if it is a VR game, press 1, otherwise press 0")
categories = input ("are there and cagetorgies you want the game in(I.E. RTS, FPS, simulation)")


print (pathVDF, name, " ",path, " ",start, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary," ", last_playtime, categories)
file1.write("")
file1.close()
input ("press enter to close")
