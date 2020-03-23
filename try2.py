#second attempt
import sys, os
pathText = open("apps.txt", 'w+')
#---------------------------------------------------------------
#this is the itch.io directory setter
check1 = 0
itchDIRfile = open("info\\itchDIR.txt", 'r+')
while (check1 < 1):
    if itchDIRfile.readline(1) == " ":
        itchDIR = input("copy and paste itch games directory ")
        itchDIRfile.write(itchDIR)
        check1 = 1
    else:
        itchDIR = itchDIRfile.readline()
#---------------------------------------------------------------
#checks for steam ID and asks for it if not detected 
steamIDfile = open('info\\steamID.txt', 'r+')
if (steamIDfile.readline(1) == ""):
    steamIDpath = "C:\\Program Files (x86)\\Steam\\userdata"
    steamIDpath1 = os.path.realpath(steamIDpath)
    os.startfile(steamIDpath)
    steamID = str(input("copy and paste the numbers from the folder"))
    steamIDfile.write(steamID)
    steamIDfile.close()
else:
    steamID = steamIDfile.read()

#--------------------------------------------------------------

for root, dirs, files in os.walk(itchDIR):
    for file in files:
        if file.endswith(".exe"):
            exepaths = (os.path.join(root, file))
            pathText.write(exepaths, '\n')