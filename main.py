import sys
import time
import zipfile
import shutil
import wget
import requests
import os
import os.path
from os import system

#Values
mainFolder = 'C:/fiarlyy_updater/'
user = os.getlogin()
launcherVersion = 0.3

#Copyright claim
print("Copyright: Made by ! xDolarlar#9262")
system("title " + "Fiarlyy Updater (" + str(launcherVersion) + ")")

#Codes
if os.path.exists(mainFolder) == False:
    os.mkdir(mainFolder)

#Functions

def getLatestClientVersion():
    response = requests.get("https://raw.githubusercontent.com/DeyviMc/fiarlyy_updater/main/latestVersion.txt")
    return(response.text)
    
def getCurrentClientVersion():
    if os.path.exists(mainFolder + 'clientVersion.txt'):
        f = open(mainFolder + 'clientVersion.txt', "r")
        return(f.read())
    else:
        return(0)

def downloadFabric():
    print("Fabric indiriliyor (Fabric installer kullanarak!)")
    os.system("java -jar fabric-installer-0.11.1.jar client -mcversion 1.19.2 -loader 0.14.13")

def update():
    #Check
    if os.path.exists(mainFolder + 'mods.zip'):
        pass
    else:
        URL = "https://github.com/DeyviMc/fiarlyy_updater/raw/main/mods.zip"
        response = wget.download(URL, mainFolder + 'mods.zip')
        print("\nIndirme tamamlandı!")
    if os.path.exists('C:/Users/' + user + '/AppData/Roaming/.minecraft/mods'):
        shutil.rmtree('C:/Users/' + user + '/AppData/Roaming/.minecraft/mods')
    os.mkdir('C:/Users/' + user + '/AppData/Roaming/.minecraft/mods')
    os.replace(mainFolder + 'mods.zip', 'C:/Users/' + user + '/AppData/Roaming/.minecraft/mods/mods.zip')
    with zipfile.ZipFile('C:/Users/' + user + '/AppData/Roaming/.minecraft/mods/mods.zip', 'r') as zip_ref:
        zip_ref.extractall('C:/Users/' + user + '/AppData/Roaming/.minecraft/mods/')
    os.remove('C:/Users/' + user + '/AppData/Roaming/.minecraft/mods/mods.zip')
    if os.path.exists(mainFolder + 'clientVersion.txt') == False:
        with open(mainFolder + 'clientVersion.txt', 'w') as fp:
            pass
    f = open(mainFolder + 'clientVersion.txt', "w")
    f.write(str(getLatestClientVersion()))
    f.close()
    return(True)

#Codes

if os.path.exists('C:/Users/' + user + '/AppData/Roaming/.minecraft') == False:
    print("Minecraft bulunamadı!")
    time.sleep(3)
    sys.exit()

if os.path.exists('C:/Users/' + user + '/AppData/Roaming/.minecraft/versions/fabric-loader-0.14.13-1.19.2') == False:
    print("Fabric bulunamadı")
    downloadFabric()

if getLatestClientVersion() != getCurrentClientVersion():
    print("Mod paketiniz güncel değil! Güncelleniyor...")
    update()
else:
    print("Mod paketiniz güncel :)")

time.sleep(3)