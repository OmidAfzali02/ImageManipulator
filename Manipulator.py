import pywhatkit as pk
from stegano import lsb
import tkinter
from tkinter import filedialog

modes = ["0", "1", "2", "3", "4", "5", "q"]

while True:
    def main():
        print("Welcome to Image Manipulator By Omid Afzali\n")
        print("0- Stegano graph encoding")
        print("1- Stegano graph decoding")
        print("2- ascii creator")
        print("q- Quit")

        mode = input("\nSelect preferred mode:  ")

        if mode not in modes:
            print("\nSelect an available mode!! ")
        else:
            return mode.lower()


    def stegano_graph_hide(img, msg):
        img = img
        res = 'stegano art.png'
        msg = msg

        try:
            lsb.hide(img, msg).save(res)
            print("done")
        except:
            print("Error occurred")

    mode = main()
    if mode == "0":
        print("Stegano graph encode mode loaded")
        print("Select Image file:  ")
        img = tkinter.filedialog.askopenfilename()
        msg = input("Now enter your message:  ")
        stegano_graph_hide(img, msg)
        print(f"All done!\n Your stegano art is in the same folder as the image\n")

    elif mode == "1":
        pass
    elif mode == "2":
        pass
    elif mode == "3":
        pass
    elif mode == "q":
        break
