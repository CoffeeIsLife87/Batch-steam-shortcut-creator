#second attempt
import sys, os
check1 = 0
itchDIRfile = open("info\\itchDIR.txt", 'r+')
while (check1 < 1):
    if itchDIRfile.readline(1) == " ":
        itchDIR = input("copy and paste itch games directory ")
        itchDIRfile.write(itchDIR)
        check1 = 1
    else:
        itchDIR = itchDIRfile.readline()

 
for root, dirs, files in os.walk(itchDIR):
    for file in files:
        if file.endswith(".exe"):
            exepaths = (os.path.join(root, file))
            (exepaths, '\n')