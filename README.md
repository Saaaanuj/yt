# YouTube Video Downloader with Audio Processing

This project is a Python script that automates the following tasks:

1. **Search for YouTube videos based on a user query**
2. **Download the top results as audio files**
3. **Process the audio by trimming the first 30 seconds**
4. **Merge all processed audio files into a single audio file**
5. **Compress the merged file into a ZIP archive**
6. **Email the final ZIP file to a specified email address**

---

## Features

- **Search and Download:** Allows the user to specify a query and number of videos to download.
- **Audio Trimming:** Automatically trims the first 30 seconds from the downloaded audio.
- **Audio Merging:** Combines all trimmed audio files into a single file.
- **File Compression:** Compresses the merged audio into a ZIP file for easy sharing.
- **Email Automation:** Sends the ZIP file to a specified recipient.

---

## Requirements

To run this script, you need the following:

- Python 3.7+
- Libraries:
  - `yt-dlp`
  - `pydub`
  - `smtplib`
  - `os`
  - `shutil`
  - `email`

### Install Dependencies

1. Install `yt-dlp` for downloading YouTube videos:
   ```bash
   pip install yt-dlp
   ```
2. Install `pydub` for audio processing:
   ```bash
   pip install pydub
   ```
3. Install `ffmpeg` (required for `pydub`):
   - For Windows: [Download from here](https://ffmpeg.org/download.html).
   - For Linux:
     ```bash
     sudo apt-get install ffmpeg
     ```
   - For Mac:
     ```bash
     brew install ffmpeg
     ```

---

## Usage

1. Clone the repository or copy the script to your local machine.
2. Run the script:
   ```bash
   python youtube_audio_processor.py
   ```
3. Provide inputs when prompted:
   - Search query (e.g., `Sharry Maan`)
   - Number of videos to download (e.g., `5`)
   - Recipient email address (e.g., `example@gmail.com`)

---

## How It Works

1. **Search and Download:**
   - The script uses `yt-dlp` to search for videos matching the query.
   - The audio of the top results is downloaded in MP3 format.

2. **Audio Processing:**
   - Each downloaded audio file is trimmed to remove the first 30 seconds using `pydub`.

3. **Merging Audio:**
   - All processed audio files are merged into a single file.

4. **File Compression:**
   - The merged audio file is compressed into a ZIP archive for convenient sharing.

5. **Email Automation:**
   - The final ZIP file is sent to the specified recipient via email using `smtplib`.

---

## Example

### Input
- Search query: `Sharry Maan`
- Number of videos: `5`
- Email ID: `example@gmail.com`

### Output
- Merged audio file: `sharrymaan_merged.mp3`
- Compressed file: `sharrymaan_audio.zip`
- Email sent to `example@gmail.com` with the ZIP file attached.

---

## Troubleshooting

### Common Issues

1. **`ffmpeg` Not Found:**
   - Ensure `ffmpeg` is installed and added to your system's PATH.

2. **Audio File Errors:**
   - Check if the downloaded files are valid and accessible.

3. **Email Sending Issues:**
   - Ensure that the SMTP settings and credentials are correctly configured.

---

## Future Enhancements

- Add support for downloading video formats.
- Allow more advanced audio editing options.
- Integrate with cloud storage platforms for sharing files.
- Implement a GUI for ease of use.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.

---