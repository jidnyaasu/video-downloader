import os
from tarfile import ExtractError
import yt_dlp


def get_video(url, folder, mp4):
    options = {
        "format": "bestvideo[ext!=webm]+bestaudio[ext!=webm]/best[ext!=webm]",
    }

    try:
        os.chdir(folder)
    except FileNotFoundError:
        os.mkdir(folder)
        os.chdir(folder)

    if mp4:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download(url)
    else:
        with yt_dlp.YoutubeDL() as ydl:
            ydl.download(url)


def main(label, button, url, output_folder, mp4):
    label.config(text="Downloading..... Please wait", fg="blue")
    try:
        get_video(url, output_folder, mp4)
        label.config(text="Download complete!", fg="green")
    except Exception as e:
        label.config(text=f"Please enter valid url", fg="red")
    
    finally:
        if mp4:
            button.config(bg="sky blue")
        else:
            button.config(bg="light green")
