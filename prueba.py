import os
import cv2
from matplotlib import pyplot as plt
import glob

def recorre_imagenes():
    path="prueba"
    listaFrames = []

    for image in os.listdir(path):
        input_path = os.path.join(path, image)
        histrRecord = []


        print (input_path)

        img = cv2.imread(input_path)

        cv2.imshow('image', img)

        color = ('b', 'g', 'r')

        for i, col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(histr, color = col)
            plt.xlim([0,256])
            print('-----Color name --> '+ str(col))
            print(histr)
            SummaryOfColor = summary_color(histr)
            histrRecord.append(SummaryOfColor)

        
        print('-------New image---------')
       
        
        listaFrames.append([input_path,histrRecord])
        print(listaFrames)

        plt.show()


def summary_color(histr):
    result = 0
    colorSum = 0
    index = 0
    for idx, value in enumerate(histr):
        colorSum += value
        index = idx

    result = colorSum/(index+1)
    print('Color sum: ' + str(colorSum))
    print('index: '+ str(index+1))
    print('result: '+ str(result))
    return result

if __name__ == '__main__':
    recorre_imagenes()
