from pytube import YouTube
from sys import argv
import platform
import psutil


def get_logged_users():
    # Get a list of currently connected users
    users = psutil.users()

    # Extract and print the names of logged-in users
    logged_usernames = [user.name for user in users]
    logged_username = logged_usernames[0]
    if logged_usernames:
        print("Logged-in users:")
        for username in logged_usernames:
            print(f"- {username}")
    else:
        print("No users currently logged in.")

    return logged_username

def download_video():
        
    link = argv[1]
    yt = YouTube(link)
    os_system = platform.system()
    print("Title: ", yt.title)

    print("View: ", yt.views)
    print("os_system: ", os_system)
    loggedAs = get_logged_users()
    yd = yt.streams.get_highest_resolution()
    
    if os_system == 'Windows':
        print("Os system detected: ", os_system)
        final_destination = r"C:\Users\{}\Downloads".format(loggedAs)
        print("Downloading to : ", final_destination)
    elif os_system == 'Linux':
        print("Os system detected: ", os_system)
        final_destination = r"/home/{}/".format(loggedAsLinux)
        print("Downloading to : ", final_destination)
    else: 
        print("Undetected OS system")
        final_destination = input("Undetected OS system, specify download destination: ")
        print("Downloading to : ", final_destination)
    yd.download(final_destination) 

if __name__ == "__main__":
    download_video()