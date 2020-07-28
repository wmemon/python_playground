import sys
import os
from PIL import Image

def input_folder():
    if not len(sys.argv) == 3:
        print("Need two arguements,"+ str(len(sys.argv)-1) +" given!")
        return None
    return [sys.argv[1],sys.argv[2]]

def convert_image(sd_list):
    if not sd_list:
        return None

    (source,destination) = sd_list
    (source,destination) = str(source),str(destination)
    """
    This function takes the source and destination folder to convert jpg to png simultaneously.
    :param source: source folder taken arg1
    :param destination: destination folder taken arg2
    :return: None
    """
    # Make a list of all the files inside the source folder if it exists.
    try:
        images = os.listdir(source)
        images = set(images)
    except FileNotFoundError:
        print("[!]The source directory does not exist. Try again!")
        return None
    # Check if the destination exists. If it does not, create destination.
    if not os.path.exists(destination):
        os.mkdir(destination)
    # Grab all pictures in a list , open and save it with png format.
    # Works only for windows. For other OS . Use pathlib module.
    for image in images:
        im = Image.open(f"{source}\\{image}")
        im.save(f"{destination}\\png_{os.path.splitext((os.path.splitext(image)[0]))[0]}.png", format='png')
    return None


