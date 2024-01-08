import subprocess


class YouTubeDownloader:
    def __init__(self, yt_dlp_path='yt-dlp'):
        self.yt_dlp_path = yt_dlp_path

    def download_video(self, url):
        command = [self.yt_dlp_path, '--no-playlist', '-f',
                   'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI

    def download_audio(self, url):
        command = [self.yt_dlp_path, '-x',
                   '--audio-format', 'mp3', '--no-playlist', url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI

    def download_playlist(self, url):
        command = [self.yt_dlp_path, '--yes-playlist', '-f',
                   'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI

    def download_all_playlists(self, channel_url):
        command = [self.yt_dlp_path, '--yes-playlist', '--match-filter', '!is_live',
                   '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', channel_url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI

    def download_playlist_as_mp3(self, url):
        command = [self.yt_dlp_path, '--yes-playlist',
                   '-x', '--audio-format', 'mp3', url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI

    def download_all_playlists_as_mp3(self, channel_url):
        command = [self.yt_dlp_path, '--yes-playlist', '--match-filter',
                   '!is_live', '-x', '--audio-format', 'mp3', channel_url]
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            print(line)  # replace this with code to update your GUI
