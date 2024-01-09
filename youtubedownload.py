import subprocess
import os

class YouTubeDownloader:
    def __init__(self, yt_dlp_path='yt-dlp', output_dir='output'):
        self.yt_dlp_path = yt_dlp_path
        self.output_dir = output_dir
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def download_video(self, url):
        command = [self.yt_dlp_path, '--no-playlist', '-f',
                   'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', '-o',
                   os.path.join(self.output_dir, '%(title)s.%(ext)s'), url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI

    def download_audio(self, url):
        command = [self.yt_dlp_path, '-x',
                   '--audio-format', 'mp3', '--no-playlist', '-o',
                   os.path.join(self.output_dir, '%(title)s.%(ext)s'), url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI