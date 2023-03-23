import cv2
import numpy as np
from PIL import Image
from IPython.display import clear_output

def ascii_art(img, new_width=80):
    img = img.convert("L")
    width, height = img.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    img = img.resize((new_width, new_height))
    pixels = img.getdata()

    chars = ["B", "S", "#", "&", "@", "$", "%", "!", "*", ";", ":", ",", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    return ascii_image

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        ascii_frame = ascii_art(img)
        clear_output(wait=True)
        print(ascii_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
