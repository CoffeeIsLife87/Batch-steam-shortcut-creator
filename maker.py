#-------------------------------------------------------------------------------

# ToDo

# fix not being able to add games with path/name with "&" symbol
# add detection for non-standard installations of steam
# add the option to add all the games to favorite (is there a tag for that?)
# allow multiple paths to scan 
# be able to remove game/tools after you delete them

#let me know if there is something else you want me to add


#----------------------------------------------------------------------------------------------
import sys, os
#os.system('cmd /c '+'"C:\\Program Files (x86)\\Steam\\steam.exe" -shutdown')
#----------------------------------------------------------------------------------------------
# this portion is not done yet and may never be done
#checks whether or not the user want the cleanout behaviour by default
#DefaultCleanBehaviour = open('autoItchtoSteamlibrary\\info\\CleanoutByDefault.txt', 'r+')
#Defaultcheck = DefaultCleanBehaviour.readline()

#cleanout = Defaultcheck
#cleanoutcheck = 1
#if cleanout == "":
#    cleanout = input("would you like to clean out deleted apps? ")
#    while (cleanoutcheck == 1):
#        if cleanout == "yes" or "no":
#            if cleanout == "yes":
#                DoCleanout = 1
#                cleanoutcheck = 0
#            else:
#                DoCleanout = 0
#                cleanoutcheck = 0
#        else:
#            cleanout = input('this is a "yes" or "no" question (it might be caps sensitive) ')

#if (Defaultcheck == ""):
#    cleanoutcheck = 1
#    Defaultcheck = input("Do you want the have shortcuts cleaned out by default (useful if you uninstall things all the time for testing ) ")
#    while (cleanoutcheck == 1):
#        if Defaultcheck == "yes" or "no":
#            if Defaultcheck == "yes":
#                DoCleanout = 1
#                DefaultCleanBehaviour.write(Defaultcheck)
#                DefaultCleanBehaviour.close
#                cleanoutcheck = 0
#            else:
#                DoCleanout = 0
#                DefaultCleanBehaviour.write(Defaultcheck)
#                DefaultCleanBehaviour.close
#        else:
#            Defaultcheck = input('this is, once again, a "yes" or "no" question (it might be caps sensitive) ')
#    DefaultCleanBehaviour.write(Defaultcheck)
#    DefaultCleanBehaviour.close
#else:
#    cleanout = Defaultcheck
#    if Defaultcheck == "yes":
#        DoCleanout = 1
#print (Defaultcheck) #for debugging

#-------------------------------------------------------------------------------
#functions

#this splits the path into a name, a full path, and the directory the game is in (credit to someone in the python discord for this bit)
def split_path(path):
  path = path
  start, name = path.rsplit("\\", 1)
  #that makes sure that everything is spaced properly as well as adds double quotes to the names/paths
  return '"'+name.split(".")[0]+'"'+" "+'"'+path+'"'+" "+'"'+start+'"'

shortcut = ('py -2 autoItchtoSteamlibrary\\shortcuts.py') #this will be used later for running the second python script with the arguments after it
#-------------------------------------------------------------------------------
#checks for itch.io directory to scan and askes for one if it is not detected
itchDIRfile = open('autoItchtoSteamlibrary\\info\\itchDIR.txt', 'r+')
itchDIRcheck = itchDIRfile.readline()
if (itchDIRcheck == ""):
    itchDIR = input("copy and paste itch games directory ")
    itchDIRfile.write(itchDIR)
    itchDIRfile.close
else:
    itchDIR = itchDIRcheck
    #print (itchDIR) #for debugging
#-------------------------------------------------------------------------------
#checks for steam ID or askes for it if it is not detected
steamIDfile = open('autoItchtoSteamlibrary\\info\\steamID.txt', 'r+')
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

