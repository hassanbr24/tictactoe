Este archivo se ha creado a modo de explicar el juego "Tic-Tac-Toe" desarrollado en Python.
El juego se ha desarrollado gracias a la libreria Flask la cual nos permite interactuar con dicho juego a través
de API Rest.

Las instrucciones para iniciar el juego:

1: Ejecutar play.bat el cual es un archivo .bat que te abrirá dos ventanas CMDs automaticamente y te colocarás en el directorio del juego.
	1.1: En la primera ventana servidor de CMD se ejecuta index.py el cual es el script del juego con el que interacturameos desde la segunda ventana cliente CMD para trabajar con API Rest
	2.2: En la segunda ventana cliente CMD será en la que jugaremos.

2: Para iniciar la partida tenemos que ejecutar desde el cliente el siguiente comando:
	curl -UseBasicParsing http://127.0.0.1:5000/board
	Gracias a 'curl' podremos realizar peticiones HTTP para nuestro servidor.

3: Una vez ejecutado, nos pedirá introducir la contraseña que se muestra en el servidor.

4: A partir de entonces, recibiremos el tablero en formato JSON gracias a jsonily en el cliente.

5: Para que el jugador X comience a jugar, ejecutar en cliente:
	curl -X POST -H "Content-Type: application/json" -d "{\"row\": 1, \"col\": 0}" http://127.0.0.1:5000/play
	Donde row: 1 y col: 0 es la posicion donde se desea colocar la X

6: Al ejecutar el anterior comando recibiremos el tablero con la X en la posición introducida. El siguiente jugador O le tocaría jugar

7: Jugar asi sucesivamente hasta que se haya una línea de X o O y haya ganador. En caso de que no la haya, habrá empate. 
En ambas situaciones el juego termina y se puede iniciar otra partida.

8: Si un jugador juega en una posición que ya está rellena, saltará el mensaje de "Movimiento inválido"

	