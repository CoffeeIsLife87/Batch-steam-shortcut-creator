import os , platform , string , time , getpass 

#----------------------------------------------------------
#variables
#For all of the "_"'s in the script that is an unused variable and pylint doesn't care so that's what I used
OldRoot = "                       "#if I did an empty string it wouldn't work, however, this works unless there is that many/more spaces in a row(I hope no one does that for thier title)
UserName = getpass.getuser()
SkipPath = '         '
OS = platform.system()# for whatever reason when I ported this to macOS catalina platform.system returned Darwin so macOS = Darwin in python

Blacklist = open("info/blacklist.txt" , 'r')
BLread = Blacklist.read()
BLread = BLread.replace('"','')
BLread = tuple(BLread.split(' , '))
#----------------------------------------------------------
#Functions
try:
    def split_path(path):
        Path = path
        if OS == "Windows":
            if path.endswith("index.html"):
                name , _ = Path.split(".")
                S , name , _ = name.rsplit("\\",2)
                start = os.path.join(S , name)
            else:
                start, name = path.rsplit("\\", 1)
                name , _ = (name.split('.', 1))
        if OS == "Linux":
            start, name = path.rsplit("/", 1)
            if path.endswith("index.html"):
                _ , name , _ = path.rsplit("/",2)
                start , _= path.rsplit("/", 1)
            if "." in name:
                name , _ = (name.split('.', 1))
        if OS == "Darwin":
            global SkipPath
            ActualPath , _ = path.split(".app",1)
            Path = ActualPath+".app"
            if SkipPath == '         ':
                SkipPath = ActualPath
            else:
                if ActualPath in SkipPath:
                    pass
                else:
                    SkipPath = "%s\n%s"%(SkipPath , ActualPath)
            start, name = ActualPath.rsplit("/", 1)
            name , _ = (name.split('.', 1))
                #name path start icon
        return ('"%s" "%s" "%s" "%s"'%(name , Path , start , Path))#this line makes sure that everything is spaced properly as well as adds double quotes to the names/paths
    def GetInstallLocation():
        global SteamLocal , SteamIDnum
        if OS == "Windows":
            if os.path.exists("C:\\Program Files (x86)\\Steam"):
                SteamLocal = "C:\\Program Files (x86)\\Steam"
                IDCheck = "%s\\userdata"%(SteamLocal)
                for _ , dirs , _ in os.walk(IDCheck):
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
                            for Root , _ , Files in os.walk(i):
                                for file in Files:
                                    if file == "steam.exe":
                                        SteamLocal = Root
                                        print ('\nfound steam install in "%s"'%SteamLocal)
                                        continue
                        IDCheck = "%s\\userdata"%(SteamLocal)
                        for _ , dirs , _ in os.walk(IDCheck):
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
                            for _ , dirs , _ in os.walk(IDCheck):
                                for dir in dirs:
                                    if len(dir) == 9:
                                        SteamIDnum = dir
                                        continue
                        else:
                            while UserError == 1:
                                SteamLocal = input("Looks like the path you entered isn't valid\n\nplease make sure the path you are entering is correct\n")
                                if os.path.exists(SteamLocal):
                                    for Root , _ , Files in os.walk(SteamLocal):
                                        for file in Files:
                                            if file == "steam.exe":
                                                UserError = 0
                                                IDCheck = "%s\\userdata"%(SteamLocal)
                                                for _ , dirs , _ in os.walk(IDCheck):
                                                    for dir in dirs:
                                                        if len(dir) == 9:
                                                            SteamIDnum = dir
                                                            continue
                                                continue
        if OS == "Linux":
            foundit = 1
            for Root , _ , Files in os.walk("/"):
                if foundit == 1:
                    for file in Files:
                        if file == "steam.sh":
                            foundit = 0
                            SteamLocal = Root
                            print ('\nfound steam install in "%s"'%SteamLocal)
                            continue
                else:
                    continue
            IDCheck = "%s/userdata"%(SteamLocal)
            for _ , dirs , _ in os.walk(IDCheck):
                for dir in dirs:
                    if len(dir) == 9:
                        SteamIDnum = dir
                        continue
        if OS == "Darwin":
            foundit = 1
            for Root , _ , Files in os.walk("/Users/%s/"%UserName):
                if foundit == 1:
                    for file in Files:
                        if "Steam" in Root:
                            for CorrectDir , _ , _ in os.walk(Root):
                                if foundit == 0:
                                    continue
                                if ("userdata" in CorrectDir):
                                    foundit = 0
                                    print("found it")
                                    SteamLocal = Root
                                    print ('\nfound steam install in "%s"'%SteamLocal)
                                    continue
                            continue
                else:
                    continue
            IDCheck = "%s/userdata"%(SteamLocal)
            for _ , dirs , _ in os.walk(IDCheck):
                for dir in dirs:
                    if len(dir) == 9:
                        SteamIDnum = dir
                        continue
        return SteamIDnum , SteamLocal
    def getsettings():
        global SteamID , InstallLocation , DefaultCleanout , Proton
        #settings are layed out like "SteamID , Steam Install Location , cleanout by default"
        SettingFile = open("info/settings" , 'r')
        SavedSettings = SettingFile.read()
        SteamID , InstallLocation , DefaultCleanout , Proton = SavedSettings.split(' , ')
        if SavedSettings == "'' , '' , '' , ''":
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
            if OS == "Windows":
                Proton = "no"
            if OS == "Darwin":
                Proton = "no"
            if OS == "Linux":
                properanswer2 = 0
                while properanswer2 == 0:
                    EnableProton = input("\nwould you like to enable proton for running windows games?(THIS IS HIGHLY EXPERIMENTAL! IT MIGHT BE BROKEN DEPENDING ON THE GAME) (y/n)")
                    if EnableProton == ("y"):
                        Proton = "yes"
                        properanswer2 = 1
                    if EnableProton == ("n"):
                        Proton = "no"
                        properanswer2 = 1
            GetInstallLocation()
            SettingsWrite = open("info/settings" , 'w')
            SteamID = SteamID.replace(SteamID , SteamIDnum)
            InstallLocation = InstallLocation.replace(InstallLocation , SteamLocal)
            FullSettings = ('%s , "%s" , %s , %s'%(SteamID , InstallLocation , Cleanout , Proton))
            SettingsWrite.write(FullSettings)
        return SteamID , InstallLocation , DefaultCleanout
    def Cleanout():
        global ReplaceVDF
        if DefaultCleanout == 'yes':
            if OS == "Windows":
                BaseVDF = "info\\shortcuts.vdf"
                ReplaceVDF = ("%s\\userdata\\%s\\config"%(InstallLocation.replace('"','') , SteamID))
                if os.path.exists(ReplaceVDF+"\\shortcuts.vdf"):
                    os.popen('del "%s\\shortcuts.vdf"'%(ReplaceVDF))
                    os.popen('copy "%s" "%s"'%(BaseVDF , ReplaceVDF))
                else:
                    os.popen('copy "%s" "%s"'%(BaseVDF , ReplaceVDF))
            if OS == "Linux":
                BaseVDF = "info/shortcuts.vdf"
                ReplaceVDF = ("%s/userdata/%s/config"%(InstallLocation.replace('"','') , SteamID))
                os.system('rm "%s/shortcuts.vdf"'%(ReplaceVDF))
                os.system('cp "%s" "%s"'%(BaseVDF , ReplaceVDF))
            if OS == "Darwin":
                BaseVDF = "info/shortcuts.vdf"
                ReplaceVDF = ("%s/userdata/%s/config"%(InstallLocation.replace('"','') , SteamID))
                os.system('rm "%s/shortcuts.vdf"'%(ReplaceVDF))
                os.system('cp "%s" "%s"'%(BaseVDF , ReplaceVDF))
        return
    def CloseSteam():
        if OS == "Windows":
            def checkIfProcessRunningWin():
                if 'steam.exe' in os.popen("tasklist").read():
                    return "True"
                else:
                    return "False"
            if checkIfProcessRunningWin() == "True":
                os.system('"%s\\steam.exe" -shutdown'%(InstallLocation.replace('"',''))) #this closes steam before running the rest of the script
        if OS == "Linux":
            def checkIfProcessRunningLinux():
                SteamRunning = os.popen('ps -aux | grep steam').read()
                #print(SteamRunning)
                SteamSH = ("%s/steam.sh"%InstallLocation.replace('"',''))
                if SteamSH in SteamRunning:
                    return "True"
            if checkIfProcessRunningLinux() == "True":
                print("Steam is running. Stopping for shortcuts creation")
                os.system("pkill steam")
            else:
                print("\nSteam isn't running. Won't try to stop it\n")
                pass
        if OS == "Darwin":
            def checkIfProcessRunningMac():
                global SteamPID
                SteamPID = os.popen("pgrep steam").read()
                if SteamPID == '':
                    pass
                else:
                    return "True"
            if checkIfProcessRunningMac() == "True":
                print("Steam is running. Stopping for shortcuts creation")
                for ID in SteamPID.split("\n"):
                    if ID == '':
                        pass
                    else:
                        os.system("kill -HUP %s"%ID)
            else:
                print("\nSteam isn't running. Won't try to stop it\n")
                pass
        return
    def CheckDirs(OldRoot):
        F = open("info/Dirs.txt" , 'r')
        NewPaths = ""
        CheckForSplit = F.read()
        if CheckForSplit == '':
            if OS == "Windows":
                print ("\nNow lets add some folders for scanning!")
                DirsToCheck = input('\nWhat Directories would you like to have scanned?\nIf you are doing multiple then seperate them as follows(this is an example BTW):\n       C:\\Games\\ItchGames , C:\\Games\\EpicGames , C:\\Games\\OtherGames\nMake sure that you seperate all your directories with space and then a comma and then another space " , " \n')
                WriteDirs = open("info\\Dirs.txt" , 'w')
                WriteDirs.write(DirsToCheck)
            if OS == "Linux":
                DirsToCheck = input('\nWhat Directories would you like to have scanned\nIf you are doing multiple then seperate them as follows\n       /home/%s/.config/itch/apps , /home/other/Games\nMake sure that you seperate all your directories with space and then a comma and then another space " , " '%UserName)
                WriteDirs = open("info/Dirs.txt" , 'w')
                WriteDirs.write(DirsToCheck)
            if OS == "Darwin":
                DirsToCheck = input('\nWhat Directories would you like to have scanned\nIf you are doing multiple then seperate them as follows\n       /Users/%s/Library/Application Support/itch/apps , /Users/%s/Games\nMake sure that you seperate all your directories with space and then a comma and then another space " , " '%(UserName , UserName))
                WriteDirs = open("info/Dirs.txt" , 'w')
                WriteDirs.write(DirsToCheck)
        if CheckForSplit == '':
            CheckForSplit = DirsToCheck
        if " , " in CheckForSplit:
            PathExists = CheckForSplit.split(" , ")
            for CheckPath in PathExists:
                print(CheckPath)
                if os.path.exists(CheckPath):
                    getfiles(CheckPath , OldRoot)
                else:
                    print('it looks like "%s" is an invalid directory, skipping'%CheckPath)
                    for i in PathExists:
                        if i == CheckPath:
                            pass
                        else:
                            if len(NewPaths) > 1:
                                NewPaths = ("%s , %s"%(NewPaths , i))
                            else:
                                NewPaths = i
                    StripPaths = ("[" , "]" , "'")
                    for symbol in StripPaths:
                        if symbol in PathExists:
                            print("got to symbols")
                            PathExists = PathExists.replace(symbol , '')
                    WriteDirs = open("info/Dirs.txt" , 'w')
                    WriteDirs.write(NewPaths)
        else:
            if os.path.exists(CheckForSplit.replace("\n",'')):
                getfiles(CheckForSplit.replace("\n",'') , OldRoot)
            else:
                print('it looks like "%s" is an invalid directory, make sure you spelled everything (and capitalized if you are on linux/mac) correctly'%CheckForSplit)
                WriteDirs = open("info/Dirs.txt" , 'w')
                WriteDirs.write("")
    def getfiles(scandir , OldRoot):
        global GameName
        for Root , _ , Files in os.walk(scandir):
            for file in Files:
                if OS == "Windows":
                    if file.endswith(".exe"):
                        ExeFile = (os.path.join(Root , file))
                        InBlacklist(ExeFile)
                    if file == "index.html":
                        if OldRoot in os.path.join(Root , file):
                            pass
                        else:
                            _ , GameName , _ = Root.rsplit("\\",2)
                            OldRoot = GameName
                            HTMLFILE = (os.path.join(Root , file))
                            InBlacklist(HTMLFILE)
                if OS == "Linux":
                    CheckFile = os.path.join(Root , file)
                    ExeCheck = os.access(CheckFile, os.X_OK)
                    if str(ExeCheck) == "True":
                        ExecFile = (os.path.join(Root , file))
                        InBlacklist(ExecFile)
                    if file == "index.html":
                        if OldRoot in os.path.join(Root , file):
                            pass
                        else:
                            _ , GameName , _ = Root.rsplit("/",2)
                            OldRoot = GameName
                            HTMLFILE = (os.path.join(Root , file))
                            InBlacklist(HTMLFILE)
                    if Proton == "yes":
                        if file.endswith(".exe"):
                            ExeFile = (os.path.join(Root , file))
                            InBlacklist(ExeFile)
                    else:
                        pass
                if OS == "Darwin":# in macOS .app files are treated as folders for NO REASON!
                    if ".app" in Root:
                        NoRepeasts = 1
                        for i in SkipPath.split("\n"):
                            if i in Root:
                                NoRepeasts = 0
                                continue
                        if NoRepeasts == 1:
                            InBlacklist(Root)
    def InBlacklist(File):
        BLCheck = 0
        if File.endswith(BLread):
            BLCheck = 1
        if OS == "Windows" or "Linux":
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
            DLLcheck, _ = File.rsplit("\\", 1)
            for _ , _ , FL in os.walk(DLLcheck):
                for file in FL:
                    if file.endswith(".dll"):
                        DLLcheck1 = file
                        if (DLLcheck1 == "openvr_api.dll"):
                            inVRLibrary = ("1")
                            LaunchOptions = ('"-vr -vrmode openvr -HmdEnable 1"')
            DLLcheck , _ = File.rsplit("\\", 1)
            for _ , _ , FL in os.walk(DLLcheck):
                for file in FL:
                    if file.endswith(".dll"):
                        DLLcheck1 = file
                        if (DLLcheck1 == "OVRPlugin.dll"):
                            if inVRLibrary == ("0"):
                                LaunchOptions = ('"-vr -vrmode oculus"')
                            inVRLibrary = ("1")
        else:
            pass
        AddShortcut(File)
    def AddShortcut(File):
        if OS == "Windows":
            Run = ('"%s\\shortcuts.vdf" %s "" %s 0 1 1 %s 0 "Non-Steam-Game"'%(ReplaceVDF , split_path(File) , LaunchOptions , inVRLibrary))
            os.system("python shortcuts.py %s"%Run)
        if OS == "Linux":
            Run = ('"%s/shortcuts.vdf" %s "" %s 0 1 1 %s 0 "Non-Steam-Game"'%(ReplaceVDF , split_path(File) , LaunchOptions , inVRLibrary))
            os.system("python3 shortcuts.py %s"%Run)
        if OS == "Darwin":
            Run = ('"%s/shortcuts.vdf" %s "" %s 0 1 1 %s 0 "Non-Steam-Game"'%(ReplaceVDF , split_path(File) , LaunchOptions , inVRLibrary))
            os.system("python3 shortcuts.py %s"%Run)
    def main():
        getsettings()
        CloseSteam()
        Cleanout()
        CheckDirs(OldRoot)
        return
    main()
except:
    print("\n\n\n\noperation canceled by user using ctrl+c or an error occured\n\n")
