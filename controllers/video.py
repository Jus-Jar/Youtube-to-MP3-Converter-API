import yt_dlp
import os
import shutil

def download_video(videoObject, audio_only=True):
    # Define the Url and output directory
    video_url = videoObject['videoUrl']
    output_directory = "cache"
    
    # Define the options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio',
        'outtmpl': f'{output_directory}/%(id)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}] if audio_only else [],
    }

    try:
        # Use yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            video_file_path = ydl.prepare_filename(info_dict)

            # If we are downloading audio only, modify the file path for the mp3 extension
            if audio_only:
                video_file_path = video_file_path.replace('.webm', '.mp3').replace('.m4a', '.mp3')

            print(f"Downloaded file saved to: {video_file_path}")
            return video_file_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def clear_cache_folder(cache_folder="cache"):
    try:
        # Check if the folder exists
        if os.path.exists(cache_folder):
            # Loop through each file in the directory
            for filename in os.listdir(cache_folder):
                file_path = os.path.join(cache_folder, filename)

                # Check if it's a file or a directory
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Delete the file
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Delete the directory and its contents
            print(f"Cache folder '{cache_folder}' cleared.")
        else:
            print(f"Cache folder '{cache_folder}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")