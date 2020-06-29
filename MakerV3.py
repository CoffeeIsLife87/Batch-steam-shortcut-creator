import os , platform , string , time , getpass

#----------------------------------------------------------
#variables
UserName = getpass.getuser()
OS = platform.system()

Blacklist = open("info/blacklist.txt" , 'r')
BLread = Blacklist.read()
BLread = BLread.replace('"','')
BLread = tuple(BLread.split(' , '))
#----------------------------------------------------------
#Functions
def split_path(path):
    path = path
    if OS == "Windows":
        start, name = path.rsplit("\\", 1)
        name , junk = (name.split('.', 1))
    if OS == "Linux":
        start, name = path.rsplit("/", 1)
        name , junk = (name.split('.', 1))
            #name path start icon
    return ('"%s" "%s" "%s" "%s"'%(name , path , start , path))#this line makes sure that everything is spaced properly as well as adds double quotes to the names/paths

def GetInstallLocation():
    global SteamLocal , SteamIDnum
    if OS == "Windows":
        if os.path.exists("C:\\Program Files (x86)\\Steam"):
            SteamLocal = "C:\\Program Files (x86)\\Steam"
            IDCheck = "%s\\userdata"%(SteamLocal)
            for root , dirs , files in os.walk(IDCheck):
                for dir in dirs:
                    if len(dir) == 9:
                        SteamIDnum = dir
                        continue
        else:
            time.sleep(0.5)
            print("\nNon-standard install of steam detected!\n\nIs it ok if I scan for it?\n")
            ValidAnswer = 1
            while ValidAnswer == 1:
                ScanCheck = input("(y/n)")
                if ScanCheck == "y":
                    DriveLetters = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
                    ValidAnswer = 0
                    for i in DriveLetters:
                        i = i+"\\"
                        for Root , Dirs , Files in os.walk(i):
                            for file in Files:
                                if file == "steam.exe":
                                    SteamLocal = Root
                                    print ('\nfound steam install in "%s"'%SteamLocal)
                                    continue
                    IDCheck = "%s\\userdata"%(SteamLocal)
                    for root , dirs , files in os.walk(IDCheck):
                        for dir in dirs:
                            if len(dir) == 9:
                                SteamIDnum = dir
                                continue
                if ScanCheck == "n":
                    ValidAnswer = 0
                    UserError = 1
                    SteamLocal = input(" \nSince you didn't want to scan for it can you copy and paste the location of the steam base folder (The one that has steam.exe in it)\n")
                    if os.path.exists(SteamLocal):
                        IDCheck = "%s\\userdata"%(SteamLocal)
                        for root , dirs , files in os.walk(IDCheck):
                            for dir in dirs:
                                if len(dir) == 9:
                                    SteamIDnum = dir
                                    continue
                    else:
                        while UserError == 1:
                            SteamLocal = input("Looks like the path you entered isn't valid\n\nplease make sure the path you are entering is correct\n")
                            if os.path.exists(SteamLocal):
                                for Root , Dirs , Files in os.walk(SteamLocal):
                                    for file in Files:
                                        if file == "steam.exe":
                                            UserError = 0
                                            IDCheck = "%s\\userdata"%(SteamLocal)
                                            for root , dirs , files in os.walk(IDCheck):
                                                for dir in dirs:
                                                    if len(dir) == 9:
                                                        SteamIDnum = dir
                                                        continue
                                            continue
    if OS == "Linux":
        for Root , Dirs , Files in os.walk("/"):
            for file in Files:
                if file == "steam.sh":
                    SteamLocal = Root
                    print ('\nfound steam install in "%s"'%SteamLocal)
                    continue
        IDCheck = "%s/userdata"%(SteamLocal)
        for root , dirs , files in os.walk(IDCheck):
            for dir in dirs:
                if len(dir) == 9:
                    SteamIDnum = dir
                    continue
    return SteamIDnum , SteamLocal

def getsettings():
    global SteamID , InstallLocation , DefaultCleanout
    #settings are layed out like "SteamID , Steam Install Location , cleanout by default"
    SettingFile = open("info/settings" , 'r')
    SavedSettings = SettingFile.read()
    SteamID , InstallLocation , DefaultCleanout = SavedSettings.split(' , ')
    if SavedSettings == "'' , '' , ''":
        print ("\n\nLooks like you have never used this tool before (or you downloaded a new version or something)\nlets go through some setup.\n")
        time.sleep(0.5)
        properanswer = 0
        while properanswer == 0:
            DefaultCleanout = input("would you like to clean out old shortcuts before adding new ones? (y/n)")
            if DefaultCleanout == ("y"):
                Cleanout = "yes"
                properanswer = 1
            if DefaultCleanout == ("n"):
                Cleanout = "no"
                properanswer = 1
        GetInstallLocation()
        SettingsWrite = open("info/settings" , 'w')
        SteamID = SteamID.replace(SteamID , SteamIDnum)
        InstallLocation = InstallLocation.replace(InstallLocation , SteamLocal)
        FullSettings = ('%s , "%s" , %s'%(SteamID , InstallLocation , Cleanout))
        SettingsWrite.write(FullSettings)
    return SteamID , InstallLocation , DefaultCleanout

