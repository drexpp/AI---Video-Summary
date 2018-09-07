set /p video="Introduce el NOMBRE y FORMATO del video a fragmentar: "
set /p fps="Introduce cada cuantos frames quieres almacenar el fotograma: "

ffmpeg -i $video -vf fps=fps=$fps captura-%d.png
pause
