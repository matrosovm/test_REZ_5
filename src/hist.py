from sys import argv
from PIL import Image


def main():
    try:
        with Image.open(argv[1]) as in_image:
            in_image = in_image.convert("RGB")
            pixels = list(in_image.getdata())
        hyst = dict()
        for color in pixels:
            if color in hyst:
                hyst[color] += 1
            else:
                hyst[color] = 1
        for color, count in hyst.items():
            print(str(color) + ": " + str(count))
    except OSError:
        print("unable to open input image")


if __name__ == "__main__":
    main()
