# Gestor de Eventos para Naves Mineras 
Inspirado en el universo de ciencia ficción de The Expanse, el proyecto tiene lugar en una nave minera de hielo y, como la radiación del espacio se lleva mal con la microelectrónica, he diseñado una sencilla aplicación de consola que permita la gestión consistente de eventos e inventario que se pueda ejecutar en ordenadores de hardware "antiguo y robusto".

El proyecto es una aplicación de consola que consiste en un gestor de eventos donde cuentas con un calendario, un inventario de objetos, un listado de personas y un conjunto de ubicaciones a manejar. La función principal es poder crear eventos sin que estos generen contradicciones con el inventario, listado de personas, ubicación, tipo de evento, eventos ya existentes y un listado de reglas específicas, todo ello representado en un conjunto de restricciones que se han de cumplir para poder guardar un nuevo evento en el calendario. Ésta y el resto de funciones se explican más a fondo en la sección 

## Lista de contenidos
- [Introducción](#gestor-de-eventos-para-naves-mineras)
- [Instrucciones de ejecución](#instrucciones-de-ejecución)
- [Instrucciones de uso](#instrucciones-de-uso)
  - [Ejemplo de uso](#ejemplo-de-uso)
- [Diseño del proyecto](#diseño-del-proyrcto)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Flujo de ejecución](#flujo-de-ejecución)
  - [Historia y experiencie](#historia-y-experiencia)


## Instrucciones de ejecución

1. Clone el [repositorio](https://github.com/cubangnocchi/ProgProject01-c25-26) usando **git bash**
    ```bash
       git clone https://github.com/cubangnocchi/ProgProject01-c25-26.git
    ```
2. Abra el directorio del proyecto en su consola. 
   
3. Ejecute el comando
    ```bash
    python main.py
    ``` 

###### ℹ️ debe tener instalado python 3.13.7

##### [↩ volver a lista de contenidos](#lista-de-contenidos)

## Instrucciones de uso

Una ves abierto el programa en su consola deberá abrirse un menú. Ahí se listaran las opciones y se le intruirá cómo accionarlas. A continuación un ejemplo de lo que debe esperar:
```
---[MAIN MENUE]---
[1] - list events
[2] - list items
[3] - list crew
[4] - add item to inventoory
[5] - create event
[6] - add crew member
[x] - exit
press a [key] + [Enter↲] to select one of the options:
```

##### [↩ volver a lista de contenidos](#lista-de-contenidos)

### Ejemplo de uso

texto

##### [↩ volver a lista de contenidos](#lista-de-contenidos)

## Diseño del proyrcto

texto

##### [↩ volver a lista de contenidos](#lista-de-contenidos)

### Estructura del proyecto

[src/ ](./src/) En esta carpeta se encuentra el código principal del proyecto que está dividido en las siguientes secciones:

- [calendar/](./src/calendar/) en esta sección se encuentra todo lo relativo al calendario:
  - [event/](./src/calendar/event_class/)
    - [event.py](./src/calendar/event_class/event.py) clase Event. Una instancia guarda un nombre, un intervalo de fechas, la listas de las llaves de la base de datos que corresponden a las personas y recursos asignados, una lista que representa las cantidades de los objetos asignados, el tipo de evento y el lugar en que tiene lugar. Cuennta con los métodos necesarios para [convertir al formato JSON](./src/calendar/event_class/event.py#89) y para [convertir de vuelta a una instancia de la clase](./src/calendar/event_class/event.py#104).
    - [interval.py](./src/calendar/event_class/interval.py) clase Interval. Una instancia consta de dos fechas en formato *datetime*, representando inicio y fin de un periodo de tiempo. Su función prinsipal es contener métodos que faciliten el manejo de fechas como conocer si [dos intervalos se solapan](./src/calendar/event_class/interval.py#24).
  - [calendar.py](./src/calendar/calendar.py) clase Calendar. Una instancia consta de una lista ordenada de eventos y una *fecha actual* de referencia. El orden de la lista de eventos se garantiza a través de [un método](./src/calendar/calendar.py#79) encargado de insertar cada evento agregado en la posición correcta con un algoritmo de búsqueda binaria. Tamién cuenta con conversión a formato JSON y de vuelta a instancia de clase.
- [data_base/](./src/data_base/): Aquí se enciuentra todo lo relativo a la persistencia de datos.
  - [data_management.py](./src/data_base/data_management.py) Este archivo es el encargado de cargar la información de la base de datos, convertirla a los formatos requeridos para su uso, convertirla de vuelta al formato JSON y guardarla. También cuenta con [un método](./src/data_base/data_management.py/#30) destinado a ofrecer un mínimo de datos predeterminados en caso de que no exista base de datos disponible.
  - [save01.json]()

##### [↩ volver a lista de contenidos](#lista-de-contenidos)

### Flujo de ejecución

texto

##### [↩ volver a lista de contenidos](#lista-de-contenidos)

### Historia y experiencia

texto

##### [↩ volver a lista de contenidos](#lista-de-contenidos)
