Procesador de datos de la central telefónica 131 y eSAMU
=======================

Este proyecto busca compilar los distintos informes que se pueden conseguir desde las plataformas informáticas del SAMU VIña del Mar.

Hoy se cuentan con dos softwares separados: llamadas (central Asterisk tipo elastix en servidor propio FreePBX) y datos clínicos de regulación e intervención en software de elaboración propia (eSAMU)

# Respecto a las llamadas
La compilación de las llamadas se hace de archivos CDR (Call Detail Record). El almacenamineto de los CDR se hace en la carpeta 'BD llamadas', el posterior procesamiento de los datos se realiza en la carpeta ' Compilador llamadas'. El producto queda como 'llamadas_contraspaso.pkl'.


## Mecanismo de compiación
Hay proceso de juntar BD, corregir información, y un programa propio que permite identificar con un 99,4% de áxito aquellas llamadas traspasadas. Todo lo anteror es realizado por un script bash que junta todos los actores anteriores

 - Juntar BD: se ejecuta el 'Complilacion llamadas.ipynb'. Este archivo se desarrolló en Jupyter para exploración visual de datos. De todas formas este archivo se utiliza para correr el software. Este archivo lee las BD y las junta en una sola llamada 'llamadas.pkl'.

 - Identificar las llamdas que son el resultado de un traspaso. Actualmente en el mundo de Asterisk es muy complejo identificar a través de CDR las llamadas taspasadas, para eso se creó un nuevo registro llamado CEL (Call Event Logging) que no está por ahora disponible en nuestra realidad. El CEL permite identificar claramente las llamadas que son el resultado de un traspaso. Se creó un script que identifica las llamadas que son el reultados de un traspaso al analizar: Tiempo de llamada, y si posteriormente este tiempo calza con una llamada a otro anexo. Este script lee 'llamadas.pkl' y  luego cre en el directorio principal el 'llamadas_contraspaso.pkl'.

# Respecto al eSAMU

Los archivos que se logran obtener para todos los efecto son 3:

-	Reporte Base: Reporte automático desarrollado por el departamento de informática que identifica entradas del eSAMU que tienen mezcla creación de incidentes, salidas de ambulancias y pacientes.
-	Tab_ambul_data.csv: Reporte de elaboración propia que se enfoca en datos de cada salida de ambulancia.
-	Tab_paciente_data.csv: Reporte de elaboración propia que se enfoca en datos de cada atención de paciente
-	Tab_REM_data.csv: Reporte de elaboración propia que se enfoca en datos de cada evento creado.

## Mecanismo de compilación
Aún no desarrollado




