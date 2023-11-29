# Proyecto-Programacion-2 
 
## Descripción

En este proyecto final consta en un Simulador de Ecosistemas basado en programación
orientada a objetos que permite la representación y manipulación de diferentes biomas,
como selvas, desiertos, bosques templados, entre otros, utilizando una matriz para simular
Las interacciones de flora y fauna en un ambiente dinámico y visualmente accesible. Para este proyecto utilizamos las bibliotecas de Python como Pygame, math y random para la generación de ventanas y la creación de nuestro Ecosistema.

## Guia de instalacion. 

- Para instalar nuestro simulador del ecosistema  primero que nada uno de los requerimientos es tener instalado previamente instalado Visual Studio Code para poder ejectuar nuestro Simulador.

- Una vez dicho esto para instalar nuestro simulador solo basta con abrir el CMD o "símbolo del sistema" que se encuentra en nuestro ordenador y hacer un git clone a nuestro repositorio. 


 `git clone  https://github.com/saezjose/Proyecto-Programacion-2.git`    


 - una vez colocado el comando anteriormente mencionado, descargará todos los archivos necesarios para el buen funcionamiento de nuestra simulación.


 - abrimos Visual Studio Code.


 - y buscamos nuestra carpeta anteriormente descargada.


 - y listo tendremos nuestra simulación lista para ser utilizada.
   

## Manual de Uso.

Para utilizar nuestro simulador basta con ejecutar el archivo `mainprincipal.py` esto nos creará la siguiente ventana.

[![captura.png](https://i.postimg.cc/dtz4VXdT/captura.png)](https://postimg.cc/kBvxjTTn)


Esto nos muestra la simulación ejecutándose la cual nos muestra un bosque generado con matrices de manera aleatoria y además podemos observar un ecosistema de animales ya sean depredadores como sus presas las cuales tienen una lógica de que cuando el depredador se acerca a la presa hay una probabilidad de que la cacé o falle en el intento. además de ciclos de vida de los depredadores después de cierto tiempo el animal muere y también ciclos de reproducción de ambos lados tanto depredadores y presas después de una cierta cantidad de ciclos estos se reproducen. Y también está la existencia de ciclos de día y de noche después de cierta cantidad de ciclos se hace de día o de noche.

Ademas mientras se ejecuta nuestro simulador este guardara datos y crea un registro de los
eventos en un archivo (log) o un archivo de texto como podemos ver a continuacion.

[![Agregar-un-t-tulo.png](https://i.postimg.cc/8cPG0cwM/Agregar-un-t-tulo.png)](https://postimg.cc/r0b7d8Bw)


##Si deseamos realizar cambios a nuestra simulacion podemos hacer lo siguiente.

En la linea 14 y 16 de nuestro archivo `animales.py` podremos modificar la cantidad de ciclos o de tiempo de cada reproduccion de los animales y la distancia de caza que pueden tener los depredadores al cazar sus presas.

[![distancia.png](https://i.postimg.cc/Y0C9WMG2/distancia.png)](https://postimg.cc/Vr2myyW2)

Si deseamos modificar la generacion de nuestros animales podemos modificar la siguiente linea de codigo en nuestro archivo `animales.py`. 
en la parte del codigoque dice por ejemplo "`(Leon, 2, 2)`". la cual podemos modificar la aparicion de los animales generados en nuestra simulacion en este ejemplo podemos cambiar la cantidad de leones generados en nuestra simulacion. 

[![generacionanimales.png](https://i.postimg.cc/HnhL0bHV/generacionanimales.png)](https://postimg.cc/tnFypZsj)


En la linea 208 del archivo `animales.py` podemos cambiar el ciclo o el tiempo que pasa al cambiar el estado de horario de dia y noche.

[![ciclos-dias.png](https://i.postimg.cc/g222tYNv/ciclos-dias.png)](https://postimg.cc/kBLCBdr4)

Y en la linea 27 y 31 de nuestro archivo `plantas.py` podemos cambiar el tiempo de vida de las plantas podemos ajustar la cantidad de tiempo de vida estas mismas para que avance mas rapido o mas lento.

[![gestionarvelocidadplantas.png](https://i.postimg.cc/MpqdhLQ0/gestionarvelocidadplantas.png)](https://postimg.cc/qzDsKjQg)



