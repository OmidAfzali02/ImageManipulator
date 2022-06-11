import pywhatkit as pk
from stegano import lsb
import tkinter
from tkinter import filedialog

modes = ["0", "1", "2", "3", "4", "5", "q"]

while True:
    def main():
        print("Welcome to Image Manipulator By Omid Afzali")
        print("0- Stegano graph encoding")
        print("1- Stegano graph decoding")
        print("q- Quit")

        mode = input("Select preferred mode:  ")

        if mode not in modes:
            print("Select an available mode!! ")
        else:
            return mode.lower()


    mode = main()
    if mode == "0":
        pass
    elif mode == "1":
        pass
    elif mode == "2":
        pass
    elif mode == "3":
        pass
    elif mode == "q":
        break
