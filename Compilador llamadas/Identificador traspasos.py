import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import date, datetime, time, timedelta
from babel.dates import format_date, format_datetime, format_time, format_timedelta, Locale
import locale                                    # para tratar de poner espanol
#locale = Locale('es', 'CL')
#locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')  

import os
import runpy
from pyexcel_ods import get_data

BD = pd.read_pickle('./llamadas.pkl')
print(BD)


lista_llamdas_traspasadas = []
inicio = datetime.now()
print(inicio)
dum = BD.copy()
for x in dum.index.values:
    print (x)
    if dum.loc[x].Tipo_llamada != 'Entre SAMU':
        recive = dum.loc[x].Destino_nSIP
        rango = dum.loc[(dum.Fecha < dum.loc[x].Fin) & (dum.Fecha > dum.loc[x].Fecha)]
        #rango
        if (rango.shape[0] !=0):
            #(rango.Tipo_llamada == 'Entre SAMU')
            print('inicio shape ')
            print('SIP:', recive)
            rango.shape
            
            indice = list(rango.loc[
                (rango.Origen_n == recive) &
                (rango.Estado == 'Contestada')].tail(1).index
                         )
            if len(indice) !=0:
                print('INGRESADO!!', dum.loc[x].Fecha)
                lista_llamdas_traspasadas.append(indice[0])
                print(datetime.now() - inicio)
            print('fin shape ')
        print('------------------------------------')
    print('next')
len(lista_llamdas_traspasadas)
print(datetime.now() - inicio)

BD.loc[BD.index.isin(lista_llamdas_traspasadas), 'Trapaso'] = 'Si'
BD.loc[BD.index.isin(lista_llamdas_traspasadas)== False, 'Trapaso'] = 'No'

BD.Trapaso.value_counts()

BD.to_pickle('./llamadas_contraspaso.pkl')

print(BD.columns)

# end