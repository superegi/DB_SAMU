#!/bin/bash
echo 'Se ejecutará el compilador con las BDs'
sleep 2
date
jupyter nbconvert --execute --ExecutePreprocessor.timeout=1000 'Complilacion llamadas.ipynb'
date
sleep 1
echo 'Ya se juntó ecompilo. toca agregar las traspasadas'
date
python3 'Identificador traspasos.py'
date
sleep 1
