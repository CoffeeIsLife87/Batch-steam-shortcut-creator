#----------------------------------------------------------------------------------------------------------------------------------------------------

# ToDo

# fix not being able to add games with path/name with "&" symbol (I have no clue how to do this) (low priority)
# add the option to add all the games to favorite (is there a tag for that?) (medium priority)

#let me know if there is something else you want me to add

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Finished features

# be able to remove game/tools after you delete them(this is not a foolproof method right now)
# add detection for non-standard installations of steam 
# allow multiple paths to scan (Is there an elegant method of doing this? YES! There is!) (medium prioity)

#----------------------------------------------------------------------------------------------------------------------------------------------------

import sys, os, getpass
#----------------------------------------------------------------------------------------------------------------------------------------------------

#functions

#this splits the path into a name, a full path, and the directory the game is in (credit to someone in the python discord for this bit)
def split_path(path):
  path = path
  start, name = path.rsplit("\\", 1)
  #that makes sure that everything is spaced properly as well as adds double quotes to the names/paths
  return '"'+name.split(".")[0]+'"'+" "+'"'+path+'"'+" "+'"'+start+'"'

shortcut = ('py -2 shortcuts.py') #this will be used later for running the second python script with the arguments after it
#----------------------------------------------------------------------------------------------------------------------------------------------------

# Standard path check
if os.path.exists("C:\\Program Files (x86)\\Steam\\steam.exe"):
    StandardSteamInstall = 1
else:
    StandardSteamInstall = 0
    Install = open('info\\NonStandardLocal.txt', 'r+')
    ReadInstall = Install.read()
    SteamInstall = ReadInstall
    if SteamInstall == "":
        print ("non-standard installation of steam detected")
        SteamInstall = input("please copy and paste you steam folder location (I.E. A:\\steaminstallfolder) don't do (A:\\steaminstallfolder\\) or IT WILL NOT WORK")
        Install.write(SteamInstall)
        Install.close()
#----------------------------------------------------------------------------------------------------------------------------------------------------
if StandardSteamInstall == 1:
    os.system('cmd /c '+'"C:\\Program Files (x86)\\Steam\\steam.exe" -shutdown') #this closes steam before running the rest of the script
if StandardSteamInstall == 0:
    os.system('cmd /c '+'"'+SteamInstall+'\\steam.exe" -shutdown')
#----------------------------------------------------------------------------------------------------------------------------------------------------

#checks for itch.io directory to scan and askes for one if it is not detected
DIRfile = open('info\\Dirs.txt', 'r+')
DIRcheck = DIRfile.read()
if (DIRcheck == ""):
    DIR = input("all of the directories you want scanned divided by a ',' (I.E. 'C:\\DirOne , C:\\DirTwo , B:\\games\\Itch games').\n This will work with only one directory only if you want to do 'C:\\itch games' or something of that nature ")
    DIRfile.write(DIR)
    DIRfile.close()
else:
    DIR = DIRcheck
    #print (DIR) #for debugging
#----------------------------------------------------------------------------------------------------------------------------------------------------

#checks for steam ID or askes for it if it is not detected
steamIDfile = open('info\\steamID.txt', 'r+')
steamIDcheck = steamIDfile.read()
# I had to rearange some stuff so it was easier to manage so if some things have comments that seem out of place that is why
#-------------------------------------------------------------------------------

if StandardSteamInstall == 1:
    if (steamIDcheck == ""):
        steamIDpath = "C:\\Program Files (x86)\\Steam\\userdata"
        steamIDpath = os.path.realpath(steamIDpath)
        os.startfile(steamIDpath) #opens steam user folder for users so they can copy and paste the numbers that represent their ID
        steamID = str(input("copy and paste the numbers from the folder"))
        steamIDfile.write(steamID)
        steamIDfile.close()
    else:
        steamID = steamIDcheck
        #print (steamID) #for debugging
