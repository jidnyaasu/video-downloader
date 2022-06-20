from threading import Thread
from tkinter import *
from video_downloader import DownloaderGui
from main import main


app = DownloaderGui("VideoDownloaderApp")

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


def download_best_mp4():
    download(app, mp4=True)


app.url_label = Label(app.root, text="Changed text")
app.url_label.pack()

app.best_button.config(text="Download Best\nQuality Available\nin Any Format", command=download_best_mp4)
