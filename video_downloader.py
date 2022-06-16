import os.path
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font

from main import main

root = Tk()
root.title("Video Downloader")
root.geometry("600x400+650+300")
root.configure(bg="#FCF2D8")


def download_best():
    complete = main(url.get(), output_folder.get())
    Label(root, text=complete, bg="#FCF2D8", fg="blue").place(anchor=CENTER, relx=0.5, rely=0.85)


def download_best_mp4():
    complete = main(url.get(), output_folder.get(), True)
    Label(root, text=complete, bg="#FCF2D8", fg="blue").place(anchor=CENTER, relx=0.5, rely=0.85)


def paste():
    clipboard = root.clipboard_get()
    url.delete(0, tkinter.END)
    url.insert(0, clipboard)


def ask_folder():
    folder = filedialog.askdirectory() + "/"
    output_folder.delete(0, tkinter.END)
    output_folder.insert(0, folder)


# Label
Label(root, text="Please paste Video Link here :  ", bg="#FCF2D8").place(
    anchor=CENTER, relx=0.5, rely=0.05
)

# url textbox
url = Entry(root, width=50, borderwidth=3, bg="alice blue")
url.pack()
url.place(anchor=CENTER, relx=0.5, rely=0.15)

# Paste button
Button(root, text="Paste", command=paste, bg="pink").place(
    anchor=CENTER, relx=0.5, rely=0.25
)

# Output folder textbox
Label(root, text="Please select output folder :  ", bg="#FCF2D8").place(
    anchor=CENTER, relx=0.5, rely=0.35
)
output_folder = Entry(root, width=50, borderwidth=3, bg="alice blue")
output_folder.pack()
output_folder.place(anchor=CENTER, relx=0.5, rely=0.45)

# Defaulting output folder to Videos directory
videos_directory = os.path.expanduser("~") + "/Videos/"
output_folder.insert(0, videos_directory)

# Select folder button
Button(root, text="Select Folder", command=ask_folder, bg="pink").place(
    anchor=CENTER, relx=0.5, rely=0.55
)

# Download buttons
Button(
    root,
    text="Download Best\nQuality Available\nin Any Format",
    bg="light green",
    command=download_best,
).place(anchor=CENTER, relx=0.35, rely=0.72)
Button(
    root,
    text="Download Best\nQuality Available\nin mp4 Format",
    bg="sky blue",
    command=download_best_mp4,
).place(anchor=CENTER, relx=0.65, rely=0.72)

# Author info
font = Font(family="Helvetica", weight="bold")
author = Label(
    root, text="Software by: Saurabh Joshi", fg="maroon", bg="#FCF2D8", font=font
)
author.place(anchor=CENTER, relx=0.5, rely=0.95)

root.mainloop()
