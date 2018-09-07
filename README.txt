IMPORTANTE: En mac es normal que se cree un archivo temporal llamado .DS_store
si este archivo se encuentra en la carpeta que se encuentren las imagenes deberá
ser eliminado.

El código contiene 5 funciones auxiliares además de la principal "main"


Para particionar las imagenes he usado ffmpeg guardando los fotogramas con 
el nombre "captura-x.png", además se ha incluido un script en bash (tiene
versión windows y linux/mac) para realizar la partición de un video que se
encuentre en la carpeta donde se localice el script además de preguntar por el
número de fotogramas por segundo en los que se desea particionar, a mayor
cantidad es posible que se pierda más información.

La función "recorre_imagenes" se encarga de preguntar por la carpeta donde
se encuentren los fotogramas, posteriormente se calculan los histogramas para
los colores BGR (blue green red) y se realiza la media de los mismos con la
función auxiliar "summary_color". Gracias a una variable almacenada luego
podremos calcular el número de K con el método del punto de codo de manera
rápida y efectiva. Esta función devuelve la lista de frames para la función
"aplicarKMedias"

La función "summary_color" se encarga de calcular la media aritmética de los
colores.

"aplicarKMedias" recibe la lista de fotogramas y se encarga de clasificarlos por
el algoritmo de K-Medias previamente preparando los datos para ser representados
una vez que los clusteres sean encontrados. Se hará uso de la función del punto
de codo para que le sea mostrado al usuario una gráfica donde podrá decidir para
cada ejemplo que valor de K es mejor.

"elbowMethod" recibe un array con los valores si él número de fotogramas es
mayor de 20, se calculará hasta con un máximo de 20 centroides calculando su
puntuación a cada uno para posteriormente junto con la gráfica poder decidir
cual es el valor de K más eficiente.

"obtenerFramesEnOutputPath" recibe la lista de frames importantes como un array
con los nombres de los ficheros .png y su función principal es copiar los
fotogramas principales para el resumen de la carpeta INPUTPATH a la carpeta de
salida.


Deberemos crear una carpeta de entrada donde serán introducidas las fotografias
y una carpeta de salida donde serán devueltos los fotogramas claves del video.

Es recomendable usar otra carpeta donde se almacenarán los videos y donde se
podrá cortar, una vez aplicado el script para particionar el video, a la carpeta
de entrada.

Para usar el programa será necesario ejecutarlo como administrador junto con el
comando "sudo python3 VideoSummary.py", escribiremos la contraseña y nos pedirá
la carpeta  entrada donde se encuentren los fotogramas a procesar.
Nos aparecerá el nombre de los fotogramas siendo procesados.

Una vez finalice se nos mostrará una imagen para decidir el valor de K
atendiendo al método del punto de codo.

Deberemos introducir el valor en la terminal y nos mostrará los distintos grupos
encontrados por el algoritmo.

Una vez cerrada la ventana lo último será introducir el nombre de la carpeta de
salida donde se almacenarán los fotogramas clave.


El script puede no funcionar en windows si ffmpeg no se encuentra en el PATH.
