"""
Created by Bennhyon (often called Cuek)

This script takes all .mp4 files inside a folder and create .png thumbnails
with the same name using ffmpeg.exe.

This script has to be executed with at least 1 argument
in Windows CMD (you need to move to the directory where you have the mp4 files first):

python YATC.py *path_to_ffmpeg* [thumbnail_width] [thumbnail_height]

ex: python YATC.py D:/ffmpeg/bin/ffmpeg.exe 450 450 (works with antislashes)
"""


import os
import subprocess
import sys
try:
    ffmpeg_path = str(sys.argv[1])
    width = str(sys.argv[2])
    height = str(sys.argv[3])
except:
    print("Seems to be missing one or more argument(s), the script will be using the defaults")
    width=0
    height=0

#region Functions
def CorrectPath(path):
    #Returns true if valid, false if not
    return (":/"in path or ":\\" in path)and "ffmpeg.exe" in path
if not ffmpeg_path or not isinstance(ffmpeg_path,str) or not CorrectPath(ffmpeg_path):
    input("Invalid ffmpeg path \n should look like this : C:/Directory/ffmpeg.exe (\\ can be used)  \n Press any key to exit..")
    exit()
if not isinstance(width,str): width = "200"
if not isinstance(height,str): height = "200"

def GetLocalPath(): #Gets the local path of the directory
    lpath = os.path.realpath(__file__)
    namee = lpath.split("\\")[len(lpath.split("\\"))-1]
    path = lpath.strip(namee)
    return path
def FindWhere(inst,list): #Returns where the instance of an object is in the list, -1 if not present
    for i in range(len(list)):
        if inst == list[i]:
            return i
    else: return -1
#endregion
localPath = GetLocalPath()
print("local path:" , localPath)

files = os.listdir() #Gets all the filenames in the directory
pngFiles = []
mp4Files = []

#Adds mp4 and png files to lists to be used later
for i in range(len(files)):
    if ".png" in str(files[i]):
        pngFiles.append(localPath+files[i])
    elif ".mp4" in str(files[i]):
        mp4Files.append(localPath+files[i])
#endregion

#Adds filenames to list for easier use later
filenames = []
for i in mp4Files:
    filenames.append(i.split("\\")[len(i.split("\\"))-1].replace(".mp4",".png"))
print("thumbnails present",pngFiles)

#region Creates the thumbnails if they don't exist already
j = 0
i = ""
for i in mp4Files:
    #print(files[i])
    #print(localPath+fileNames[i])
    if i.replace(".mp4",".png") in pngFiles:
        print(i,"already has a thumbnail")
    else:
        print("Creating thumbnail for", i)
        print(width+"x"+height)
        subprocess.call([ffmpeg_path, '-i', i, '-n', '-ss', '00:00:00.000','-s',str(width)+'x'+str(height), '-frames:v','1',filenames[j]])

    j+=1
#endregion
