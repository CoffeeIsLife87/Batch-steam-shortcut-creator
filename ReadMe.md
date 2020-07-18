# Prerequsites #

* [python 3](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe)

make sure you click "add python to path" when installing for windows

* http.server (for launching html games from steam)

this can be installed using  **pip install shttp**(on windows) or **pip3 install --user shttp** (on linux. --user is not required unless you are on fedora)

* [steam](https://store.steampowered.com/)
      (duh)

## Usage ##

* Download/clone the repository or download the latest release

* Run makerV3.py

* give it the info it needs to function

* sit back and let the script do the work

* enjoy! :)

## anouncements ##

HTML5/webGL games launch and are playable now

Fixed double shortcuts for games with 64bit and 32bit variants

Now supports linux as well as Proton(partially)

I am pretty sure linux compatibility is done, however I have only tested it on stock ubuntu 20.04 LTS and fedora 32 so there may be issues

The Re-Write is complete

Now only requires python 3

Now Detects whether or not a game is a VR game based on whether or not one or both DLL files are present (openvr_api.dll / OVRPlugin.dll), (not working on linux)

It now removes old shortcuts (it does leave a blank shortcut tho)

It now detects whether or not your steam install is standard (and makes it easier for the user if it isn't)

It can now scan multiple directories (so you can add your itch.io games and your epic games store games as well as any others you may have)

fixed not being able to add a game/program that contained an "&" in the path/name

## To Be Done ##

more QA/testing

## known issues ##

There are no icons for shortcuts on linux

## other ##

I use [shortcut manager](https://github.com/CorporalQuesadilla/Steam-Shortcut-Manager) for setting the shortcuts
