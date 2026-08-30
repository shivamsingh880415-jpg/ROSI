import os
import threading
import gtts
from PIL import Image, ImageEnhance

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

DOWNLOADS_DIR = "/sdcard/Download/"
ROSI_DIR = os.path.join(DOWNLOADS_DIR, "ROSI_Project")
if not os.path.exists(ROSI_DIR):
    os.makedirs(ROSI_DIR)

class ROSIApp(App):
    def build(self):
        self.title = "ROSI Smart AI"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.header = Label(
            text="ROSI AI Assistant", 
            font_size='22sp', 
            bold=True,
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.header)

        self.cmd_input = TextInput(
            text="ROSI lori sunao", 
            hint_text="Enter command (e.g. lori, scan, edit photo)",
            multiline=False, 
            size_hint_y=None, 
            height=50,
            font_size='16sp'
        )
        layout.add_widget(self.cmd_input)

        btn_speak = Button(
            text="SEND COMMAND TO ROSI", 
            size_hint_y=None, 
            height=60, 
            font_size='16sp',
            bold=True
        )
        btn_speak.bind(on_press=lambda x: self.process_command(self.cmd_input.text))
        layout.add_widget(btn_speak)

        self.log_label = Label(
            text="ROSI Engine Ready!", 
            size_hint_y=1, 
            halign='center', 
            valign='middle',
            font_size='15sp'
        )
        self.log_label.bind(size=self.log_label.setter('text_size'))
        layout.add_widget(self.log_label)

        return layout

    def update_status(self, text):
        Clock.schedule_once(lambda dt: setattr(self.log_label, 'text', text))

    def process_command(self, user_command):
        cmd = user_command.lower()
        self.update_status(f"Processing Command: '{user_command}'...")

        if "lori" in cmd or "song" in cmd or "sing" in cmd:
            threading.Thread(target=self.make_lori_task, args=(user_command,), daemon=True).start()
        elif "scan" in cmd or "file" in cmd or "download" in cmd:
            threading.Thread(target=self.scan_files_task, daemon=True).start()
        elif "edit" in cmd or "photo" in cmd or "image" in cmd:
            threading.Thread(target=self.edit_photo_task, daemon=True).start()
        else:
            threading.Thread(target=self.run_all_task, daemon=True).start()

    def make_lori_task(self, text):
        out_path = os.path.join(ROSI_DIR, "lullaby.mp3")
        try:
            tts = gtts.gTTS(text=text, lang='hi', slow=True)
            tts.save(out_path)
            self.update_status(f"ROSI Response:\nAudio Generated Successfully!\nSaved Path: {out_path}")
        except Exception as e:
            self.update_status(f"Error: {str(e)}")

    def scan_files_task(self):
        try:
            files = os.listdir(DOWNLOADS_DIR)
            self.update_status(f"ROSI Response:\nScanned {len(files)} files in Downloads folder.")
        except Exception as e:
            self.update_status(f"Error: {str(e)}")

    def edit_photo_task(self):
        in_path = os.path.join(DOWNLOADS_DIR, "test.jpg")
        if os.path.exists(in_path):
            out_path = os.path.join(ROSI_DIR, "edited_test.jpg")
            img = Image.open(in_path)
            img = ImageEnhance.Brightness(img).enhance(1.3)
            img.save(out_path)
            self.update_status("ROSI Response:\nPhoto edited and saved successfully!")
        else:
            self.update_status("ROSI Response:\n'test.jpg' file missing in Downloads.")

    def run_all_task(self):
        self.update_status("ROSI Response:\nCommand processed for custom prompt!")

if __name__ == "__main__":
    ROSIApp().run()
