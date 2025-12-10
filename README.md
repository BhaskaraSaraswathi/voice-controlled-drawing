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

Clone the repo (or create a new folder and copy the script):
```
git clone <your-repo-url>
cd voice-shape-drawer
```

Create and activate a virtual environment (recommended)
