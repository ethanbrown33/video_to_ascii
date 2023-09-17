from cv2 import VideoCapture, cvtColor, COLOR_BGR2GRAY, resize
import os
from datetime import datetime
ART_SCALE = 8
SHADING = '..:oQ#'

cam = VideoCapture(0)
while True:
    result, image = cam.read()
    image = cvtColor(image, COLOR_BGR2GRAY)
    image = resize(image, (int((image.shape[0] // ART_SCALE) * 3), image.shape[1] // ART_SCALE))
    line = ""
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            line += SHADING[int((image[y, x]) // (256 / len(SHADING)))]
        line += "\n"
    os.system('cls')
    print(line)
