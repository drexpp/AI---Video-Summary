import os
import cv2
from matplotlib import pyplot as plt
import glob
import pandas as pd
import numpy as np
#Kmeans algorithm implemented by sklearn also pairwise_distances for 
#obtatining the shortest representant of each cluster center.
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
#For copying images from source path to output path
import shutil

num_imagenes_en_path = 0
inputPath = ""

def recorre_imagenes():
    print('Indique el nombre de la carpeta donde se encuentran las imagenes')
    path = input()
    global inputPath
    inputPath = path
    listaFrames = []

    amount_images = 0
    for image in os.listdir(path):
        amount_images += 1
        input_path = os.path.join(path, image)
        histrRecord = []

        img = cv2.imread(input_path)

        #cv2.imshow('image', img)

        color = ('b', 'g', 'r')

        for i, col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,255])
            SummaryOfColor = summary_color(histr)
            histrRecord.append(SummaryOfColor)
        
        sum = 0
        for colors in histrRecord:
            sum += colors

        averageBGR = sum/3

        print('imagen procesada: ' + image) 
        listaFrames.append([input_path,averageBGR])

    #Global is used for updating global variable, later on it is used to select
    #the number of elbow samples
    global num_imagenes_en_path
    num_imagenes_en_path = amount_images
    return listaFrames
   

def summary_color(histr):
    result = 0
    colorSum = 0
    index = 0
    for idx, value in enumerate(histr):
        colorSum += value
        index = idx

    return colorSum/256


def aplicarKMedias(listaFrames):
    plt.rcParams['figure.figsize'] = (16, 9)
    plt.style.use('ggplot')

    data = pd.DataFrame({
        'x': [i for i in range(1, len(listaFrames))],
        'y': [listaFrames[i][1] for i in range(1, len(listaFrames))]
        })

    f1 = data['x'].values
    f2 = data['y'].values 

    X = np.array(list(zip(f1, f2)))

    colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    elbowMethod(X)

    print('Indique el número de K en referencia a la gráfica anterior')
    
    k_value = input()

    kmeans = KMeans(n_clusters=int(k_value)).fit(X)
    centroids = kmeans.cluster_centers_
    labels = kmeans.predict(X)
    asignar = []
    for row in labels:
        asignar.append(colores[row])
    
    C = centroids
    plt.scatter(X[:, 0], X[:, 1], c=asignar, s=20)
    plt.scatter(C[:, 0], C[:, 1], marker = '*', c=colores, s=100)
    
    plt.show()
    
    closest, _ = pairwise_distances_argmin_min(centroids, X)
     
    listaKeyFrames = []
    for captureNumber in closest:
        listaKeyFrames.append('captura-' + str(captureNumber)+'.png')

    return listaKeyFrames


def elbowMethod(X): 
    num_iterations = 5

    if num_imagenes_en_path > 20:
        num_iterations = 20
    elif num_imagenes_en_path > 10 and num_imagenes_en_path <= 20:
        num_iterations = 10
    else:
        print('Necesitas más fotogramas')
        exit()

    Nc = range(1, num_iterations)
    kmeans = [KMeans(n_clusters=i) for i in Nc]
    kmeans
    score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
    score
    plt.plot(Nc, score)
    plt.xlabel('Número de clusters')
    plt.ylabel('Puntuación de K')
    plt.title('Curva del codo')
    plt.show()

def obtenerFramesEnOutputPath(listaKeyFrames):
     print('Indique donde desea almacenar las imagenes resumen')
     outputPath = input()

     for image in os.listdir(inputPath):
         input_path = os.path.join(inputPath, image)

         for frame in listaKeyFrames:
             if image == frame:
                 fullSourcePath = os.path.abspath(input_path)
                 fullDestinationPath = os.path.abspath(outputPath)
                 shutil.copy(fullSourcePath, fullDestinationPath)


#Main function, 3 function calls
# - First: get all frames
# - Second: Obtain the key frames
# - Third: Get those key frames from INPUTPATH to OUTPUTPATH by copying them
if __name__ == '__main__':
    listaFrames = recorre_imagenes()
    listaKeyFrames = aplicarKMedias(listaFrames)
    obtenerFramesEnOutputPath(listaKeyFrames)
 
