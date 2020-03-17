result = ("")
import os
for root, dirs, files in os.walk("B:\itch apps"):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))
             print (result)


appname = "epic games store"
exepath = '"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"'
DirWithExe = '"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32"'
LuanchOptions = input("do you have launch options, press enter if no")
if (LuanchOptions == ""):
    LuanchOptions = ""
print (LuanchOptions)
    
    



print ("AppName ", appname, "Exe" , exepath,"StartDir ", DirWithExe," icon ShortcutPath", LuanchOptions, "ishidden AllowDesktopConfig    AllowOverlay    openvr    Devkit  DevkitGameID  LastPlayTime")
