#!/bin/bash

read -p "Introduce el NOMBRE y FORMATO del video a fragmentar: " video

read -p "Introduce cada cuantos frames quieres almacenar el fotograma: " fps

ffmpeg -i $video -vf fps=fps=$fps captura-%d.png


