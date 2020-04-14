# this is my attempt at removing apps that don't exist anymore
# if I can read the shortcuts.VDF file and determine all of the existing shortcuts than I can scan the itch dir for the exe files
# I can then delete the bits that contain the data of the unused shortcut


import crc_algorithms,sys,os
#-------------------------------------------------------------------------------------
#using the file from maker.py I can determine the file path
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

pathVDF = ('"'+"C:\\Program Files (x86)\\Steam\\userdata\\"+steamID+"\\config\\shortcuts.vdf"+'"'+" ")

VDFread = open(pathVDF,'r')