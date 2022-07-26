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


def main(app, mp4):
    app.status_message.config(text="Downloading..... Please wait", fg="blue")
    try:
        get_video(app.url.get(), app.output_folder.get(), mp4)
        app.status_message.config(text="Download complete!", fg="green")
    except Exception as e:
        app.status_message.config(text=f"Please enter valid url", fg="red")
        print(e)
    
    finally:
        app.best_button.config(state="normal")
        app.mp4_button.config(state="normal")
