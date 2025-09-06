import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader  # 👈 Import Sound


class DownloaderApp(App):
    def build(self):
        self.title = "Collins App"  # App title

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Enter YouTube URL:")
        layout.add_widget(self.label)

        self.url_input = TextInput(hint_text="Paste URL here", multiline=False)
        layout.add_widget(self.url_input)

        # Download Video Button
        self.video_btn = Button(text="Download Video", size_hint=(1, 0.3))
        self.video_btn.bind(on_press=self.download_video)
        layout.add_widget(self.video_btn)

        # Download Audio Button
        self.audio_btn = Button(text="Download Audio (MP3)", size_hint=(1, 0.3))
        self.audio_btn.bind(on_press=self.download_audio)
        layout.add_widget(self.audio_btn)

        # Status Label
        self.status = Label(text="")
        layout.add_widget(self.status)

        # Load sounds
        self.success_sound = SoundLoader.load("success.mp3")  # success tone
        self.error_sound = SoundLoader.load("error.mp3")      # error tone

        return layout

    def play_success_sound(self):
        if self.success_sound:
            self.success_sound.play()

    def play_error_sound(self):
        if self.error_sound:
            self.error_sound.play()

    def download_video(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.status.text = "Please enter a URL."
            self.play_error_sound()
            return

        try:
            command = ["yt-dlp", "-f", "best", "-o", "%(title)s.%(ext)s", url]
            subprocess.run(command, check=True)
            self.status.text = "✅ Video download completed!"
            self.play_success_sound()
        except Exception as e:
            self.status.text = f"❌ Error: {e}"
            self.play_error_sound()

    def download_audio(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.status.text = "Please enter a URL."
            self.play_error_sound()
            return

        try:
            command = ["yt-dlp", "-x", "--audio-format", "mp3", "-o", "%(title)s.%(ext)s", url]
            subprocess.run(command, check=True)
            self.status.text = "✅ Audio (MP3) download completed!"
            self.play_success_sound()
        except Exception as e:
            self.status.text = f"❌ Error: {e}"
            self.play_error_sound()


if __name__ == "__main__":
    DownloaderApp().run()
