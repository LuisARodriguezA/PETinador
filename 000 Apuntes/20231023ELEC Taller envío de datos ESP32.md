
2023-10-23
07:32:55
Tags: #UNAL #ELEC #ESP32
___
# Taller envío de datos ESP32
___

* El día de hoy realizamos un ejercicio con Node.js en el cual logramos controlar de forma remota al esp32 mediante la herramienta de Node.red
* Inicialmente la instalación e inicialización fue sencilla gracias al repertorio de fuentes del curso.
	* Se instalo Node.js
	* Se instalo Node.red
	* Se inicializa el servidor de Node.red
	* Se configura con los archivos base dados por el profesor.
	* Se conecta al COM6 para que se comunique con el ESP32.
		* Aquí encontramos el primer problema, pues no habíamos podido subir el .py al ESP32 directamente, solamente estábamos corriendo el código desde el Thonny
	* Después de esta configuración se pudo terminar de forma correcta la inicialización del servidor y se pudo controlar de forma exitosa el ESP32 de forma remota
	* Adicionalmente conseguimos controlarlo desde un dispositivo externo haciendo el debido **cambio de IP**.
- [x] #ELEC Setup ESP32 ⏫ 📅 2023-11-13 ✅ 2023-11-08
___
# Sources
1. [Microcontrolador enviando datos a red local](https://liascript.github.io/course/?https://raw.githubusercontent.com/johnnycubides/taller-ing-electronical-UNAL/main/README.md#37)
2. [Enviar datos desde microcontrolador a red local con Micropython y Node Red](https://www.youtube.com/watch?v=ZE4nFGTepT8)
___