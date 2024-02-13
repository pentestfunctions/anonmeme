import tkinter as tk
from screeninfo import get_monitors
from playsound import playsound
import threading
import os
import sys

class GifPlayer:
    def __init__(self, monitor, frames_directory="gif_frames", audio_file_path="audio_jungle.mp3"):
        self.monitor = monitor
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        self.frames_directory = os.path.join(base_path, frames_directory)
        self.audio_file_path = audio_file_path
        self.root = tk.Tk() if not hasattr(GifPlayer, 'root') else tk.Toplevel(GifPlayer.root)
        GifPlayer.root = self.root
        self.setup_window()
        self.setup_audio()

    def setup_window(self):
        self.root.geometry(f"{self.monitor.width}x{self.monitor.height}+{self.monitor.x}+{self.monitor.y}")
        self.root.overrideredirect(True)
        self.canvas = tk.Canvas(self.root, width=self.monitor.width, height=self.monitor.height)
        self.canvas.pack(fill="both", expand=True)
        self.load_and_display_frames()

    def load_and_display_frames(self):
        self.frames = [tk.PhotoImage(file=os.path.join(self.frames_directory, frame)) for frame in os.listdir(self.frames_directory) if frame.endswith('.png')]
        self.current_frame = 0
        self.update_frame()

    def update_frame(self):
        self.canvas.create_image(0, 0, anchor="nw", image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.root.after(100, self.update_frame)

    def setup_audio(self):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        audio_file_path = os.path.join(base_path, self.audio_file_path)
        threading.Thread(target=lambda: playsound(audio_file_path), daemon=True).start()

if __name__ == "__main__":
    monitors = get_monitors()
    players = []
    for monitor in monitors:
        player = GifPlayer(monitor)
        players.append(player)
    if players:
        players[0].root.mainloop()
