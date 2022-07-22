from threading import Thread
from tkinter import *
from video_downloader import DownloaderGui
from main import main


root = Tk()
title = "VideoDownloaderApp"
app = DownloaderGui(root, title)


def download(app, mp4=False):
    if app.url.get():
        app.best_button.config(state=DISABLED)
        app.mp4_button.config(state=DISABLED)
        if mp4:
            # app.mp4_button.config(bg="red")
            thr = Thread(target=main, args=[app, mp4])
        else:
            # app.best_button.config(bg="red")
            thr = Thread(target=main, args=[app, mp4])
        thr.start()
    else:
        app.status_message.config(text="Please paste video url", fg="red")


def download_best():
    download(app)


def download_best_mp4():
    download(app, mp4=True)


app.best_button.config(text="Download best quality\navailable in any format", command=download_best)
app.mp4_button.config(text="Download best quality\navailable in mp4 format", command=download_best_mp4)

root.mainloop()
