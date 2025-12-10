# voice-controlled-drawing


A simple Python project that listens for voice commands (e.g. "draw red circle and blue hexagon"), parses color+shape instructions, and draws the requested shapes on a random canvas using OpenCV. This repository is ideal for learning basic speech input, simple natural-language parsing, and drawing with OpenCV.

#### Features

- Listen to voice commands using the speech_recognition library.

- Parse multi-shape, multi-color instructions (e.g. "red circle, blue square").

- Draw many common shapes: circle, square, rectangle, triangle, line, ellipse, polygon, pentagon, hexagon, star, heart, diamond, parallelogram, trapezium, cross, and more.

- Display output in a Jupyter-friendly canvas (uses matplotlib to show images inline).

 #### Prerequisites

- Python 3.8+ installed.

- A working microphone for live voice input.

- On Windows, installing PyAudio can be a little tricky — see Troubleshooting below.

#### Installation (step-by-step)

1. Clone the repo (or create a new folder and copy the script):
```
git clone <your-repo-url>
cd voice-shape-drawer
```

2. Create and activate a virtual environment (recommended):
```
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd.exe)
venv\Scripts\activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
If you have trouble installing PyAudio on Windows, see Troubleshooting below.

4. Run the script

```
python scropt.py
```

When the program runs it will open your microphone and print Say a command (e.g., 'draw red circle and blue hexagon').... Speak a command clearly.

#### Troubleshooting

Microphone not found / permission error

 - Ensure your OS grants microphone access to Python.

 - Try switching to a different microphone device in speech_recognition.

PyAudio installation fails on Windows

 - Option A (recommended on Windows): install using pipwin which fetches prebuilt wheels:

```
pip install pipwin
pipwin install pyaudio
```

 - Option B: download and install the correct whl file for your Python version from a binary wheel site and pip install <whl-file>.

Google Speech API offline / errors

 -The default recognizer in speech_recognition uses Google Web Speech and requires internet access. You can use offline backends like pocketsphinx, but installation and accuracy differ.
