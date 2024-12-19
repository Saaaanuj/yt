import yt_dlp
from pydub import AudioSegment
import os
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re

ydl_opts = {
    'format': 'bestaudio/best',  
    'outtmpl': 'C:/Users/sanuj/Downloads/sharrymaan/%(title)s.%(ext)s',  # Save with title as filename
}


def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

# Function to download videos and extract audio
def download_videos(query, max_videos):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(f"ytsearch{max_videos}:{query}", download=False)['entries']
            
            video_urls = [result['webpage_url'] for result in search_results]

            ydl.download(video_urls)
            print(f"Downloaded {len(video_urls)} videos for the query: '{query}'")
        
            audio_files = process_audio_files(video_urls)
  
            if not audio_files:
                print("No valid audio files to process.")
                return

            merged_audio = merge_audio(audio_files)
            
            merged_file_path = 'C:/Users/sanuj/Downloads/sharrymaan/merged_audio.mp3'
            merged_audio.export(merged_file_path, format='mp3')
            print(f"Merged audio saved at: {merged_file_path}")
          
            zip_path = 'C:/Users/sanuj/Downloads/sharrymaan/merged_audio.zip'
            zip_audio(zip_path, merged_file_path)
            
            # Send the zipped file by email
            send_email(zip_path)
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to process audio files (cut first 30 seconds)
def process_audio_files(video_urls):
    audio_files = []
    for url in video_urls:
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                video_title = info_dict.get('title', 'Unknown Title')  
            sanitized_title = sanitize_filename(video_title)
            file_name = f"C:/Users/sanuj/Downloads/sharrymaan/{sanitized_title}.mp3"
            
            
            if os.path.exists(file_name):
                audio = AudioSegment.from_mp3(file_name)
                # Cut the first 30 seconds
                audio = audio[30000:]  
                audio_files.append(audio)
                print(f"Processed: {file_name}")
            else:
                print(f"File not found: {file_name}")
        except Exception as e:
            print(f"Error processing {url}: {e}")
    return audio_files

def merge_audio(audio_files):
    if len(audio_files) > 0:
        merged_audio = audio_files[0]
        for audio in audio_files[1:]:
            merged_audio += audio
        return merged_audio
    else:
        return None

def zip_audio(zip_path, audio_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(audio_path, os.path.basename(audio_path))
    print(f"Audio files zipped to: {zip_path}")


def send_email(zip_path):
    sender_email = "add mail"
    receiver_email = "add mail"
    password = "add password"  # Use an app password or OAuth2 if 2FA is enabled

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Merged Audio File"

    # Attach the zip file
    with open(zip_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(zip_path)}')
        msg.attach(part)

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

search_query = input("What kind of videos do you want? ")
max_videos = input("How many videos do you want? ")

download_videos(search_query, max_videos)
