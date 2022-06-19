import yt_dlp as yt
from tkinter import *
from tkinter import Tk, font, ttk


def display_options(*event):

    hide()
    
    ydl_opts = {}
    resolutions = []

    url = link.get()
    
    valid = valid_link(url)  # check the validity of link
 
    if valid:
        with yt.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False) 
            formats = meta.get('formats', meta) 
            vid_title = meta.get('title', meta) # gets the title

        title.config(text=f'Title: {vid_title}')
        title.place(x=220, y=70)

        for f in formats:
            resolutions.append(f['format']) #filter to only formats

        options['values'] = resolutions # sets combobox values to available resolutions

    else:
        error.config(text='Invalid link', fg='red')
        error.place(x=150, y=210)

def valid_link(link): # function to check validity of the link
   
    extractors = yt.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(link) and e.IE_NAME != 'generic':
            return True
    return False


def download():
    hide()
    res = option_lst.get()

    if res !=  'resolution':
        res = int(res[:res.find('-')].strip())
        
        ydl_opts = {'format': f'{res}', 
                    'outtmpl': r'C:\yourPath\%(title)s.%(ext)s'}  # specify your download path here

        url = link.get()
        
        with yt.YoutubeDL(ydl_opts) as ydl: 
            ydl.download([url])

    else:
        error.config(text='Invalid resolution', fg='red')
        error.place(x=150, y=210)
    
def hide():
    title.place_forget()
    error.place_forget()


root = Tk()
root.geometry('700x250')
root.title('YouTube Downloader')

link = StringVar()
option_lst = StringVar()

link.trace('w', display_options)
option_lst.set('resolution')

link_here = Label(root, text="Paste Here", font=(30))
link_here.place(x=220,y=40)

title = Label(root, text='')
title.place(x=220, y=230)

error = Label(root, text='')
error.place(x=220, y=210)

options = ttk.Combobox(root, textvariable=option_lst, state="readonly") 
options.place(x=300, y=210)

pasted = Entry(root,width=60,textvariable=link)
pasted.place(x=80,y=120)

Button(root,text="Download Video", width=20, bg="black", fg="gray", command=download).place(x=250,y=170)

root.mainloop()
