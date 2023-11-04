from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from pytube import YouTube
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askokcancel
import youtube_dl
import threading
import os

window = Tk()
window.title("Video/Audio Downloader")
window.configure(background = "white")

def didNotWork():
    url_entry.delete(0, END)
    url_entry.insert(END, "That didn't work!  Try again.")

def onClickVideo():
    try:
        #get the YouTube html
        youtubeObject = YouTube(url_entry.get())
        #Create a file object indicating where to save the video, in mp4 format.
        file = filedialog.asksaveasfilename(filetypes = [('video', '*.mp4')], defaultextension = '.mp4', title = 'Save as a File')
        #Creates another youtube object in the highest resolution possible
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        #Downloads the object to the file chosen earlier
        youtubeObject.download(file)
    except:
        didNotWork()

def onClickAudio():
    try:
        #Get the YouTube html
        mp3_link = url_entry.get()  
        #create the audio object as an mp3
        audio = YouTube(mp3_link)    
        #Create a file object indicating where to save the audio, in mp3 format
        file = filedialog.asksaveasfilename(filetypes = [('audio', '*.mp3')], defaultextension = '.mp3', title = 'Save as a File')
        #Create an output object that is only the audio downloaded to the file object location
        output = audio.streams.get_audio_only().download(file)
        #Identify the paths for the download
        base, ext = os.path.splitext(output)
        #Create the new file name with the mp3 extension
        new_file = base + '.mp3'
        #rename the output file to the new file with extension
        os.rename(output, new_file)
    except:
        didNotWork()


##Create a label
Label (window, text = "YouTube Link: ", fg = "black", font = "none 12 bold", background="white"). grid(row = 0, column = 0, padx=20, pady=20)

##Create the text entry
url_entry = Entry(window, width = 16, bg = "white")
url_entry.grid(row = 0, column = 1, padx=20)

##Create a Button
vid = Button(window, text = "Download Video", command = onClickVideo).grid(row = 1, column = 0, sticky=E, pady=20, padx=20)
aud = Button(window, text = "Download Audio", command = onClickAudio).grid(row = 1, column = 1, sticky=W, pady=20, padx=20)

##Create a Button Frame


window.mainloop()