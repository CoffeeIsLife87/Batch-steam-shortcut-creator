import sys,os #because that is what you do

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
readVDF = open(str(pathVDF))
VDFsplit = readVDF.read()


#check for a path in itchDIR
#read the file
#start checking for startswith var backwards through the file
#when found set the character position
#check for the path found by the itchdir scan
#if a file is present in the shortcuts.VDF file that is not in the itch dir then it will be removed based on the opening \x08\x08 and the following \x08\x08


def SplitIntoATon(pathVDF):
    for root, dirs, files in os.walk(itchDIR):
        for file in files:
            if file.endswith(".exe"):
                 result = (os.path.join(root, file))
                 check = VDFsplit.find(result)
                 if (check == -1):
                     return ("NOT THERE")
                 else:
                     return ("I found it and it is at collumn "+str(check))

print (SplitIntoATon(pathVDF))
