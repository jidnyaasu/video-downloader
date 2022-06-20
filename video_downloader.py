import os
from threading import Thread
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font

from main import main

class DownloaderGui:

    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("600x400+650+300")
        self.root.configure(bg="#FCF2D8")

        # Label
        Label(self.root, text="Please paste Video Link here :  ", bg="#FCF2D8").place(
            anchor=CENTER, relx=0.5, rely=0.05
        )

        # url textbox
        self.url = Entry(self.root, width=50, borderwidth=3, bg="alice blue")
        self.url.pack()
        self.url.place(anchor=CENTER, relx=0.5, rely=0.15)

        # Paste button
        Button(self.root, text="Paste", command=self.paste, bg="pink").place(
            anchor=CENTER, relx=0.5, rely=0.25
        )

        # Output folder textbox
        Label(self.root, text="Please select output folder :  ", bg="#FCF2D8").place(
            anchor=CENTER, relx=0.5, rely=0.35
        )
        self.output_folder = Entry(self.root, width=50, borderwidth=3, bg="alice blue")
        self.output_folder.pack()
        self.output_folder.place(anchor=CENTER, relx=0.5, rely=0.45)

        # Defaulting output folder to Videos directory
        if os.name == "nt":
            self.videos_directory = os.path.expanduser("~") + "\\Videos\\"
        else:
            self.videos_directory = os.path.expanduser("~") + "/Videos/"
        self.output_folder.insert(0, self.videos_directory)

        # Select folder button
        Button(self.root, text="Select Folder", command=self.ask_folder, bg="pink").place(
            anchor=CENTER, relx=0.5, rely=0.55
        )

        # Download buttons
        # Best quality button
        self.best_button = Button(
            self.root,
            text="Download Best\nQuality Available\nin Any Format",
            bg="light green",
            command=self.download_best,
        )
        self.best_button.pack()
        self.best_button.place(anchor=CENTER, relx=0.35, rely=0.72)

        # mp4 format button
        self.mp4_button = Button(
            self.root,
            text="Download Best\nQuality Available\nin mp4 Format",
            bg="sky blue",
            command=self.download_best_mp4,
        )
        self.mp4_button.pack()
        self.mp4_button.place(anchor=CENTER, relx=0.65, rely=0.72)

        # Status Message
        self.label = Label(self.root, text="", bg="#FCF2D8")
        self.label.pack()
        self.label.place(anchor=CENTER, relx=0.5, rely=0.85)

        # Author info
        font = Font(family="Helvetica", weight="bold")
        author = Label(
            self.root, text="Software by: Saurabh Joshi", fg="maroon", bg="#FCF2D8", font=font
        )
        author.place(anchor=CENTER, relx=0.5, rely=0.95)

        self.root.mainloop()



    def download(self, mp4=False):
        if self.url.get():
            if mp4:
                self.mp4_button.config(bg="red")
                thr = Thread(target=main, args=[self.label, self.mp4_button, self.url.get(), self.output_folder.get(), mp4])
            else:
                self.best_button.config(bg="red")
                thr = Thread(target=main, args=[self.label, self.best_button, self.url.get(), self.output_folder.get(), mp4])
            thr.start()
        else:
            self.label.config(text="Please paste video url", fg="red")


    def download_best(self):
        self.download()


    def download_best_mp4(self):
        self.download(mp4=True)


    def paste(self):
        clipboard = self.root.clipboard_get()
        self.url.delete(0, tkinter.END)
        self.url.insert(0, clipboard)


    def ask_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            if os.name == "nt":
                folder += "\\"
            else:
                folder += "/"
            self.output_folder.delete(0, tkinter.END)
            self.output_folder.insert(0, folder)
