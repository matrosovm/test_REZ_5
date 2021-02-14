from sys import argv
from PIL import Image


def main():
    try:
        with Image.open(argv[1], "r") as in_image:
            out_image = in_image.copy().transpose(Image.TRANSPOSE)
            out_image.save(argv[2])
    except OSError:
        print("unable to open input image")


if __name__ == "__main__":
    main()
