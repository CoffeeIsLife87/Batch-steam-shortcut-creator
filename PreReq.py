import os,sys,getpass

# this replaces my windows username with the actual user's windows username
readVDF1 = open('info\\shortcuts.vdf', 'r+')
readVDF2 = readVDF1.read()
#print(readVDF2) #debugging

StartDefault = ("C:\\Users\\heros\\OneDrive\\Documents\\GitHub\\autoItchtoSteamlibrary\\placeholder\\")
FullDefault = ("C:\\Users\\heros\\OneDrive\\Documents\\GitHub\\autoItchtoSteamlibrary\\placeholder\\placeholder.exe")

CWD = os.getcwd()

Junk, SplitStart = StartDefault.split("\\GitHub", 1)
Start = (CWD+SplitStart)
#print (Start) #debugging
#print (SplitStart) #debugging

junk, SplitFull = FullDefault.split("\\GitHub", 1)
Full = (CWD+SplitFull)
#print (Full) #debugging
#print (SplitFull) #debugging

NewShortCut = readVDF2.replace(StartDefault,Start)
NewShortCut = NewShortCut.replace(FullDefault,Full)
print (NewShortCut) #debugging
writeVDF = open('info\\shortcuts.vdf', 'w')
writeVDF.write(NewShortCut)