def Cleanout():
    global ReplaceVDF
    ReplaceVDF = ("%s/userdata/%s/config"%(InstallLocation.replace('"','') , SteamID))
    if DefaultCleanout == 'yes':
        BaseVDF = "info/shortcuts.vdf"
        if OS == "Windows":
            os.system('del "%s\\shortcuts.vdf"'%(ReplaceVDF))
            os.system('copy "%s" "%s"'%(BaseVDF , ReplaceVDF))
        if OS == "Linux":
            os.system('rm "%s/shortcuts.vdf"'%(ReplaceVDF))
            os.system('cp "%s" "%s"'%(BaseVDF , ReplaceVDF))
    return

def CloseSteam():
    if OS == "Windows":
        os.system('"%s\\steam.exe" -shutdown'%(InstallLocation.replace('"',''))) #this closes steam before running the rest of the script
    if OS == "Linux":
        try:
            os.system("killall -HUP steam")
        except:
            print("Steam isn't running. Won't try to stop it")
    return

def CheckDirs():
    F = open("info/Dirs.txt" , 'r')
    CheckForSplit = F.read()
    if CheckForSplit == '':
        if OS == "Windows":
            print ("\nNow lets add some folders for scanning!")
            DirsToCheck = input('\nWhat Directories would you like to have scanned?\nIf you are doing multiple then seperate them as follows:\n       C:\\Games\\ItchGames , C:\\Games\\EpicGames , C:\\Games\\OtherGames\nMake sure that you seperate all your directories with space and then a comma and then another space " , " \n')
            WriteDirs = open("info\\Dirs.txt" , 'w')
            WriteDirs.write(DirsToCheck)
        if OS == "Linux":
            DirsToCheck = input('\nWhat Directories would you like to have scanned\nIf you are doing multiple then seperate them as follows\n       /home/%s/.config/itch/apps , /home/other/Games\nMake sure that you seperate all your directories with space and then a comma and then another space " , " '%UserName)
            WriteDirs = open("info/Dirs.txt" , 'w')
            WriteDirs.write(DirsToCheck)
    if CheckForSplit == '':
        CheckForSplit = WriteDirs
    if " , " in CheckForSplit:
        print("found a split")
        PathExists = CheckForSplit.split(" , ")
        for CheckPath in PathExists:
            if os.path.exists(CheckPath):
                getfiles(CheckPath)
            else:
                print('it looks like "%s" is an invalid directory'%CheckPath)
    else:
        if os.path.exists(CheckForSplit.replace("\n",'')):
            getfiles(CheckForSplit.replace("\n",''))
        else:
            print('it looks like "%s" is an invalid directory'%CheckForSplit)

def getfiles(dir):
    LastFile = ""
    for Root , Dirs , Files in os.walk(dir):
        for file in Files:
            if OS == "Windows":
                if file.endswith(".exe"):
                    ExeFile = (os.path.join(Root , file))
                    InBlacklist(ExeFile)
            if OS == "Linux":
                CheckFile = os.path.join(Root , file)
                ExeCheck = os.access(CheckFile, os.X_OK)
                if str(ExeCheck) == "True":
                    if str(LastFile) in file:
                        pass
                    else:
                        ExecFile = (os.path.join(Root , file))
                        InBlacklist(ExecFile)
                    if "." in file:
                        LastFile = file.split(".",1)
                    else:
                        LastFile = file

def InBlacklist(File):
    BLCheck = 0
    if File.endswith(BLread):
        BLCheck = 1
    if "MACOSX" in File:
        BLCheck = 1
    if 'windows-i686' in File:
        BLCheck = 1
    if File.endswith(".so"):
        BLCheck = 1
    if File.endswith(".dll"):
        BLCheck = 1
    if BLCheck == 0:
        VRDLLcheck(File)

def VRDLLcheck(File):
    global LaunchOptions , inVRLibrary
    LaunchOptions = '""'
    inVRLibrary = "0"
    if OS == "Windows":
        DLLcheck, junk = File.rsplit("\\", 1)
        for base, sub, FL in os.walk(DLLcheck):
            for file in FL:
                if file.endswith(".dll"):
                    DLLcheck1 = file
                    if (DLLcheck1 == "openvr_api.dll"):
                        inVRLibrary = ("1")
                        LaunchOptions = ('"-vr -vrmode openvr -HmdEnable 1"')
        DLLcheck, junk = File.rsplit("\\", 1)
        for base, sub, FL in os.walk(DLLcheck):
            for file in FL:
                if file.endswith(".dll"):
                    DLLcheck1 = file
                    if (DLLcheck1 == "OVRPlugin.dll"):
                        if inVRLibrary == ("0"):
                            LaunchOptions = ('"-vr -vrmode oculus"')
                        inVRLibrary = ("1")
    AddShortcut(File)

def AddShortcut(File):
    if OS == "Windows":
        Run = ('"%s\\shortcuts.vdf" %s "" %s 0 1 1 %s 0 "Non-Steam-Game"'%(ReplaceVDF , split_path(File) , LaunchOptions , inVRLibrary))
        os.system("python shortcuts.py %s"%Run)
    if OS == "Linux":
        Run = ('"%s/shortcuts.vdf" %s "" %s 0 1 1 %s 0 "Non-Steam-Game"'%(ReplaceVDF , split_path(File) , LaunchOptions , inVRLibrary))
        os.system("python3 shortcuts.py %s"%Run)

def main():
    getsettings()
    CloseSteam()
    Cleanout()
    CheckDirs()
    return

main()
