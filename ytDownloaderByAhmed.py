import tkinter
import customtkinter
import yt_dlp
from tkinter import filedialog
from PIL import Image, ImageTk
import io
import requests

def reset_fields():
    title_label.configure(text="Title: ")
    duration_label.configure(text="Duration: ")
    uploader_label.configure(text="Uploader: ")
    thumbnail_label.configure(image='', text="Thumbnail: ")
    progressBar.set(0)
    pPercentage.configure(text="0%")

def fetch_video_details():
    reset_fields()  # Reset fields before fetching new details
    try:
        ytlink = link.get()
        if ytlink:
            ydl_opts = {
                'quiet': True,  # Suppress output except errors
                'extract_flat': True  # Extract metadata without downloading
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(ytlink, download=False)

                # Update labels with video details
                title_label.configure(text=f"Title: \n \n  {info_dict.get('title', 'N/A')}")
                duration_label.configure(text=f"Duration: \n \n  {info_dict.get('duration', 'N/A')} seconds")
                uploader_label.configure(text=f"Uploader: \n \n  {info_dict.get('uploader', 'N/A')}")

                # Fetch and display thumbnail
                thumbnail_url = info_dict.get('thumbnail', '')
                if thumbnail_url:
                    response = requests.get(thumbnail_url)
                    image_data = io.BytesIO(response.content)
                    image = Image.open(image_data)
                    image.thumbnail((280, 280))  # Resize for display
                    thumbnail_image = ImageTk.PhotoImage(image)
                    thumbnail_label.configure(image=thumbnail_image, text="")
                    thumbnail_label.image = thumbnail_image

    except Exception as e:
        print("Error:", e)
        title_label.configure(text="Title: Error")
        duration_label.configure(text="Duration: Error")
        uploader_label.configure(text="Uploader: Error")
        thumbnail_label.configure(image='', text="Thumbnail: Error")  # Clear image if error

def button_function():
    try:
        ytlink = link.get()
        selected_quality = optionmenu.get()

        # Map quality options to yt_dlp format strings
        format_map = {
            "Best Quality": 'bestvideo+bestaudio/best',
            "Low Quality": 'best',
            "Audio Only": 'bestaudio/best'
        }

        ydl_opts = {
            'format': format_map.get(selected_quality, 'bestvideo+bestaudio/best'),
            'outtmpl': f'{download_path.get()}/%(title)s.%(ext)s',
            'progress_hooks': [on_progress],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(ytlink, download=True)


            print("Downloaded successfully!")
    except Exception as e:
        print("Error:", e)


def on_progress(d):
    if d['status'] == 'downloading':
        pPercentage.configure(text=f"{d['_percent_str']}")
        pPercentage.update()
        progressBar.set(float(d['downloaded_bytes']) / float(d['total_bytes']))

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        download_path.set(directory)

# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# The app's frame
my = customtkinter.CTk()
my.geometry("720x487")
my.title("YouTube Video Downloader")
my.resizable(False, False)  # Disable resizing

# TITLE
title = customtkinter.CTkLabel(my, text="YouTube Video Downloader \n by Ahmed Haitham")
title.pack(padx=10, pady=10)

# LINK INPUT
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(my, width=700, height=40, textvariable=url_var)
link.pack(padx=10, pady=5)

# Bind the link input to fetch video details
link.bind("<KeyRelease>", lambda event: fetch_video_details())

# DOWNLOAD DESTINATION
download_path = tkinter.StringVar(value="D:/Python project")
dest_frame = customtkinter.CTkFrame(my)
dest_frame.pack(padx=10, pady=10, fill="x")

dest_label = customtkinter.CTkLabel(dest_frame, text="Download Destination:")
dest_label.pack(side="left", padx=5, pady=5)

dest_entry = customtkinter.CTkEntry(dest_frame, width=400, textvariable=download_path, state='disabled')
dest_entry.pack(side="left", padx=5, pady=5)

dest_button = customtkinter.CTkButton(dest_frame, text="Choose Destination", command=select_directory)
dest_button.pack(side="left", padx=5, pady=5)

# VIDEO DETAILS AND THUMBNAIL
details_frame = customtkinter.CTkFrame(my)
details_frame.pack(padx=10, pady=5, fill="both", expand=False)

title_label = customtkinter.CTkLabel(details_frame, text="Title: ", anchor="w")
title_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")

duration_label = customtkinter.CTkLabel(details_frame, text="Duration: ", anchor="w")
duration_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")

uploader_label = customtkinter.CTkLabel(details_frame, text="Uploader: ", anchor="w")
uploader_label.grid(row=2, column=0, padx=5, pady=2, sticky="w")

thumbnail_label = customtkinter.CTkLabel(details_frame, text="", width=200, height=200)
thumbnail_label.grid(row=0, column=2, rowspan=3, padx=10, pady=5, sticky="e")

# PROGRESS, DOWNLOAD BUTTON, AND QUALITY MENU
bottom_frame = customtkinter.CTkFrame(my)
bottom_frame.pack(padx=10, pady=10, fill="x", expand=False)

# Configure columns for layout
bottom_frame.grid_columnconfigure(0, weight=1)  # Left side
bottom_frame.grid_columnconfigure(1, weight=0)  # Right side

pPercentage = customtkinter.CTkLabel(bottom_frame, text="0%")
pPercentage.grid(row=0, column=0, padx=5, pady=5)

progressBar = customtkinter.CTkProgressBar(bottom_frame, width=500, height=12)
progressBar.set(0)
progressBar.grid(row=1, column=0, padx=5, pady=5, sticky="w")

button = customtkinter.CTkButton(bottom_frame, text="Download", command=button_function)
button.grid(row=0, column=1, padx=10, pady=7, sticky="e")

quality_options = ["Best Quality", "Low Quality", "Audio Only"]
optionmenu = customtkinter.CTkOptionMenu(bottom_frame, values=quality_options)
optionmenu.set("Best Quality")
optionmenu.grid(row=1, column=1, padx=10, pady=7, sticky="e")

# RUN APP
my.mainloop()
