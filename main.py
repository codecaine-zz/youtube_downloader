# Import the necessary modules
import threading
import PySimpleGUI as sg
from youtubedownload import YouTubeDownloader

def main():
    # Define the layout for the PySimpleGUI window
    layout = [
        [sg.Text('URL'), sg.Input(key='-URL-', size=(115, 1))],  # Input field for the URL
        # Buttons for each download method
        [sg.Button('Download Video'), sg.Button('Download as MP3'), sg.Button('Download Playlist'), sg.Button('Download All Playlists'), sg.Button('Download Playlist as MP3'), sg.Button('Download All Playlists as MP3')],
        [sg.Output(size=(120, 20))]  # Output element to display the output of the yt-dlp command from stdout and stderr
    ]

    # Create the PySimpleGUI window
    window = sg.Window('YouTube Downloader', layout)

    # Create a YouTubeDownloader object
    downloader = YouTubeDownloader()

    # Function to start a download in a separate thread
    def start_download(method, url):
        method(url)

    # Event loop for the PySimpleGUI window
    while True:
        event, values = window.read()  # Read an event and values from the window
        if event == sg.WINDOW_CLOSED:  # If the window was closed, break the loop
            break
        # If a button was clicked, start the corresponding download method in a separate thread
        elif event == 'Download Video':
            threading.Thread(target=start_download, args=(downloader.download_video, values['-URL-']), daemon=True).start()
        elif event == 'Download Audio':
            threading.Thread(target=start_download, args=(downloader.download_audio, values['-URL-']), daemon=True).start()
        elif event == 'Download Playlist':
            threading.Thread(target=start_download, args=(downloader.download_playlist, values['-URL-']), daemon=True).start()
        elif event == 'Download All Playlists':
            threading.Thread(target=start_download, args=(downloader.download_all_playlists, values['-URL-']), daemon=True).start()
        elif event == 'Download Playlist as MP3':
            threading.Thread(target=start_download, args=(downloader.download_playlist_as_mp3, values['-URL-']), daemon=True).start()
        elif event == 'Download All Playlists as MP3':
            threading.Thread(target=start_download, args=(downloader.download_all_playlists_as_mp3, values['-URL-']), daemon=True).start()

    # Close the window after the event loop is finished
    window.close()

# If this script is run directly (not imported as a module), call the main function
if __name__ == '__main__':
    main()