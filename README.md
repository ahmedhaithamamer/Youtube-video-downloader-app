# YouTube Video Downloader
![interface](https://github.com/user-attachments/assets/c4373493-5e36-438f-9567-9255f089e553)
## Overview
This is a Python-based YouTube video downloader with a user-friendly graphical interface built using `tkinter` and `customtkinter`. The application allows users to download videos in different qualities or as audio-only, displaying detailed video information before downloading.

## Features
- **Video Information Fetching**: Automatically fetch and display video title, duration, uploader, and thumbnail from a YouTube link.
- **Multiple Download Options**: Choose between Best Quality, Low Quality, or Audio Only formats for downloading.
- **Download Progress Tracking**: Real-time progress bar and percentage display during the download process.
- **Custom Download Location**: Select and specify the directory where the video will be saved.
- **Error Handling**: Provides feedback and handles errors during the download process.

## Requirements
- Python 3.6 or higher
- `tkinter` (comes pre-installed with Python)
- `customtkinter` (`pip install customtkinter`)
- `yt-dlp` (`pip install yt-dlp`)
- `Pillow` (`pip install Pillow`)
- `requests` (`pip install requests`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/youtube-video-downloader.git
    cd youtube-video-downloader
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
    ```bash
    python main.py
    ```

2. Enter a YouTube video URL in the input field.

3. Choose the download quality from the options provided.

4. Optionally, select a custom directory to save the downloaded video.

5. Click the "Download" button to start downloading. The progress bar and percentage will update as the download proceeds.

## Screenshots
> *Main Interface*
> 
![interface](https://github.com/user-attachments/assets/c4373493-5e36-438f-9567-9255f089e553)

> *Video for more details*
> 
https://youtu.be/nthU4VIoKK8



