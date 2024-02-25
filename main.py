import tkinter as tk
from googleapiclient.discovery import build # pip install google-api-python-client
from googleapiclient.errors import HttpError

YOUTUBE_API_KEY = 'KEY'

class YouTubeNotifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Channel Notifier")
        
        self.channel_listbox = tk.Listbox(root, width=50)
        self.channel_listbox.pack(pady=10)
        self.channel_listbox.bind("<<ListboxSelect>>", self.show_video_status)
        
        self.status_label = tk.Label(root, text="", font=('Helvetica', 18))
        self.status_label.pack(pady=10)
        
        self.youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        self.load_channels()
    
    def load_channels(self):
        channels = ["UC_x5XG1OV2P6uZZ5FSM9Ttw", "UCPGzT4wecuWM0BH9mPiulXg"]
        
        for channel_id in channels:
            self.channel_listbox.insert(tk.END, channel_id)
    
    def show_video_status(self, event):
        selected_channel_index = self.channel_listbox.curselection()
        if selected_channel_index:
            selected_channel = self.channel_listbox.get(selected_channel_index)
            video_status = self.get_latest_video_status(selected_channel)
            self.status_label.config(text=video_status)
    
    def get_latest_video_status(self, channel_id):
        try:
            response = self.youtube.channels().list(part='contentDetails', id=channel_id).execute()
            uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            playlist_items = self.youtube.playlistItems().list(part='snippet', playlistId=uploads_playlist_id, maxResults=1).execute()
            if playlist_items['items']:
                return "1" 
            else:
                return "0" 
        except HttpError as e:
            return "Error: Couldn't fetch data. Check your API key or network connection."


if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeNotifierApp(root)
    root.mainloop()
