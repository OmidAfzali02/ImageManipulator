import pywhatkit as pk
from stegano import lsb
import tkinter
from tkinter import filedialog
import cv2

modes = ["0", "1", "2", "3", "q"]

while True:
    def main():
        print("Welcome to Image Manipulator By Omid Afzali\n")
        print("0- Stegano graph encoding")
        print("1- Stegano graph decoding")
        print("2- ascii creator")
        print("3- Object detection")
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


    def stegano_graph_show(img):
        img = img

        try:
            reveal = lsb.reveal(img)
            print(f"Message revealed: \n{reveal}")
        except:
            print("Cannot find anything")


    def ascii(img):
        pk.image_to_ascii_art(img, "ascii art")


    def obj_det(mode, img):
        thres = 0.55  # threshold to detect objects
        classNames = []
        classFile = 'coco.names'
        with open(classFile, "rt") as f:
            classNames = f.read().rstrip('\n').split('\n')

        configPath = "./ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        weighPath = "./frozen_inference_graph.pb"

        net = cv2.dnn_DetectionModel(weighPath, configPath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        if mode == 0:
            img = cv2.imread(img)
            classIds, confs, bbox = net.detect(img, confThreshold=thres)
            if len(classIds) != 0:
                for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                    cv2.rectangle(img, box, color=(0, 0, 255), thickness=2)
                    cv2.putText(img, classNames[classId - 1].title(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 160), 1)
            cv2.imshow('Object Detector', img)
            cv2.waitKey(0)

        else:
            cap = img
            cap.set(3, 640)
            cap.set(4, 480)

            while True:
                success, img = cap.read()
                classIds, confs, bbox = net.detect(img, confThreshold=thres)

                if len(classIds) != 0:
                    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                        cv2.rectangle(img, box, color=(0, 0, 255), thickness=2)
                        cv2.putText(img, classNames[classId - 1].title(), (box[0] + 10, box[1] + 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 2)
                        cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 160), 1)
                cv2.imshow('Object Detector', img)
                key = cv2.waitKey(1)
                if key == 91 or key == 113:
                    break

            cap.release()


    mode = main()
    if mode == "0":
        print("Stegano graph encode mode loaded ")
        print("Select Image file:  ")
        img = tkinter.filedialog.askopenfilename()
        msg = input("Now enter your message:  ")
        stegano_graph_hide(img, msg)
        print("All done!\n Your stegano art is in the same folder as the image\n")

    elif mode == "1":
        print("Stegano graph decode mode loaded ")
        print("Select Image file:  ")
        img = tkinter.filedialog.askopenfilename()
        stegano_graph_show(img)

    elif mode == "2":
        print("ascii mode loaded ")
        print("Select Image file:  ")
        img = tkinter.filedialog.askopenfilename()
        ascii(img)
        print("All done!\n Your ascii art is in the same folder as the image\n")

    elif mode == "3":
        print("Object Detector loaded ")
        mode = input("0-from an image, 1-from webcam:  ")
        try:
            mode = int(mode)
        except:
            print("Please select from available modes ")
        if mode == 0:
            img = tkinter.filedialog.askopenfilename()
            obj_det(0, img)
        elif mode == 1:
            obj_det(1, cv2.VideoCapture(0))

    elif mode == "q":
        break
