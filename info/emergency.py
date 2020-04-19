# in case of something breaking run this file and it will reset
# all of the files that get changed by maker.py

Cleanout = open("CleanoutByDefault.txt",'w')
Cleanout.write('')
Cleanout.close()

Dir = open("Dirs.txt",'w')
Dir.write('')
Dir.close()

NonStandard = open("NonStandardLocal.txt",'w')
NonStandard.write('')
NonStandard.close()

steamID = open("steamID.txt",'w')
steamID.write('')
steamID.close()