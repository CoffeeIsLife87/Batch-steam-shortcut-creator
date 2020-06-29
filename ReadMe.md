## Prerequsites ##

 * [python 3](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe)

      make sure you click "add python to path" when installing

 * [steam](https://store.steampowered.com/)
      (duh)

## Usage ##

* Download/clone the repository or download the latest release 

* Run start.bat or run maker.py

* give it the info it needs to function

* sit back and let the script do the work

* enjoy! :)

## anouncements ##

I am pretty sure linux compatibility is done, however I have only tested it on stock ubuntu 20.04 LTS so there may be issues

The Re-Write is complete but I have not ported it to linux (I don't have linux or VM software and I don't care enought to install it but If I can get it to work in WSL then I will try)

Now Detects whether or not a game is a VR game based on whether or not one or both DLL files are present (openvr_api.dll / OVRPlugin.dll), (not working on linux)

It now removes old shortcuts (it does leave a "placeholder" shortcut tho)

It now detects whether or not your steam install is standard (and makes it easier for the user if it isn't)

It can now scan multiple directories (so you can add your itch.io games and your epic games store games as well as any others you may have)

fixed not being able to add a game/program that contained an "&" in the path/name

Now only requires python 3

## To Be Done ##

add proton option for .exe files on linux

more QA/testing

Mac OS support? (anybody want that? make an issue and I will work on it)

itch has HTML games so I should probably check on those

## other ##

I use [shortcut manager](https://github.com/CorporalQuesadilla/Steam-Shortcut-Manager) as well as ["documentation"](https://www.youtube.com/watch?v=dQw4w9WgXcQ) for setting the shortcuts
