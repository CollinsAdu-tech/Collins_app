from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import yt_dlp

class CollinsLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="Collins App: YouTube Downloader"))

        btn = Button(text="Download Example Video")
        btn.bind(on_press=self.download_video)
        self.add_widget(btn)

    def download_video(self, instance):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # test video
        ydl_opts = {"outtmpl": "/sdcard/Download/%(title)s.%(ext)s"}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

class CollinsApp(App):
    def build(self):
        return CollinsLayout()

if __name__ == "__main__":
    CollinsApp().run()
