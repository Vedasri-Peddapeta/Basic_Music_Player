import tkinter as tk
from tkinter import filedialog
import pygame
import os

# ---------------- PYGAME SETUP ----------------
pygame.mixer.init()

song_path = None
is_paused = False


# ---------------- FUNCTIONS ----------------
def load_song():
    global song_path

    song_path = filedialog.askopenfilename(
        filetypes=[("MP3 Files", "*.mp3")]
    )

    if song_path:
        pygame.mixer.music.load(song_path)

        song_name = os.path.basename(song_path)
        song_label.config(text=song_name)

        status_label.config(text="Song loaded ✓")


def play_song():
    global is_paused

    if song_path:
        pygame.mixer.music.play()
        is_paused = False
        status_label.config(text="Playing ♪")


def pause_song():
    global is_paused

    if song_path:
        pygame.mixer.music.pause()
        is_paused = True
        status_label.config(text="Paused")


def resume_song():
    global is_paused

    if song_path and is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        status_label.config(text="Playing ♪")


def stop_song():
    global is_paused

    pygame.mixer.music.stop()
    is_paused = False
    status_label.config(text="Stopped")


def set_volume(value):
    volume = float(value)
    pygame.mixer.music.set_volume(volume)


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Melody Player")
root.geometry("430x560")
root.resizable(False, False)
root.configure(bg="#121212")


# ---------------- HEADER ----------------
title = tk.Label(
    root,
    text="♫  MELODY",
    font=("Arial", 24, "bold"),
    fg="#ffffff",
    bg="#121212"
)
title.pack(pady=(25, 5))


subtitle = tk.Label(
    root,
    text="Your little music player",
    font=("Arial", 10),
    fg="#888888",
    bg="#121212"
)
subtitle.pack()


# ---------------- ALBUM ART ----------------
album_frame = tk.Frame(
    root,
    width=260,
    height=260,
    bg="#1f1f1f"
)
album_frame.pack(pady=25)

album_frame.pack_propagate(False)

album_icon = tk.Label(
    album_frame,
    text="♫",
    font=("Arial", 90),
    fg="#bb86fc",
    bg="#1f1f1f"
)
album_icon.place(relx=0.5, rely=0.5, anchor="center")


# ---------------- SONG NAME ----------------
song_label = tk.Label(
    root,
    text="No song selected",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#121212",
    wraplength=350
)
song_label.pack(pady=(0, 5))


status_label = tk.Label(
    root,
    text="Load a song to begin",
    font=("Arial", 10),
    fg="#888888",
    bg="#121212"
)
status_label.pack()


# ---------------- PROGRESS BAR ----------------
progress = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    showvalue=False,
    length=330,
    bg="#121212",
    fg="#bb86fc",
    highlightthickness=0,
    troughcolor="#333333"
)
progress.pack(pady=15)


# ---------------- CONTROL BUTTONS ----------------
control_frame = tk.Frame(root, bg="#121212")
control_frame.pack()


def create_button(parent, text, command, width=6):
    return tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        height=2,
        font=("Arial", 10, "bold"),
        fg="white",
        bg="#242424",
        activebackground="#333333",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2"
    )


load_button = create_button(
    control_frame,
    "LOAD",
    load_song,
    7
)
load_button.grid(row=0, column=0, padx=5)


stop_button = create_button(
    control_frame,
    "■",
    stop_song,
    5
)
stop_button.grid(row=0, column=1, padx=5)


pause_button = create_button(
    control_frame,
    "Ⅱ",
    pause_song,
    5
)
pause_button.grid(row=0, column=2, padx=5)


resume_button = create_button(
    control_frame,
    "▶",
    resume_song,
    5
)
resume_button.grid(row=0, column=3, padx=5)


play_button = tk.Button(
    control_frame,
    text="PLAY",
    command=play_song,
    width=7,
    height=2,
    font=("Arial", 10, "bold"),
    fg="white",
    bg="#bb86fc",
    activebackground="#9c64d8",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2"
)
play_button.grid(row=0, column=4, padx=5)


# ---------------- VOLUME ----------------
volume_label = tk.Label(
    root,
    text="🔊  Volume",
    font=("Arial", 10),
    fg="#aaaaaa",
    bg="#121212"
)
volume_label.pack(pady=(25, 0))


volume = tk.Scale(
    root,
    from_=0,
    to=1,
    resolution=0.01,
    orient="horizontal",
    showvalue=False,
    length=250,
    command=set_volume,
    bg="#121212",
    fg="#bb86fc",
    highlightthickness=0,
    troughcolor="#333333"
)
volume.set(0.7)
volume.pack()


# ---------------- START GUI ----------------
root.mainloop()
