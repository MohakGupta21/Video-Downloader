import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from pytube import YouTube


from moviepy.editor import *
import shutil
from tkinter.messagebox import *

def download_mp3():
    text = inputMp3Str.get()
    if text == "":
        tkinter.messagebox.showinfo(title="Alert",message="Enter Name of the file")
        return

    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading...")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)

    # code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile(text +'.mp3')
    audio_file.close()
    shutil.move(text +'.mp3',file_path)
    print("Download Complete")

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading...")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)

    # code for mp4
    video_clip.close()
    shutil.move(mp4,file_path)
    print("Download complete")
def getPath():
    path = filedialog.askdirectory()
    path_label.config(text=path)

root = Tk()
root.title('Video Downloader')
canvas = Canvas(root,width=400, height=350)
canvas.pack()


#App Label
app_label =Label(root,text="Video Downloader",fg="blue",font= ('Arial',20))
canvas.create_window(200,20,window=app_label)

#Entry to accept video URL
url_label = Label(root,text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,110,window=url_entry)

#path to download videos
path_label = Label(root,text="Select path to download")
path_button = Button(root,text="Select", command = getPath)

canvas.create_window(200,150,window=path_label)
canvas.create_window(200,180,window=path_button)

#download button
download_button = Button(root,text="Download", command = download)
canvas.create_window(200,240,window= download_button)

#Label and Entry for MP3 files
download_frame =Frame(root,width=100,height=50)
inputMp3Str = Entry(download_frame)
label = Label(download_frame,text="Enter text for MP3:")

label.grid(row=0,column=0)
inputMp3Str.grid(row=0,column=1)

canvas.create_window(200,270,window= download_frame)

#Download MP3 button
download_mp3_button = Button(root,text="Download MP3", command= download_mp3)
canvas.create_window(200,300,window= download_mp3_button)


root.mainloop()
