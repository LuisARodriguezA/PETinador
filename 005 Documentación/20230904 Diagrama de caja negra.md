2023-09-04
07:18:03
Tags: #academy #UNAL #ELEC 
___
# 2023-09-04 Diagrama de caja negra
___
* Diagrama de flujo
	* Representación gráfica de lo que hace nuestro proyecto
	* Diagrama de caja negra
		* Representa los sistemas
			* Recursos
			* Energía
			* Comunicación
		* Caja negra definida a la tecnología
			* Especifico sobre los sensores
			* Lista de componentes, datasheets  hojas de cálculo.
* El proyecto se divide en
	* Contenedor
		* Menos flexible
	* Software
	* Hardware
* La idea es poder traducir todo a energía
	* Analógico
		* Rango de valores
	* Digital
		* ON/OFF
![[diagrama-caja-negra-general.drawio.png]]
* El cerebro toma las decisiones a partir de las señales eléctricas que estamos cuantificando.
* Todo esto debe comunicarse entre si, comunicación por cable, wireless, etc...
* La comunicación con el usuario también es importante
	* Interfaz
	* UI
	* Celular, como medio de traducción para la información que ve el usuario.
## Energía
* La energía tiene que llegar al sensor, actuador, y al cerebro... ósea a todo.
* Hay que discutir todo esto **EN EQUIPO**
## Sensores
* Sondas de temperatura
* Presión
* Luz Rotación 
## Actuadores
* Servomotor
* Parlante 
* LED
## Controladores
* ADC
	* De análogo a digital
* DAC
	* De digital a analógico
* Transistor
	* Entada analógica que puede transformar en una gran señal
	* https://concepto.de/transistor/
* Diodo
	* Sometido a cambios de temperatura
## Arduino
* 8bits
* Tiene su RAM, ROM, etc.
* Programador, puerto tipo impresoras.
___
### Todo
- [x] #ELEC Diagrama de caja negra ⏫ 📅 2023-09-11 ✅ 2023-09-10
___
# Sources
1. 
___