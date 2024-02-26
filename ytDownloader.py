from pytube import YouTube
from sys import argv
import platform

link = argv[1]
yt = YouTube(link)
os_system = platform.system()
print("Title: ", yt.title)

print("View: ", yt.views)
print("os_system: ", os_system)
yd = yt.streams.get_highest_resolution()
if os_system == 'Windows':
    print("Os system detected: ", os_system)
    final_destination = r"C:\Users\konra\Downloads"
elif os_system == 'Linux':
    print("Os system detected: ", os_system)
    final_destination = r"/home/masta4ce/Downloads"
else: 
    print("Undetected OS system")
    final_destination = input("Undetected OS system, specify download destination: ")

yd.download(final_destination) 