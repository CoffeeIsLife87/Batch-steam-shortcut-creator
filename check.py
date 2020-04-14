import sys,os #because that is what you do
blacklist = ("ffmpeg.exe","unins000.exe", "UnityCrashHandler64.exe", "UnityCrashHandler32.exe", "UnrealCEFSubProcess.exe", "UE4PrereqSetup_x64.exe", "dxwebsetup.exe","uninstall.exe","vc_redist","oalinst.exe","UE4Game-Win64-Shipping.exe","pythonw.exe","python.exe","Spatial Media Metadata Injector.exe","zsync.exe","zsyncmake.exe")
#-------------------------------------------------------------------
#checks for itch.io directory to scan and askes for one if it is not detected
itchDIRfile = open('info\\itchDIR.txt', 'r+')
itchDIRcheck = itchDIRfile.readline()
if (itchDIRcheck == ""):
    itchDIR = input("copy and paste itch games directory ")
    itchDIRfile.write(itchDIR)
    itchDIRfile.close
else:
    itchDIR = itchDIRcheck
    #print (itchDIR) #for debugging
# ItchDir is necissary for checking finding what files do and don't exist
#-------------------------------------------------------------------
#checks for steam ID or askes for it if it is not detected
steamIDfile = open('info\\steamID.txt', 'r+')
steamIDcheck = steamIDfile.readline()
if (steamIDcheck == ""):
    steamIDpath = "C:\\Program Files (x86)\\Steam\\userdata"
    #opens steam user folder for users so they can copy and paste the numbers that represent their ID
    steamIDpath = os.path.realpath(steamIDpath)
    os.startfile(steamIDpath)
    steamID = str(input("copy and paste the numbers from the folder"))
    steamIDfile.write(steamID)
    steamIDfile.close()
else:
    steamID = steamIDcheck
    #print (steamID) #for debugging
pathVDF = ("C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf") #this is the file it will read and write to
#-------------------------------------------------------------------

startswith = ('\x08\x08') #this will be useful for finding a starting/ending point for deletion when something is missing
readVDF = open(str(pathVDF))#this is what we are reading off of
VDFsplit = readVDF.read()# shortcuts.vdf is a single line file so we don't have to use .readline()


#check for a path in itchDIR
#read the shortcuts.vdf file
#start checking for startswith var backwards through the file (this is just a rough draft that I wanted to remember. you don't have to follow this)
#when found set the character position
#check for the path found by the itchdir scan
#if a file is present in shortcuts.VDF that is not in the itch dir then it will be removed based on the opening \x08\x08 and the \x08\x08 that triggers the beginning of the next shortcut

#this does the opisite of what I want
#as of right now it checks the dirs for files and make sure they are on shortcuts.vdf
#I want it to do the oposite
def SplitIntoATon(pathVDF):
    for root, dirs, files in os.walk(itchDIR):
        for file in files:
            if file.endswith(".exe"):
                 result = (os.path.join(root, file))
                 check = VDFsplit.find(result)
                 if (check == -1):
                     print(result)
                 else:
                     print("good")

                 
    if (check == -1):
        found = ("I was able to clean out")
    else:
        found = ("none have been found")
    return (found)



full_appName        =  '\x01'  +  'appname'             +  '\x00'  +  '\x00'
full_quotedPath     =  '\x01'  +  'exe'                 +  '\x00'  +  '\x00'
full_startDir       =  '\x01'  +  'StartDir'            +  '\x00'  +  '\x00'
full_iconPath       =  '\x01'  +  'icon'                +  '\x00'  +  '\x00'
full_shortcutPath   =  '\x01'  +  'ShortcutPath'        +  '\x00'  +  '\x00'
full_launchOptions  =  '\x01'  +  'LaunchOptions'       +  '\x00'  +  '\x00'
full_isHidden       =  '\x02'  +  'IsHidden'            +  '\x00'  +  '\x00\x00\x00'
full_allowDeskConf  =  '\x02'  +  'AllowDesktopConfig'  +  '\x00'  +  '\x00\x00\x00'
full_allowOverlay   =  '\x02'  +  'AllowOverlay'        +  '\x00'  +  '\x00\x00\x00'
full_openVR         =  '\x02'  +  'OpenVR'              +  '\x00'  +  '\x00\x00\x00'
full_lastPlayTime   =  '\x02'  +  'LastPlayTime'        +  '\x00'
full_tags           =  '\x00'  +  'tags'                +  '\x00'  +  '\x08\x08'

startswith + full_appName + full_quotedPath + full_startDir + full_iconPath + full_shortcutPath + full_launchOptions + full_isHidden + full_allowDeskConf + full_allowOverlay + full_openVR + full_tags

print (SplitIntoATon(pathVDF))