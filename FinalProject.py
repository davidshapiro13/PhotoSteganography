#David Shapiro
#May 2024
#User Interface for Photo Steganography
from photo_steg import PhotoSteganography
import os

def encode():
    file_name = input("Path of Image File: ")

    #Check files are correct
    if not file_name.lower().endswith(".png"):
        print("This program only works with PNGs.")
        return
    if not os.path.isfile(input_file_name):
        print(f"{file_name} Does Not Exist. Try again.")
        return
    
    new_file_name = input("Name of New File: ")
    file_or_text = input("Read from (f)ile or (c)onsole? ").lower()
    if file_or_text == 'f' or file_or_text == 'file':
        input_file_name = input("Text file name: ")
        if os.path.isfile(input_file_name):
            with open(input_file_name, 'r') as f:
                message = f.read()
        else:
            print(f"{input_file_name} Does Not Exist. Try again.")
    else:
        message = input("Message to Embed: ")
        
    steg = PhotoSteganography(file_name)
    success = steg.encode(message, new_file_name)
    if success:
        print("Done!")
    else:
        print("Message too long to encode...")

def decode():
    file_name = input("Path of Image File: ")

    #Check files are correct
    if not file_name.lower().endswith(".png"):
        print("This program only works with PNGs.")
        return
    if not os.path.isfile(file_name):
        print(f"{file_name} Does Not Exist. Try again.")
        return
    
    steg = PhotoSteganography(file_name)
    text = steg.decode()
    file_or_text = input("Output to (f)ile or (c)onsole? ").lower()
    if file_or_text == 'f' or file_or_text == 'file':
        output_file_name = input("Text file name: ")
        if not os.path.isfile(output_file_name):
            with open(output_file_name, 'w') as f:
                f.write(text)
        else:
            print(f"{output_file_name} Does Not Exist. Try again.")
    else:
        print(text)

def run():
    print("Steganography Encoder/Decoder")
    print("Created by David Shapiro")

    #Main loop
    while True:
        result = input("(e)ncode, (d)ecode or (q)uit? ").lower()

        #encode
        if result == 'e' or result == 'encode':
            encode()
        #decode
        elif result == 'd' or result == 'decode':
           decode()
        #Quit
        elif result == 'q' or result == 'quit':
            quit()
        #Wrong Input
        else:
            print("Not correct input. Try again.")

if __name__ == "__main__":
    run()