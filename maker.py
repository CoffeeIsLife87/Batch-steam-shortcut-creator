result = ("")
import os
for root, dirs, files in os.walk("B:\itch apps"):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))



pathVDF = ("C:\\Program Files (x86)\\Steam\\userdata\\876672695\\config\\shortcuts.vdf ")
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
path = input ("paste the entire path to EXE")
start = input ("paste directory with exe in it(don't add the exe to the path)")
inVRLibrary = input ("if it is a VR game, press 1, otherwise press 0")
categories = input ("are there and cagetorgies you want the game in")


print (pathVDF, name, " ",path, " ",start, " ", hidden, allow_desktop_config, allow_steam_overlay, inVRLibrary," ", last_playtime, categories)
