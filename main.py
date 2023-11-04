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
window.title("Video and Audio Downloader")
window.configure(background = "white")

def didNotWork():
    url_entry.delete(0, END)
    url_entry.insert(END, "That link didn't work!  Try again.")

def onClickVideo():
    try:
        youtubeObject = YouTube(url_entry.get())
        file = filedialog.asksaveasfilename(filetypes = [('video', '*.mp4')], defaultextension = '.mp4', title = 'Save as a File')
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download(file)
    except:
        didNotWork()

def onClickAudio():
    try:
        mp3_link = url_entry.get()  
        # creating the YouTube object and passing the the on_progress function
        audio = YouTube(mp3_link)    
        file = filedialog.asksaveasfilename(filetypes = [('audio', '*.mp3')], defaultextension = '.mp3', title = 'Save as a File')
        output = audio.streams.get_audio_only().download(file)
        base, ext = os.path.splitext(output)
        new_file = base + '.mp3'
        os.rename(output, new_file)
    except:
        didNotWork()


##Create a label
Label (window, text = "YouTube Link: ", fg = "black", font = "none 12 bold"). grid(row = 0, column = 0 )

##Create the text entry
url_entry = Entry(window, width = 50, bg = "white")
url_entry.grid(row = 0, column = 1)

##Create a Button
Button(window, text = "Download Video", command = onClickVideo).grid(row = 1, column = 0)
Button(window, text = "Download Audio", command = onClickAudio).grid(row = 1, column = 1)

##Create a Button Frame


window.mainloop()