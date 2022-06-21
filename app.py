from threading import Thread
from tkinter import *
from video_downloader import DownloaderGui
from main import main


root = Tk()
title = "VideoDownloaderApp"
app = DownloaderGui(root, title)

def download(app, mp4=False):
    if app.url.get():
        if mp4:
            app.mp4_button.config(bg="red")
            thr = Thread(target=main, args=[app.label, app.mp4_button, app.url.get(), app.output_folder.get(), mp4])
        else:
            app.best_button.config(bg="red")
            thr = Thread(target=main, args=[app.label, app.best_button, app.url.get(), app.output_folder.get(), mp4])
        thr.start()
    else:
        app.label.config(text="Please paste video url", fg="red")


def download_best():
    download(app)


def download_best_mp4():
    download(app, mp4=True)


app.best_button.config(command=download_best)

root.mainloop()