#if you installed steam somewhere other than the default location then uncomment the following lines and put the path the your "shortcuts.vdf file"
#emergencyVDF = ('"'+"your path here"+'"'+" ")
#pathVDF = emergencyVDF
#-------------------------------------------------------------------------------
#comment out line 47 if you need to use emergencyVDF
pathVDF = ('"'+"C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"'+" ")
#-------------------------------------------------------------------------------
#this portion is not done

#editVDF = ("C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf")
#edit = open(editVDF, 'w')
 
#this long string of text if a placeholder for the script to work
#placeholder = '"\x00shortcuts\x00\x000\x00\x01appname\x00placeholder\x00\x01exe\x00"C:\\Users\\heros\\OneDrive\\Documents\\GitHub\\autoItchtoSteamlibrary\\placeholder\\placeholder.exe"\x00\x01StartDir\x00"C:\\Users\\heros\\OneDrive\\Documents\\GitHub\\autoItchtoSteamlibrary\\placeholder\\"\x00\x01icon\x00\x00\x01ShortcutPath\x00\x00\x01LaunchOptions\x00\x00\x02IsHidden\x00\x00\x00\x00\x00\x02AllowDesktopConfig\x00\x01\x00\x00\x00\x02AllowOverlay\x00\x01\x00\x00\x00\x02OpenVR\x00\x00\x00\x00\x00\x02Devkit\x00\x00\x00\x00\x00\x01DevkitGameID\x00\x00\x02LastPlayTime\x00\x00\x00\x00\x00\x00tags\x00\x08\x08'
#print (placeholder) # for debugging
#if DoCleanout == 1:
#    edit.writelines('380')
#    edit.close()

#-------------------------------------------------------------------------------
# A bunch of variables that will be needed later
name = "" #this gets defined later
path = ''# same
start = ""# same
hidden = " 0 " #change the "0" to a "1" for hidden if you want to hide all the games that this tool adds 
allow_desktop_config = "1 "
allow_steam_overlay = "1 "
last_playtime = "0 " 
categories = '"non-steam-game"' #I have the categories set as non steam game but if you want to set it as something else then feel free

#extensions = (pathVDF+cleanresult+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories) #this is a template in case I have to move stuff around
#-------------------------------------------------------------------------------
#scans set directory for .exe files
for root, dirs, files in os.walk(itchDIR):
    for file in files:
        if file.endswith(".exe"):
             result = (os.path.join(root, file))             
#-----------------------------------------------------------------------------------------------
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
             andcheck = "no and"
             if ("&" in (result)):
                 andcheck = "there is an &"
             else:
                #the below lines are for ensuring you don't have a 1,000,000,000 setup/uninstaller tools
                #if you find something you know people will never use please add it to the blacklist for me
                 blacklist = ("ffmpeg.exe","unins000.exe", "UnityCrashHandler64.exe", "UnityCrashHandler32.exe", "UnrealCEFSubProcess.exe", "UE4PrereqSetup_x64.exe", "dxwebsetup.exe","uninstall.exe","vc_redist","oalinst.exe","UE4Game-Win64-Shipping.exe","pythonw.exe","python.exe","Spatial Media Metadata Injector.exe","zsync.exe","zsyncmake.exe")
                 if result.endswith(blacklist):
                    pass
                 else:
                     if 'windows-i686' in result:
 # "windows-i686" means that this is a strictly 64bit version of the app/game and often times there 
 # will be a non exsclusive version of the game as well so I blacklisted this to avoid 
                         pass
                     else:
                        splitresult = split_path(result)
                        #some notes: the "result" after "splitresult" is to set the game icon
                        extensions = (" "+pathVDF+splitresult+" "+'"'+result+'"'+" "+'""'+" "+'""'+" "+hidden+allow_desktop_config+allow_steam_overlay+inVRLibrary+last_playtime+categories)
                        #print (shortcut+extensions) #this line is for checking the output without it making shortcuts coding (the line below must be commented out or it will still make shortcuts)
                        #os.system('cmd /c'+'"'+shortcut+extensions+'"')
#os.system('cmd /c '+'"C:\\Program Files (x86)\\Steam\\steam.exe"')

#--------------------------------------------------------------------------------
#just a couple of words for the user
print ("")
print ("thanks for using my tool")
print ("")
print ("let me know if something broke @ https://github.com/herosilas12/autoItchtoSteamlibrary")
print ("")
if (andcheck == "there is an &"):
    print ('BTW one of the apps/games you wanted to add to steam contained the "&" symbol, which for some reason breaks the script so you will have to add that app/game manually. sorry for the inconvienience')
print ("")
print ("")
print ("")
#close = input ("press enter to close")