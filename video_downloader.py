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


def download(mp4=False):
    if url.get():
        if mp4:
            mp4_button.config(bg="red")
            thr = Thread(target=main, args=[status_message, mp4_button, url.get(), output_folder.get(), mp4])
        else:
            best_button.config(bg="red")
            thr = Thread(target=main, args=[status_message, best_button, url.get(), output_folder.get(), mp4])
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
upper_frame.pack(side="top", fill="both", expand=True)

# Label
first_label = Label(upper_frame, text="Please paste Video Link here :  ", bg="#FCF2D8")
first_label.pack(expand=True)

# url textbox
url = Entry(upper_frame, width=50, borderwidth=3, bg="alice blue")
url.pack(expand=True)
# url.place(anchor=CENTER, relx=0.5, rely=0.15)

# Paste button
paste_button = Button(upper_frame, text="Paste", command=paste, bg="pink")
paste_button.pack(expand=True)

# Output folder textbox
output_folder_textbox = Label(upper_frame, text="Please select output folder :  ", bg="#FCF2D8")
output_folder_textbox.pack(expand=True)
output_folder = Entry(upper_frame, width=50, borderwidth=3, bg="alice blue")
output_folder.pack(expand=True)
# output_folder.place(anchor=CENTER, relx=0.5, rely=0.45)

# Defaulting output folder to Videos directory
if os.name == "nt":
    videos_directory = os.path.expanduser("~") + "\\Videos\\"
else:
    videos_directory = os.path.expanduser("~") + "/Videos/"
output_folder.insert(0, videos_directory)

# Select folder button
select_folder_button = Button(upper_frame, text="Select Folder", command=ask_folder, bg="pink")
select_folder_button.pack(expand=True)

# Download buttons section
# Button frame
button_frame = Frame(root, bg="#FCF2D8")
button_frame.pack(expand=True)

# Best quality button
best_button = Button(
    button_frame,
    text="Download Best\nQuality Available\nin Any Format",
    bg="light green",
    command=download_best,
)
best_button.grid(row=0, column=0, padx=5, pady=5)
best_button.rowconfigure(0, weight=1)
# best_button.pack(side="left", anchor="e", expand=True)
# best_button.place(anchor=CENTER, relx=0.35, rely=0.72)

# mp4 format button
mp4_button = Button(
    button_frame,
    text="Download Best\nQuality Available\nin mp4 Format",
    bg="sky blue",
    command=download_best_mp4,
)
mp4_button.grid(row=0, column=1, padx=5, pady=5)
# mp4_button.pack(side="right", anchor="w", expand=True)
# mp4_button.place(anchor=CENTER, relx=0.65, rely=0.72)

# Bottom section
# Bottom frame
bottom_frame = Frame(root, bg="#FCF2D8")
bottom_frame.pack(side="bottom", fill="both", expand=True)

# Status Message
status_message = Label(bottom_frame, text="", bg="#FCF2D8")
status_message.pack(expand=True)
# label.place(anchor=CENTER, relx=0.5, rely=0.85)

# Author info
font = Font(family="Helvetica", weight="bold")
author = Label(
    bottom_frame, text="Software by: Saurabh Joshi", fg="maroon", bg="#FCF2D8", font=font
)
author.pack(expand=True)
# author.place(anchor=CENTER, relx=0.5, rely=0.95)

root.mainloop()
