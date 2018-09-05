import os
import cv2
from matplotlib import pyplot as plt
import glob

def recorre_imagenes():
    path="prueba"

    for image in os.listdir(path):
        input_path = os.path.join(path, image)
        listaFrames = []

        print (input_path)

        img = cv2.imread(input_path)

        color = ('b', 'g', 'r')

        for i, col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(histr, color = col)
            plt.xlim([0,256])
            listaFrames.append(histr)

        plt.show()
    print(listaFrames)


if __name__ == '__main__':
    recorre_imagenes()
