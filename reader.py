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

   # Key                # Data Type  # Internal Name       # Delimiter     # Input             # Delimiter
#    full_entryID        =                                      '\x00'  +  var_entryID        +  '\x00'
#    full_appName        =  '\x01'  +  'appname'             +  '\x00'  +  var_appName        +  '\x00'
#    full_quotedPath     =  '\x01'  +  'exe'                 +  '\x00'  +  var_unquotedPath   +  '\x00'
#    full_startDir       =  '\x01'  +  'StartDir'            +  '\x00'  +  var_startDir       +  '\x00'
#    full_iconPath       =  '\x01'  +  'icon'                +  '\x00'  +  var_iconPath       +  '\x00'
#    full_shortcutPath   =  '\x01'  +  'ShortcutPath'        +  '\x00'  +  var_shortcutPath   +  '\x00'
#    full_launchOptions  =  '\x01'  +  'LaunchOptions'       +  '\x00'  +  var_launchOptions  +  '\x00'
#    full_isHidden       =  '\x02'  +  'IsHidden'            +  '\x00'  +  var_isHidden       +  '\x00\x00\x00'
#    full_allowDeskConf  =  '\x02'  +  'AllowDesktopConfig'  +  '\x00'  +  var_allowDeskConf  +  '\x00\x00\x00'
#    full_allowOverlay   =  '\x02'  +  'AllowOverlay'        +  '\x00'  +  var_allowOverlay   +  '\x00\x00\x00'
#    full_openVR         =  '\x02'  +  'OpenVR'              +  '\x00'  +  var_openVR         +  '\x00\x00\x00'
#    full_lastPlayTime   =  '\x02'  +  'LastPlayTime'        +  '\x00'  +  var_lastPlayTime
#    full_tags           =  '\x00'  +  'tags'                +  '\x00'  +  var_tags           +  '\x08\x08'
#
#    newEntry = full_entryID + full_appName + full_quotedPath + full_startDir + full_iconPath + full_shortcutPath + full_launchOptions + full_isHidden + full_allowDeskConf + full_allowOverlay + full_openVR + full_tags
#    return newEntry
