import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading
import cv2
import numpy as np
import pyautogui

class ScreenRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("EGO SR")
        self.root.geometry("350x200")
        self.root.config(background="#267573")
        self.root.resizable(False,False)

        self.recording = False
        self.filename = ""
        self.frames = []

        # Styling
        self.root.configure(bg="#267573")

        self.header_label = tk.Label(self.root, text="EGO Screen Recorder", font=("Helvetica", 20), bg="#f0f0f0")
        self.header_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording, bg="#32CD32", fg="white", font=("Helvetica", 12))
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_save_recording, bg="#FF4500", fg="white", font=("Helvetica", 12), state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_recording(self):
        self.recording = True
        self.start_button.config(text="Recording...", bg="lime", state=tk.DISABLED)
        self.stop_button.config(text="Stop Recording", bg="#FF4500", state=tk.NORMAL)
        threading.Thread(target=self.record_screen).start()

    def stop_save_recording(self):
        if self.recording:
            self.recording = False
            self.start_button.config(text="Start Recording", bg="#32CD32", state=tk.NORMAL)
            self.stop_button.config(text="Save Recording", bg="#4169E1")
        else:
            self.save_recording()

    def record_screen(self):
        self.frames = []  # Reset frames list
        while self.recording:
            # Take screenshot
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)

            # Convert RGB to BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.frames.append(frame)

    def save_recording(self):
        # Choose file location and name
        self.filename = filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("AVI files", "*.avi")])
        if not self.filename:
            return

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(self.filename, fourcc, 20.0, (self.frames[0].shape[1], self.frames[0].shape[0]))

        # Write frames to video file
        for frame in self.frames:
            out.write(frame)

        # Release the VideoWriter object
        out.release()

        messagebox.showinfo("Recording Saved", f"Recording saved as {self.filename}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenRecorder()
    app.run()
