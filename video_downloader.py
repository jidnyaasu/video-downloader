import os
from threading import Thread
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font

from main import main

root = Tk()
root.title("Video Downloader")
root.geometry("600x400+650+300")
root.configure(bg="#FCF2D8")
root.config(pady=5, padx=5)


def download(mp4=False):
    if url.get():
        mp4_button.config(state=DISABLED)
        best_button.config(state=DISABLED)
        if mp4:
            thr = Thread(target=main,
                         args=[status_message, mp4_button, best_button, url.get(), output_folder.get(), mp4])
        else:
            thr = Thread(target=main,
                         args=[status_message, mp4_button, best_button, url.get(), output_folder.get(), mp4])
        thr.start()
    else:
        status_message.config(text="Please paste video url", fg="red")


def download_best():
    download()


def download_best_mp4():
    download(mp4=True)


def paste():
    clipboard = root.clipboard_get()
    url.delete(0, tkinter.END)
    url.insert(0, clipboard)


def ask_folder():
    if os.name == "nt":
        folder = filedialog.askdirectory() + "\\"
    else:
        folder = filedialog.askdirectory() + "/"
    output_folder.delete(0, tkinter.END)
    output_folder.insert(0, folder)


# Upper section
# Upper frame
upper_frame = Frame(root, bg="#FCF2D8")
upper_frame.pack(side="top", fill="both", padx=5, pady=5, expand=True)

# Label
first_label = Label(upper_frame, text="Please paste Video Link here :  ", bg="#FCF2D8")
first_label.pack(expand=True, padx=5, pady=5)

# url textbox
url = Entry(upper_frame, width=50, borderwidth=3, bg="alice blue")
url.pack(expand=True, padx=5, pady=5)

# Paste button
paste_button = Button(upper_frame, text="Paste", command=paste, bg="pink")
paste_button.pack(expand=True, padx=5, pady=5)

# Output folder textbox
output_folder_textbox = Label(upper_frame, text="Please select output folder :  ", bg="#FCF2D8")
output_folder_textbox.pack(expand=True, padx=5, pady=5)
output_folder = Entry(upper_frame, width=50, borderwidth=3, bg="alice blue")
output_folder.pack(expand=True, padx=5, pady=5)

# Defaulting output folder to Videos directory
if os.name == "nt":
    videos_directory = os.path.expanduser("~") + "\\Videos\\"
else:
    videos_directory = os.path.expanduser("~") + "/Videos/"
output_folder.insert(0, videos_directory)

# Select folder button
select_folder_button = Button(upper_frame, text="Select Folder", command=ask_folder, bg="pink")
select_folder_button.pack(expand=True, padx=5, pady=5)

# Download buttons section
# Button frame
button_frame = Frame(root, bg="#FCF2D8")
button_frame.pack(expand=True, padx=5, pady=5)

# Best quality button
best_button = Button(
    button_frame,
    text="Download Best\nQuality Available\nin Any Format",
    bg="light green",
    command=download_best,
)
best_button.grid(row=0, column=0, padx=25, pady=5)
best_button.rowconfigure(0, weight=1)

# mp4 format button
mp4_button = Button(
    button_frame,
    text="Download Best\nQuality Available\nin mp4 Format",
    bg="sky blue",
    command=download_best_mp4,
)
mp4_button.grid(row=0, column=1, padx=25, pady=5)

# Lower section
# Lower frame
lower_frame = Frame(root, bg="#FCF2D8")
lower_frame.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

# Status Message
status_message = Label(lower_frame, text="", bg="#FCF2D8")
status_message.pack(expand=True)

# Author info
font = Font(family="Helvetica", weight="bold")
author = Label(
    lower_frame, text="Software by: Saurabh Joshi", fg="maroon", bg="#FCF2D8", font=font
)
author.pack(expand=True)

root.mainloop()
