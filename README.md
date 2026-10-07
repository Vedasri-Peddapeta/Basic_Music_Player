# ♫ Melody — Basic Python Desktop Music Player

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00?style=for-the-badge)
![Pygame](https://img.shields.io/badge/Audio-Pygame_Mixer-00C853?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-bb86fc?style=for-the-badge)

**Melody** is a lightweight, dark-themed desktop MP3 music player built with **Python**, **Tkinter**, and **Pygame Mixer**. It provides a clean, distraction-free interface for loading and playing local `.mp3` audio tracks with responsive playback and volume controls.

---

## Features:

- **Modern Dark UI** — Sleek `#121212` dark palette with `#bb86fc` purple accents.
- **MP3 File Browser** — Native system file dialog to quickly browse and load `.mp3` tracks.
- **Full Playback Controls** — Play (`PLAY`), Pause (`Ⅱ`), Resume (`▶`), and Stop (`■`) functionality.
- **Smooth Volume Control** — Real-time continuous volume adjustment slider (`0%` – `100%`).
- **Live Status Feedback** — Dynamic track title and playback status indicators (`Song loaded ✓`, `Playing ♪`, `Paused`, `Stopped`).

---

## Tech Stack:

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.8+ | Core application logic |
| **GUI Framework** | `tkinter` & `filedialog` | Window layout, widgets, and file picker |
| **Audio Engine** | `pygame.mixer` | Audio decoding, playback, pause/unpause, and volume control |

---

## Getting Started

### 1. Prerequisites

Ensure you have **Python 3.8 or higher** installed on your system:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/Vedasri-Peddapeta/Basic_MUSIC_PLAYER.git
cd Basic_MUSIC_PLAYER
```

### 3. Install Dependencies

*(Optional)* Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python music_player.py
```

---

## How to Use:

1. Click **`LOAD`** to open the file chooser and select any `.mp3` file from your computer.
2. Click **`PLAY`** to start playback from the beginning of the selected track.
3. Use **`Ⅱ`** to pause playback, **`▶`** to resume from where you paused, or **`■`** to stop the track completely.
4. Drag the **Volume** slider at the bottom to adjust audio output in real time.

---
 
## Project Structure

```text
Basic_MUSIC_PLAYER/
├── music_player.py    # Main Tkinter GUI & Pygame Mixer application
├── requirements.txt   # Python package dependencies
├── .gitignore         # Ignored build, environment, and OS files
├── LICENSE            # MIT License
└── README.md          # Project documentation
```

---

##  License

This project is licensed under the [MIT License](LICENSE).
