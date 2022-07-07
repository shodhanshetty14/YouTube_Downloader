import shutil
from tkinter import *
from tkinter import filedialog
from turtle import Screen, width
from pytube import YouTube
from moviepy.editor import VideoFileClip
import moviepy.editor as moviepy


# Wrinting the backend Functions
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_video():
    # Get the link of the video to be downloaded
    get_link = link_field.get()
    #Get the selected path of the user
    get_path = path_label.cget('text')
    screen.title("Downloading...") 
    # downloaded video
    mp4_clip = YouTube(get_link).streams.get_highest_resolution().download() 
    vid_clip = VideoFileClip(mp4_clip)
    vid_clip.close()  
    # move file to the selected directory / path
    shutil.move(mp4_clip, get_path)
    screen.title("Download Completed, Download Another files")


screen = Tk()
title = screen.title("Youtube video downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.configure(bg='lightgreen')
canvas.pack()

# adding image file
img = PhotoImage(file='YT.png')

# resizing of the image

img = img.subsample(2,2)
canvas.create_image(250, 80, image=img)

# linking the fields and Lable 
link_field = Entry(screen, width=50)
link_text = Label(screen, text = "Enter the Link of the video" ,font=('Arial', 15))

# Selection lable link
path_label = Label(screen, text = "Select the path",font=('Arial', 12))
path_btn = Button(screen, text = "Browse", command=select_path)

# adding the selction labels to the window / canvas
canvas.create_window(215, 280, window=path_label)
canvas.create_window(300, 280, window=path_btn) 

# adding the links to the window / canvas
canvas.create_window(250, 170, window=link_field)
canvas.create_window(250, 200, window=link_text, )

# Download button
download_btn = Button( screen, text = "Download", command = download_video )


# adding the download btn to the canvas
canvas.create_window(230, 350, window = download_btn)

screen.mainloop()
