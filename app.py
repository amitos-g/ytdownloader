import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import *
import os
import ctypes
"""
    this is a simple desktop app for downloading videos from youtube in mp4
    once the button is pressed,
    the code here will create a new directory in the folder you are in named 'yt_videos',
    and download the video you specified with a link to there.
    this simple app was created by amit ginat (me) and is using:
    
    * tkinter library for the gui
    * pytube library for the Youtube downloading
    
"""

def download_video():
    path = os.getcwd() + r"\yt_videos"

    url = text_box.get()
    invalid.pack_forget()
    try:
        youtube_object = YouTube(url)
        youtube_object = youtube_object.streams.get_highest_resolution()
        youtube_object.download(path)
        print(f"downloaded '{youtube_object.title}' to {path}")
        again = messagebox.askyesno("Download Successful", "Again?")
        if again:
            text_box.delete(0, tk.END)
        else:
            print()
    except PytubeError:
        print('er')
        invalid.pack()



#MAIN CODE


myappid = u'amitg.ytdownloader.one'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) # creating a unique APPID for the icon to show

# creating the window
window = tk.Tk()
window.title("Amit Ginat's YouTube Downloader")
window.geometry("1000x500")


# creating the 'enter url' label
label = tk.Label(window, text="Enter YouTube URL:", font=("Arial Bold", 40))
label.pack(pady=25) # padding y 40(from top)
label.pack()

window.wm_iconbitmap('./resources/icon.ico')
window.iconbitmap('./resources/icon.ico')

# creating a text box (apparently called Entry by tk)
text_box = tk.Entry(window, width=50, font=("Arial", 16))
text_box.pack(pady=10)

# creating a button and pointing it to the download_video command I made
button = tk.Button(window, text="Download", command=download_video, font=("Arial", 14))
button.pack(pady=15)


#create an invisible label saying the link is invalid
invalid = tk.Label(window, text="INVALID URL!", font=("Arial Bold Italic",  10) , fg="red")
invalid.pack(pady=10)
invalid.pack_forget()

# Start the main event loop
window.mainloop()


