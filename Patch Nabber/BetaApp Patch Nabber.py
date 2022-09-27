from sys import exit
from time import sleep
from os import getenv, linesep,system
from os.path import exists
from urllib.request import urlopen, urlretrieve
from json import loads

a = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
a = loads(a)["clientVersionUpload"]
print("Client version hash: "+a)
filepath = getenv("LOCALAPPDATA")+"\Roblox\Versions\\"

def littleTimmyPrevention():
    input("Did you install Roblox via running RobloxPlayerLauncher as administrator?\nTry reinstalling Roblox.\nDon't open a new issue regarding this if you installed Roblox to a non-User directory!")

debug = False
if exists(filepath) and not debug:
    print("Found \"\Roblox\Versions\\\" folder!")
    filepath+=a
    if exists(filepath):
        print("Found \""+a+"\" folder!")
    else:
        print("[Error]: Unable to locate latest roblox client!")
        littleTimmyPrevention()
        exit(1)
else:
    print("[Error]: Could not find the \"\Roblox\Versions\\\" folder!")
    littleTimmyPrevention()
    exit(1)

repo = "klobyy/Roblox-Launcher"
rpl = "RobloxPlayerLauncher.exe"
latest = urlopen("https://raw.githubusercontent.com/"+repo+"/main/Custom%20Launcher/latest").read().decode().rstrip(linesep)
#input(latest) # debuggerydoos
print("Installing latest custom launcher from github! Version: "+latest)
download = urlretrieve("https://github.com/"+repo+"/releases/download/"+latest+"/"+rpl,filepath+"\\"+rpl)

print("File is located @",download.__getitem__(0)+"\nThis window will close in 3 seconds...")
for _ in range(3,0,-1):
    system("title "+"Closing in "+_.__str__())
    print('.')
    sleep(1)
exit(0)