if StandardSteamInstall == 1:
    pathVDF = ('"'+"C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"'+" ")
    FullVDF = ('"'+"C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"')
    splitVDF = ('"'+"C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config") #this is where it gets copied to 
#-------------------------------------------------------------------------------

if StandardSteamInstall == 0:
    if (steamIDcheck == ""):
        steamIDpath = (SteamInstall+"\\userdata")
        steamIDopen = os.path.realpath(steamIDpath)
        os.startfile(steamIDopen) #opens steam user folder for users so they can copy and paste the numbers that represent their ID
        steamID = str(input("copy and paste the numbers from the folder"))
        steamIDfile.write(steamID)
        steamIDfile.close()
    else:
        steamID = steamIDcheck
        #print (steamID) #for debugging
if StandardSteamInstall == 0:
    pathVDF = ('"'+SteamInstall+"\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"'+" ")
    FullVDF = ('"'+SteamInstall+"\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"')
    splitVDF = ('"'+SteamInstall+"\\userdata\\"+steamID+"\\config") #this is where it gets copied to 
readVDF = ('info\\shortcuts.vdf')
#----------------------------------------------------------------------------------------------------------------------------------------------------

# this replaces my windows username with the actual user's windows username
readVDF1 = open('info\\shortcuts.vdf', 'r+')
readVDF2 = readVDF1.read()
#print(readVDF2) # for debugging

#----------------------------------------------------------------------------------------------------------------------------------------------------
#this portion checks if you want to have it clean out as well as ask if the user wants to do this by default
DefaultCleanBehaviour = open('info\\CleanoutByDefault.txt', 'r+')
Defaultcheck = DefaultCleanBehaviour.read()

EnsureCleanout = 1
if Defaultcheck == "yes" or "no":
    Cleanoutcheck = Defaultcheck
while EnsureCleanout == 1:
    if Cleanoutcheck == "yes" or "no":
        if Cleanoutcheck == "yes":
            DoCleanout = 1
            EnsureCleanout = 0
        if Cleanoutcheck == "no":
            DoCleanout = 0
            EnsureCleanout = 0
    if Cleanoutcheck == "":
        Cleanoutcheck = input("Do you want to clean old shortcuts? if you pick yes than any programs that aren't in the directories you set then they will be removed ('yes' or 'no') ")

EnsureCleanout = 1

if Defaultcheck == "":
    WriteDefaultBehaviour = open('info\\CleanoutByDefault.txt', 'r+')
    while (EnsureCleanout == 1):
        DefaultAsk = input("would you like to clean out by default('yes' or 'no') ")
        if DefaultAsk == "yes":
            WriteDefaultBehaviour.write(DefaultAsk)
            WriteDefaultBehaviour.close()
            EnsureCleanout = 0
        if DefaultAsk == "no":
            WriteDefaultBehaviour.write(DefaultAsk)
            WriteDefaultBehaviour.close()
            EnsureCleanout = 0

#----------------------------------------------------------------------------------------------------------------------------------------------------

StartDefault = ("C:\\Users\\heros\\OneDrive\\Documents\\GitHub\\autoItchtoSteamlibrary\\placeholder\\")
FullDefault = ("C:\\Users\\heros\\OneDrive\\Documents\\GitHub\\autoItchtoSteamlibrary\\placeholder\\placeholder.exe")
CWD = os.getcwd()
andcheck = 0
#-------------------------------------------------------------------------------

Junk, SplitStart = StartDefault.split("\\GitHub", 1)
Start = (CWD+SplitStart)
#print (Start) #debugging
#print (SplitStart) #debugging
#-------------------------------------------------------------------------------

junk, SplitFull = FullDefault.split("\\GitHub", 1)
Full = (CWD+SplitFull)
#print (Full) #debugging
#print (SplitFull) #debugging
#-------------------------------------------------------------------------------

NewShortCut = readVDF2.replace(StartDefault,Start)
NewShortCut = NewShortCut.replace(FullDefault,Full)
#print (NewShortCut) #debugging
writeVDF = open('info\\shortcuts.vdf', 'w')
writeVDF.write(NewShortCut)
writeVDF.close()
#----------------------------------------------------------------------------------------------------------------------------------------------------
# this is cleanup (if the user said not to cleanout than this section does nothing)

#thing/path of thing to copy 
shortcuts = ("info\\shortcuts.vdf") #this is the file being copied
copier = (CWD+"\\"+shortcuts+" "+splitVDF) # I don't know why this is how I did it
#------------------------------------------------------------------------------

if DoCleanout == 1:
    os.system("cmd /c del "+FullVDF) #removes outdated
    os.system("cmd /c copy "+copier) #adds the blank slate (minus the placeholder necissary for the script to work)
#os.system("cmd /c del "+FullVDF) #removes outdated
#os.system("cmd /c copy "+copier) #adds the blank slate (minus the placeholder necissary for the script to work)
#----------------------------------------------------------------------------------------------------------------------------------------------------

# A bunch of variables that will be needed later
name = "" #this gets defined later
path = ''# same
start = ""# same
hidden = " 0 " #change the "0" to a "1" for hidden if you want to hide all the games that this tool adds 
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
last_playtime = "0 " 
categories = '"non-steam-game" "FAVORITES" ' #I have the categories set as non steam game but if you want to set it as something else then feel free

#extensions = (pathVDF+cleanresult+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories) #this is a template in case I have to move stuff around
#----------------------------------------------------------------------------------------------------------------------------------------------------
SplitDir = DIR.split(",")
#print (SplitDir)
for i in SplitDir:
    #scans set directory for .exe files
    for root, dirs, files in os.walk(i):
        for file in files:
            if file.endswith(".exe"):
                 result = (os.path.join(root, file))             
#----------------------------------------------------------------------------------------------------------------------------------------------------
# the next subsection if a VR check to add the game to your VR library if it's sub/root folders have a certain .dll file (no its not flawless, but it gets the job done for now)
                #this is the openVR_api check
                 inVRLibrary = "0 "
                 DLLcheck, junk = result.rsplit("\\", 1)
                 for base, sub, FL in os.walk(DLLcheck):
                     for file in FL:
                         if file.endswith(".dll"):
                             DLLcheck1 = file
                             if (DLLcheck1 == "openvr_api.dll"):
                                 inVRLibrary = ("1 ")
                 #this is the OVRplugin check
                 DLLcheck, junk = result.rsplit("\\", 1)
                 for base, sub, FL in os.walk(DLLcheck):
                     for file in FL:
                         if file.endswith(".dll"):
                             DLLcheck1 = file
                             if (DLLcheck1 == "OVRPlugin.dll"):
                                 inVRLibrary = ("1 ")
                #-----------------------------------------------------------------
                 splitresult = split_path(result)
                 if ("&" in (result)):
                     andcheck = 1
                     result = ("\r"+result)
                     splitresult = ("\r"+splitresult)
                     print (splitresult)
                 #else:
                    #the below lines are for ensuring you don't have a 1,000,000,000 setup/uninstaller tools
                    #if you find something you know people will never use please add it to the blacklist for me
                     blacklist = ("ffmpeg.exe","unins000.exe", "UnityCrashHandler64.exe", "UnityCrashHandler32.exe", "UnrealCEFSubProcess.exe", "UE4PrereqSetup_x64.exe", "dxwebsetup.exe","uninstall.exe","vc_redist","oalinst.exe","UE4Game-Win64-Shipping.exe","pythonw.exe","python.exe","Spatial Media Metadata Injector.exe","zsync.exe","zsyncmake.exe","Amazon Game Remover.exe","CrashReportClient.exe","-Win64-Shipping.exe","VrContainer32.exe","VrContainer64.exe","ViveportContent.exe","LAUNCHER.exe","LAUNCHER_x64.exe","DXSETUP.exe","vcredist_x86.exe","vcredist_x64.exe","ProLogLauncher.exe","ProLog.exe","QtWebEngineProcess.exe")
                     if result.endswith(blacklist):
                         pass
                     else:
                         if 'windows-i686' in result:
                    # "windows-i686" means that this is a strictly 64bit version of the app/game and often times there 
                    # will be a non exsclusive version of the game as well so I blacklisted this to avoid 
                             pass
                         else:
                             #splitresult = split_path(result)
                             #some notes: the "result" after "splitresult" is to set the game icon
                             extensions = (" "+pathVDF+splitresult+" "+'"'+result+'"'+" "+'""'+" "+'""'+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories)
                             #print (shortcut+extensions) #this line is for checking the output without it making shortcuts coding (the line below must be commented out or it will still make shortcuts)
                             os.system('cmd /c'+'"'+shortcut+extensions+'"')
#----------------------------------------------------------------------------------------------------------------------------------------------------
#just a couple of words for the user
print ("")
print ("thanks for using my tool")
print ("")
print ("let me know if something broke @ https://github.com/herosilas12/autoItchtoSteamlibrary")
print ("")
if (andcheck == 1):
    print ('BTW one of the apps/games you wanted to add to steam contained the "&" symbol, which for some reason breaks the script so you will have to add that app/game manually. sorry for the inconvienience')
print ("")
print ("")
print ("")
#close = input ("press enter to close")