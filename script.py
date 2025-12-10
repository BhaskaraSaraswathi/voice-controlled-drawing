import cv2
import numpy as np
import random
import math
import speech_recognition as sr
from matplotlib import pyplot as plt

# ------------------------------------------------------------
# COLOR DICTIONARY
# ------------------------------------------------------------
color_dict = {
    "red": (0, 0, 255),
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (0, 255, 255),
    "purple": (255, 0, 255),
    "pink": (203, 192, 255),
    "brown": (19, 69, 139),
    "orange": (0, 140, 255),
    "grey": (128, 128, 128),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

shape_list = [
    "circle", "square", "rectangle", "triangle", "line",
    "ellipse", "pentagon", "hexagon", "polygon", "star",
    "diamond", "heart", "parallelogram", "trapezium", "cross"
]

# ------------------------------------------------------------
# DISPLAY CANVAS (Jupyter)
# ------------------------------------------------------------
def canvas_show(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()


# ------------------------------------------------------------
# VOICE INPUT
# ------------------------------------------------------------
def voice_processor():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a command (e.g., 'draw red circle and blue hexagon')...")
        audio = recognizer.listen(source)
        try:
            command_text = recognizer.recognize_google(audio)
            print("You said:", command_text)
            return command_text
        except:
            print("Could not understand voice.")
            return ""


# ------------------------------------------------------------
# PARSE COMMAND (multi-shape multi-color)
# ------------------------------------------------------------
def command_parser(text):
    words = text.lower().split()
    tasks = []
    current_color = None

    for word in words:
        if word in color_dict:
            current_color = color_dict[word]

        if word in shape_list:
            color = current_color if current_color else (0, 0, 0)
            tasks.append((word, color))
            current_color = None

        if word.isdigit():  # for polygon (custom sides)
            tasks.append(("polygon", (0, 0, 0), int(word)))

    return tasks


# ------------------------------------------------------------
# DRAWER FUNCTIONS
# ------------------------------------------------------------

def draw_polygon(canvas, center, radius, sides, color):
    pts = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides
        x = int(center[0] + radius * math.cos(angle))
        y = int(center[1] + radius * math.sin(angle))
        pts.append([x, y])
    pts = np.array(pts)
    cv2.polylines(canvas, [pts], True, color, 3)
    cv2.fillPoly(canvas, [pts], color)


def draw_star(canvas, center, size, color):
    points = []
    angle = 2 * math.pi / 5
    for i in range(10):
        r = size if i % 2 == 0 else size // 2
        x = int(center[0] + r * math.cos(i * angle))
        y = int(center[1] + r * math.sin(i * angle))
        points.append([x, y])
    cv2.fillPoly(canvas, [np.array(points)], color)


def draw_heart(canvas, center, size, color):
    x0, y0 = center
    for t in range(0, 360):
        rad = math.radians(t)
        x = int(x0 + size * 16 * (math.sin(rad))**3)
        y = int(y0 - size * (13 * math.cos(rad)
                             - 5 * math.cos(2 * rad)
                             - 2 * math.cos(3 * rad)
                             - math.cos(4 * rad)) / 15)
        canvas[y-2:y+2, x-2:x+2] = color


# ------------------------------------------------------------
# MASTER DRAW FUNCTION
# ------------------------------------------------------------
def draw_shape(canvas, shape, color):
    x, y = random.randint(50, 450), random.randint(50, 450)
    size = random.randint(30, 90)

    if shape == "circle":
        cv2.circle(canvas, (x, y), size, color, -1)

    elif shape == "square":
        cv2.rectangle(canvas, (x, y), (x + size, y + size), color, -1)

    elif shape == "rectangle":
        cv2.rectangle(canvas, (x, y), (x + size, y + size // 2), color, -1)

    elif shape == "line":
        x2, y2 = random.randint(50, 450), random.randint(50, 450)
        cv2.line(canvas, (x, y), (x2, y2), color, 5)

    elif shape == "triangle":
        pts = np.array([[x, y], [x + size, y], [x + size // 2, y - size]])
        cv2.fillPoly(canvas, [pts], color)

    elif shape == "ellipse":
        cv2.ellipse(canvas, (x, y), (size, size // 2), 0, 0, 360, color, -1)

    elif shape == "diamond":
        pts = np.array([[x, y-size], [x+size, y], [x, y+size], [x-size, y]])
        cv2.fillPoly(canvas, [pts], color)

    elif shape == "pentagon":
        draw_polygon(canvas, (x, y), size, 5, color)

    elif shape == "hexagon":
        draw_polygon(canvas, (x, y), size, 6, color)

    elif shape == "polygon":
        draw_polygon(canvas, (x, y), size, random.randint(5, 12), color)

    elif shape == "star":
        draw_star(canvas, (x, y), size, color)

    elif shape == "heart":
        draw_heart(canvas, (x, y), size // 2, color)

    elif shape == "parallelogram":
        pts = np.array([[x, y], [x + size, y], [x + size + 40, y + size], [x + 40, y + size]])
        cv2.fillPoly(canvas, [pts], color)

    elif shape == "trapezium":
        pts = np.array([[x, y], [x + size, y], [x + size - 40, y + size], [x + 40, y + size]])
        cv2.fillPoly(canvas, [pts], color)

    elif shape == "cross":
        cv2.rectangle(canvas, (x, y), (x + size // 3, y + size), color, -1)
        cv2.rectangle(canvas, (x - size // 3, y + size // 3), (x + size, y + 2*size//3), color, -1)


# ------------------------------------------------------------
# ENGINE
# ------------------------------------------------------------
def app_engine(tasks):
    canvas = np.ones((500, 500, 3), dtype=np.uint8) * 255
    for t in tasks:
        if len(t) == 2:
            shape, color = t
            draw_shape(canvas, shape, color)
    return canvas


# ------------------------------------------------------------
# MAIN APP
# ------------------------------------------------------------
text_cmd = voice_processor()
tasks = command_parser(text_cmd)

if not tasks:
    print("No valid shapes or colors detected.")
else:
    result = app_engine(tasks)
    canvas_show(result)

print("The End")
