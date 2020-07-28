from googletrans import Translator
import pathlib
file = input("Please enter the file to translate:- ")
def translate_text():
    # Open and read The file to a list
    try:
        with open(file,mode='r',encoding="utf-8") as to_translate:
            list_translate = to_translate.readlines()
    except (FileNotFoundError,IOError):
        print("An error occurred, Please ensure that the file provided is correct.")
        exit(1)

    #Check if translated.txt is present
    ttext =pathlib.Path('translated.txt')
    if not ttext.exists():
        with open('translated.txt',mode='w',encoding="utf-8") as translated:
            translated.write("")
            print("[*]translated.txt did not exist. Creating the file.")

    # Open transalted.txt
    translated_dest = open('translated.txt',mode='a',encoding="utf-8")


    # Translate the file to hindi and append to translated.txt
    translator = Translator()
    for lines in list_translate:
        translated_dest.write(translator.translate(lines,dest='hi').text)
        translated_dest.write("\n")

    print("The text has been Translated to Hindi and stored in translated.txt")


translate_text()

