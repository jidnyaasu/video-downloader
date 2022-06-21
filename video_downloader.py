import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from PIL import Image, ImageTk


class DownloaderGui:

    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("900x700+650+300")
        self.root.configure(bg="#FCF2D8")
        self.top = ImageTk.PhotoImage(file="youtube.png")
        Label(self.root, image=self.top).pack()

        # url textbox
        self.url_label = Label(self.root, text="Please paste Video Link here :  ", bg="#FCF2D8")
        self.url_label.place(anchor=CENTER, relx=0.5, rely=0.05)
        self.url = Entry(self.root, width=50, borderwidth=3, bg="alice blue")
        self.url.pack()
        self.url.place(anchor=CENTER, relx=0.5, rely=0.15)

        # Paste button
        self.paste_button = Button(self.root, text="Paste", command=self.paste, bg="pink")
        self.paste_button.place(anchor=CENTER, relx=0.5, rely=0.25)

        # Output folder textbox
        self.output_folder_label = Label(self.root, text="Please select output folder :  ", bg="#FCF2D8")
        self.output_folder_label.place(anchor=CENTER, relx=0.5, rely=0.35)
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
        self.select_folder_button = Button(self.root, text="Select Folder", command=self.ask_folder, bg="pink")
        self.select_folder_button.place(anchor=CENTER, relx=0.5, rely=0.55)

        # Download buttons
        # Best quality button
        self.best_button = Button(
            self.root,
            text="",
            bg="light green",
        )
        self.best_button.pack()
        self.best_button.place(anchor=CENTER, relx=0.35, rely=0.72)

        # mp4 format button
        self.mp4_button = Button(
            self.root,
            text="",
            bg="sky blue",
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
