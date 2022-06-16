import os
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


def main(url, output_folder, mp4=False):
    get_video(url, output_folder, mp4)

    return "Download complete!"
